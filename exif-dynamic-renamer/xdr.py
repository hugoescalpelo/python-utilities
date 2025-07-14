import os
import argparse
import shutil
import subprocess
import datetime
import json
from pathlib import Path
import time


def run_exiftool_batch(files, batch_size=500, corrupted_dir=None):
    data = []
    total_batches = (len(files) + batch_size - 1) // batch_size
    print(f"📥 Leyendo metadatos en {total_batches} lotes de hasta {batch_size} archivos...")

    for batch_idx in range(total_batches):
        batch_files = files[batch_idx * batch_size:(batch_idx + 1) * batch_size]
        try:
            result = subprocess.run([
                "exiftool",
                "-j",
                "-DateTimeOriginal",
                "-CreateDate",
                "-Model",
                "-MediaCreateDate",
                "-FileModifyDate",
                *[str(f) for f in batch_files]
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True, timeout=300)
            batch_data = json.loads(result.stdout)
            data.extend(batch_data)
            print(f"✅ Lote {batch_idx + 1}/{total_batches} completado ({len(batch_data)} archivos).")
        except Exception as e:
            print(f"[ERROR] Error en lote {batch_idx + 1}: {e}")
            for file in batch_files:
                print(f"❌ Moviendo archivo problemático: {file.name}")
                if corrupted_dir:
                    corrupted_dir.mkdir(exist_ok=True)
                    shutil.move(str(file), str(corrupted_dir / file.name))

    print(f"✅ Lectura completada: {len(data)} archivos procesados.")
    return data


def sanitize_model(model, fallback="UnknownModel"):
    if not model:
        return fallback
    model = model.replace(" ", "_")
    model = "".join(c for c in model if c.isalnum() or c == "_")
    return model


def get_best_date(item):
    for key in ["DateTimeOriginal", "CreateDate", "MediaCreateDate", "FileModifyDate"]:
        if key in item:
            return item[key]
    return None


def generate_new_name(file_path, date_str, model, existing_names):
    ext = file_path.suffix.lower().strip(".")
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y:%m:%d %H:%M:%S")
        formatted_date = date_obj.strftime("%Y-%m-%d_%H-%M-%S")
    except Exception:
        formatted_date = "unknown_date"
    base_name = f"{ext}_{formatted_date}_{model}"
    candidate_name = f"{base_name}.{ext}"
    count = 1
    while candidate_name in existing_names:
        candidate_name = f"{base_name}_{count}.{ext}"
        count += 1
    existing_names.add(candidate_name)
    return candidate_name


def print_progress(idx, total, bar_length=40):
    percent = idx / total
    filled_length = int(bar_length * percent)
    bar = "█" * filled_length + '-' * (bar_length - filled_length)
    print(f"\rProgreso |{bar}| {percent * 100:.2f}% ({idx}/{total})", end="")


def process_directory(input_dir, dry_run=False, override_model=None, batch_size=500):
    input_path = Path(input_dir)
    corrupted_dir = input_path / "corrupted"
    files = [f for f in input_path.rglob("*") if f.is_file()]
    print(f"📂 Detectados {len(files)} archivos para procesar.")

    exif_data = run_exiftool_batch(files, batch_size=batch_size, corrupted_dir=corrupted_dir)

    if not exif_data:
        print("[ERROR] No se obtuvieron datos EXIF")
        return

    existing_names = set()
    total = len(exif_data)

    for idx, item in enumerate(exif_data, 1):
        src_file = Path(item.get("SourceFile"))
        date_str = get_best_date(item)
        model = item.get("Model")

        if not date_str:
            print(f"\n[WARNING] Sin fecha en {src_file.name}, usando fecha de modificación")
            date_str = datetime.datetime.fromtimestamp(src_file.stat().st_mtime).strftime("%Y:%m:%d %H:%M:%S")

        if not model or model.strip() == "":
            folder_name = src_file.parent.name
            if override_model:
                model = sanitize_model(override_model)
            else:
                print(f"\n[UNKNOWN MODEL] {src_file.name}")
                user_input = input(f"Modelo para {src_file.name} [default: {folder_name}]: ").strip()
                model = sanitize_model(user_input or folder_name)
        else:
            model = sanitize_model(model)

        new_name = generate_new_name(src_file, date_str, model, existing_names)
        new_path = src_file.parent / new_name

        print_progress(idx, total)

        if not dry_run:
            src_file.rename(new_path)
        time.sleep(0.005)

    print("\n✅ Renombrado completado.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="EXIF Dynamic Renamer optimizado usando batch de exiftool con detección de colisiones, lectura por lotes y manejo de archivos corruptos")
    parser.add_argument("--input", required=True, help="Carpeta a procesar")
    parser.add_argument("--dry-run", action="store_true", help="Mostrar cambios sin aplicar")
    parser.add_argument("--override-model", type=str, help="Modelo de cámara para todos los archivos sin modelo")
    parser.add_argument("--batch-size", type=int, default=500, help="Cantidad de archivos por lote para lectura de metadatos")

    args = parser.parse_args()
    process_directory(args.input, dry_run=args.dry_run, override_model=args.override_model, batch_size=args.batch_size)
