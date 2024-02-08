from PIL import Image
import os

def resize_images_in_folder(folder_path):
    # Definir el tamaño deseado
    new_size = (320, 240)

    # Recorrer todos los archivos en la carpeta
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Construir la ruta completa al archivo
            file_path = os.path.join(folder_path, filename)

            try:
                # Abrir la imagen
                with Image.open(file_path) as img:
                    # Redimensionar la imagen
                    resized_img = img.resize(new_size, Image.ANTIALIAS)

                    # Guardar la imagen redimensionada
                    resized_img.save(file_path)

                    print(f"Imagen '{filename}' redimensionada a {new_size} píxeles.")
            except IOError:
                print(f"No se pudo procesar la imagen '{filename}'.")

# Ruta a la carpeta que contiene las imágenes
folder_path = 'path'
resize_images_in_folder(folder_path)