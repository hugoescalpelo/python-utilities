import os
import argparse
from PIL import Image

# Setting up the argument parser
parser = argparse.ArgumentParser(description='Convert images to JPG format and optionally delete the originals. Script by Hugo Escalpelo. Visit hugoescalpelo.com and check out more utilities at https://github.com/hugoescalpelo/python-utilities.')
parser.add_argument('path', type=str, help='Path to the folder with images.')
parser.add_argument('-d', '--delete', type=int, choices=[0, 1], default=0, help='Delete original files after conversion (1 for yes, 0 for no).')

# Parsing arguments
args = parser.parse_args()

# Folder path and delete option
usb_path = args.path
delete_original = args.delete

# Image formats to be converted
formats_to_convert = ('.png', '.gif', '.bmp', '.tiff', '.jfif', '.webp')

# Function to convert images
def convert_to_jpg(path, filename):
    # Ignore files that are already JPG
    if filename.lower().endswith('.jpg'):
        return

    if filename.lower().endswith(formats_to_convert):
        # Full path of the original file
        original_file = os.path.join(path, filename)
        
        # Path of the converted file
        converted_file = os.path.join(path, os.path.splitext(filename)[0] + '.jpg')
        
        # Open and convert the image
        try:
            with Image.open(original_file) as img:
                img.convert('RGB').save(converted_file, 'JPEG')
            print(f'Converted: {original_file} to {converted_file}')

            # Delete the original file if delete_original is 1
            if delete_original == 1:
                os.remove(original_file)
                print(f'Deleted: {original_file}')

        except Exception as e:
            print(f'Error converting {original_file}: {e}')

# Traverse all files in the folder
for root, dirs, files in os.walk(usb_path):
    for file in files:
        convert_to_jpg(root, file)

print("Conversion completed.")
