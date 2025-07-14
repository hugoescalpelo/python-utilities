# EXIF Dynamic Renamer

**EXIF Dynamic Renamer** es un programa de código abierto creado por **Luma Escalpelo** en colaboración con **ChatGPT (OpenAI)**. Su propósito es renombrar masivamente archivos multimedia (fotos y videos) usando sus metadatos de manera rápida y eficiente.

Actualmente optimizado para rendimiento con procesamiento en batch mediante `exiftool` y visualización en consola con barra de progreso estilo Docker.

---

## 📌 Características principales

- Renombrado masivo de fotos y videos usando metadatos.
- Extracción automática de fecha de creación desde EXIF o fecha de modificación.
- Extracción del modelo de cámara/dispositivo cuando está disponible.
- Opción de **modelo predeterminado** para archivos sin información.
- Barra de progreso gráfica durante el proceso.
- **Lectura rápida** de metadatos con `exiftool -j`.
- Modo "prueba" sin modificar archivos (`--dry-run`).

---

## 📂 Estructura de nombre resultante

```
<ext>_<YYYY-MM-DD>_<HH-MM-SS>_<Model>.<ext>
```

Ejemplos:

```
jpg_2025-07-14_13-45-23_iPhone_15_Pro.jpg
mp4_2024-11-01_18-22-00_SonyA6000.mp4
```

---

## 🚀 Uso básico

### Renombrado directo:

```bash
python xdr.py --input "/ruta/a/carpeta"
```

### Con modelo predeterminado para archivos sin metadatos:

```bash
python xdr.py --input "/ruta/a/carpeta" --override-model "iPhone_15_Pro"
```

### Solo mostrar cambios (modo prueba):

```bash
python xdr.py --input "/ruta/a/carpeta" --override-model "iPhone_15_Pro" --dry-run
```

---

## ⚙️ Requisitos

- Python 3.9+
- Dependencias Python:
  ```bash
  pip install pathlib
  ```
- Dependencia externa:
  ```bash
  sudo dnf install exiftool   # Fedora
  sudo apt install libimage-exiftool-perl   # Debian/Ubuntu
  brew install exiftool       # macOS
  ```

---

## 📝 Notas adicionales

- Soporta: JPG, JPEG, HEIC, PNG, MP4, MOV, AVI, MKV.
- Reemplaza espacios y caracteres raros del modelo con guiones bajos.
- Para imágenes descargadas o editadas sin EXIF, usa fecha de modificación.
- Código enfocado en claridad, velocidad y control total.

---

## 🧑‍💻 Autoría y licencia

Creado por **Luma Escalpelo** y **ChatGPT (OpenAI)**.

Licencia: MIT. Puedes modificar, compartir y distribuir respetando la licencia.

> *Este software ayuda a gestionar archivos multimedia de manera sostenible y organizada.*

