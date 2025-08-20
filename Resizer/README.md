# 📷 Image Resizer CLI

**Autor:** Luma Escalpelo + ChatGPT
**Licencia:** Open Source

Un programa en Python para redimensionar imágenes de forma masiva, guardando los resultados en una subcarpeta llamada `resized`. El script permite ajustar las imágenes a un tamaño específico, conservar la proporción, rellenar con bordes (letterbox), o recortar para cubrir el área definida.

---

## 🚀 Instalación

1. Clona o descarga el repositorio donde tengas el script:

   ```bash
   git clone https://github.com/<usuario>/python-utilities.git
   cd python-utilities/Resizer
   ```

2. Instala las dependencias:

   ```bash
   pip install pillow
   ```

---

## ⚙️ Uso

Ejecuta el programa desde la terminal:

```bash
python3 resizer.py <ruta> <ancho> <alto> [opciones]
```

### Argumentos

* `<ruta>` → carpeta con las imágenes a procesar.
* `<ancho>` `<alto>` → dimensiones objetivo.
* `-d, --delete` → elimina los originales después de redimensionar (1 = sí, 0 = no). Por defecto: `0`.
* `--fit {stretch,max,min,letterbox}` → modo de ajuste:

  * **stretch**: fuerza exactamente (ancho, alto) sin conservar proporción (por defecto).
  * **max**: encaja dentro de (ancho, alto), conservando proporción. Ningún lado supera el límite.
  * **min**: cubre todo (ancho, alto), conservando proporción con recorte centrado.
  * **letterbox**: encaja dentro de (ancho, alto), conserva proporción y rellena con color.
* `--bg <color>` → color de fondo para `letterbox`. Formatos: `#RRGGBB` o `R,G,B`. Ejemplo: `--bg "255,255,255"`.

---

## 🖼️ Ejemplos

### 1. Redimensionar imágenes a 800×600 sin conservar proporción

```bash
python3 resizer.py ./fotos 800 600 --fit stretch
```

### 2. Ajustar a un máximo de 1080px por lado, conservando proporción

```bash
python3 resizer.py "/home/luma/Nextcloud/Golem Ex Machina/Fotos/Sesion Cindy Resize" 1080 1080 --fit max
```

### 3. Forzar tamaño exacto con recorte centrado (dimensión mínima)

```bash
python3 resizer.py ./fotos 1080 1080 --fit min
```

### 4. Encajar con franjas negras (letterbox)

```bash
python3 resizer.py ./fotos 1024 768 --fit letterbox --bg "0,0,0"
```

### 5. Eliminar originales después de redimensionar

```bash
python3 resizer.py ./fotos 1920 1080 --fit max --delete 1
```

---

## 📂 Salida

* El script genera una carpeta llamada `resized` dentro del directorio de origen.
* Los nombres de archivo originales se conservan.
* En caso de conflicto, se sobrescriben los archivos de la carpeta `resized`.

---

## 🛠️ Notas técnicas

* Soporta formatos: `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`.
* Si el formato de salida es **JPEG** y la imagen tiene canal alfa, se convierte automáticamente a RGB.
* Actualmente, los GIF animados se reducen al primer frame.

---

## 📜 Licencia

Este programa es de código abierto. Puedes usarlo, modificarlo y distribuirlo libremente.
