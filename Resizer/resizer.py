import os
import argparse
from PIL import Image, ImageOps

# Configuración del analizador de argumentos
parser = argparse.ArgumentParser(
    description=(
        "Resize images to a specified resolution and save them in a 'resized' subfolder. "
        "Optionally, delete the original images. "
        "Uso de --fit:\n"
        "  stretch   -> fuerza tamaño exacto (no conserva proporción)\n"
        "  max       -> encaja dentro de (W,H), conserva proporción (sin recorte)\n"
        "  min       -> cubre (W,H), conserva proporción (recorte centrado)\n"
        "  letterbox -> encaja y rellena con color para llegar a (W,H)\n"
    )
)
parser.add_argument('path', type=str, help='Path to the folder with images.')
parser.add_argument('width', type=int, help='Width of the resized images.')
parser.add_argument('height', type=int, help='Height of the resized images.')
parser.add_argument('-d', '--delete', type=int, choices=[0, 1], default=0,
                    help='Delete original files after resizing (1 for yes, 0 for no).')

# NUEVO: modo de ajuste y color de fondo para letterbox
parser.add_argument('--fit', choices=['stretch', 'max', 'min', 'letterbox'],
                    default='stretch', help='Resize strategy. Default: stretch.')
parser.add_argument('--bg', type=str, default='#000000',
                    help="Background color for 'letterbox' (e.g. '#000000' or '255,255,255').")

# Analizar los argumentos
args = parser.parse_args()

# Obtener la ruta de la carpeta, ancho, alto deseado y la opción de eliminar
folder_path = args.path
new_width = args.width
new_height = args.height
new_size = (new_width, new_height)
delete_original = args.delete
fit_mode = args.fit
bg_color_arg = args.bg

# Crear la carpeta 'resized' si no existe
resized_folder_path = os.path.join(folder_path, 'resized')
if not os.path.exists(resized_folder_path):
    os.makedirs(resized_folder_path)

def parse_bg_color(bg: str):
    """Acepta '#RRGGBB' o 'R,G,B' (0-255)."""
    bg = bg.strip()
    if bg.startswith('#') and len(bg) == 7:
        r = int(bg[1:3], 16); g = int(bg[3:5], 16); b = int(bg[5:7], 16)
        return (r, g, b)
    if ',' in bg:
        parts = [int(p) for p in bg.split(',')]
        if len(parts) == 3 and all(0 <= v <= 255 for v in parts):
            return tuple(parts)
    raise ValueError("Color inválido para --bg. Usa '#RRGGBB' o 'R,G,B'.")

# Función para redimensionar una sola imagen respetando el modo elegido
def resize_one(img: Image.Image, target_size: tuple[int, int], mode: str, bg_color=(0, 0, 0)) -> Image.Image:
    # Respetar orientación EXIF si existe
    img = ImageOps.exif_transpose(img)

    if mode == 'stretch':
        return img.resize(target_size, Image.Resampling.LANCZOS)

    if mode == 'max':
        # Encaja dentro de target_size manteniendo proporción
        out = img.copy()
        out.thumbnail(target_size, Image.Resampling.LANCZOS)
        return out

    if mode == 'min':
        # Cubre target_size con recorte centrado
        return ImageOps.fit(img, target_size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))

    if mode == 'letterbox':
        # Encaja y rellena con color hasta target_size
        temp = img.copy()
        temp.thumbnail(target_size, Image.Resampling.LANCZOS)

        # Elegir modo del lienzo
        canvas = Image.new('RGB', target_size, bg_color)
        x = (target_size[0] - temp.width) // 2
        y = (target_size[1] - temp.height) // 2

        if temp.mode in ('RGBA', 'LA'):
            canvas.paste(temp.convert('RGBA'), (x, y), temp.convert('RGBA'))
        else:
            # Convertir a RGB si va a guardarse como JPEG luego
            if temp.mode not in ('RGB', 'L'):
                temp = temp.convert('RGB')
            canvas.paste(temp, (x, y))
        return canvas

    raise ValueError(f"Modo desconocido: {mode}")

# Función para redimensionar imágenes
def resize_images_in_folder(folder_path, new_size, delete_original):
    if fit_mode == 'letterbox':
        bg_color = parse_bg_color(bg_color_arg)
    else:
        bg_color = (0, 0, 0)

    # Recorrer todos los archivos en la carpeta
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Construir la ruta completa al archivo original
            original_file_path = os.path.join(folder_path, filename)
            # Construir la ruta completa al archivo redimensionado
            resized_file_path = os.path.join(resized_folder_path, filename)

            try:
                # Abrir la imagen
                with Image.open(original_file_path) as img:
                    # Redimensionar según el modo
                    resized_img = resize_one(img, new_size, fit_mode, bg_color=bg_color)

                    # Si el destino es JPG/JPEG y la imagen tiene alfa, convertir a RGB
                    ext = os.path.splitext(resized_file_path)[1].lower()
                    if ext in ('.jpg', '.jpeg') and resized_img.mode in ('RGBA', 'LA', 'P'):
                        resized_img = resized_img.convert('RGB')

                    # Guardar la imagen redimensionada
                    resized_img.save(resized_file_path)

                    print(f"Imagen '{filename}' ({fit_mode}) -> {new_size} píxeles. Guardada en '{resized_folder_path}'.")

                # Borrar la imagen original si se especificó la opción
                if delete_original == 1:
                    os.remove(original_file_path)
                    print(f"Imagen original '{filename}' eliminada.")

            except IOError as e:
                print(f"No se pudo procesar la imagen '{filename}'. Error: {e}")
            except Exception as e:
                print(f"Error general con '{filename}': {e}")

# Ejecutar la función de redimensionamiento
resize_images_in_folder(folder_path, new_size, delete_original)

print("Proceso de redimensionamiento completado.")
