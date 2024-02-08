import os
import argparse
from PIL import Image

# Configuración del analizador de argumentos
parser = argparse.ArgumentParser(description="Resize images to a specified resolution and save them in a 'resized' subfolder. Optionally, delete the original images.")
parser.add_argument('path', type=str, help='Path to the folder with images.')
parser.add_argument('width', type=int, help='Width of the resized images.')
parser.add_argument('height', type=int, help='Height of the resized images.')
parser.add_argument('-d', '--delete', type=int, choices=[0, 1], default=0, help='Delete original files after resizing (1 for yes, 0 for no).')

# Analizar los argumentos
args = parser.parse_args()

# Obtener la ruta de la carpeta, ancho, alto deseado y la opción de eliminar
folder_path = args.path
new_width = args.width
new_height = args.height
new_size = (new_width, new_height)
delete_original = args.delete

# Crear la carpeta 'resized' si no existe
resized_folder_path = os.path.join(folder_path, 'resized')
if not os.path.exists(resized_folder_path):
    os.makedirs(resized_folder_path)

# Función para redimensionar imágenes
def resize_images_in_folder(folder_path, new_size, delete_original):
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
                    # Redimensionar la imagen
                    resized_img = img.resize(new_size, Image.ANTIALIAS)

                    # Guardar la imagen redimensionada
                    resized_img.save(resized_file_path)

                    print(f"Imagen '{filename}' redimensionada a {new_size} píxeles y guardada en '{resized_folder_path}'.")

                # Borrar la imagen original si se especificó la opción
                if delete_original == 1:
                    os.remove(original_file_path)
                    print(f"Imagen original '{filename}' eliminada.")

            except IOError as e:
                print(f"No se pudo procesar la imagen '{filename}'. Error: {e}")

# Ejecutar la función de redimensionamiento
resize_images_in_folder(folder_path, new_size, delete_original)

print("Proceso de redimensionamiento completado.")
