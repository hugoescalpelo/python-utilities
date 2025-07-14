import os
import argparse
import subprocess
from pathlib import Path
import shutil


def is_file_corrupted(file_path):
    """Usa ffmpeg para verificar archivos multimedia y file para imágenes."""
    ext = file_path.suffix.lower()

    if ext in [".mp4", ".mov", ".avi", ".mkv"]:
        try:
            result = subprocess.run([
                "ffmpeg", "-v", "error", "-i", str(file_path), "-f", "null", "-"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=30
            )
            return result.stderr.strip() != ""
        except Exception:
            return True

    if ext in [".jpg", ".jpeg", ".png", ".heic"]:
        try:
            result = subprocess.run([
                "file", str(file_path)
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
            output = result.stdout.lower()
            return "cannot open" in output or "corrupt" in output or "error" in output
        except Exception:
            return True

    return False  # No se analiza otro tipo de archivo


def print_progress(idx, total, bar_length=40):
    percent = idx / total
    filled_length = int(bar_length * percent)
    bar = "█" * filled_length + '-' * (bar_length - filled_length)
    print(f"\rProgreso |{bar}| {percent * 100:.2f}% ({idx}/{total})", end="")


def scan_directory(input_dir):
    input_path = Path(input_dir)
    files = [f for f in input_path.rglob("*") if f.is_file()]
    total = len(files)
    print(f"📂 Escaneando {total} archivos en {input_dir}")

    corrupted_dir = input_path / "corruptos"
    corrupted_dir.mkdir(exist_ok=True)

    corrupted = []

    for idx, file_path in enumerate(files, 1):
        print_progress(idx, total)
        if is_file_corrupted(file_path):
            corrupted.append(file_path)
            dest = corrupted_dir / file_path.name
            print(f"\n❌ Corrupto: {file_path.name} -> movido a {dest}")
            shutil.move(str(file_path), str(dest))

    print(f"\n✅ Escaneo completado. Archivos corruptos encontrados y movidos: {len(corrupted)}")

    return corrupted


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detector de archivos multimedia corruptos con reubicación automática")
    parser.add_argument("--input", required=True, help="Carpeta a escanear")

    args = parser.parse_args()
    scan_directory(args.input)
