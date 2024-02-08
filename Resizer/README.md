# Resizer

Have you ever been in a situation where you have a lot of images and you need to resize them, like a bunch of them. In those cases, using a program like Photoshop or Gimp, becomes time consuming. For me, I needed to resize 190 images the same morning I have to program, load, build and solder a project. So I asked ChatGPT to help me write a python script to resize all those images in a few seconds.

## Table of Contents
1. [Scope](#scope)
2. [Requirements](#requirements)
   - [Python Installation](#python-installation)
   - [Library Installation](#library-installation)
3. [Instructions](#instructions)
4. [Contributing](#contributing)
5. [Troubleshooting/FAQ](#troubleshootingfaq)
6. [Greetings](#greetings)
7. [Credits](#credits)
8. [License](#license)

## Scope

The `resizer.py` script is designed to easily resize images from various formats (such as PNG, GIF, BMP, TIFF, JFIF, and WEBP) to a desired resolution. This utility is especially useful when you have to do it fast or you don't want to spend a few days resizing them one by one. It's a versatile tool that can be used across multiple operating systems including Windows, Linux, and Mac, thanks to the cross-platform nature of Python and its libraries.

This program does not take in account original aspect ratio against final aspect ratio. For better results use it only when all images are the same aspect ratio and when the aspect ratio of the final resolution is the same as the original aspect ratio.

## Requirements

To run this script, you need to have Python installed, along with the Pillow library for image processing.

### Python Installation

- **Windows:**
  1. Download Python from [python.org](https://www.python.org/downloads/windows/).
  2. Run the installer and follow the prompts. Make sure to check the box that says "Add Python to PATH" during installation.

- **Linux:**
  - Python usually comes pre-installed on Linux. To check if it's installed and to install it if it isn't, use the following commands:
    ```
    python --version
    sudo apt-get install python3
    ```

- **Mac:**
  - For Mac, Python can be installed using Homebrew:
    ```
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    brew install python
    ```

### Library Installation

After installing Python, install the Pillow library using pip:

```
pip install Pillow
```

# Instructions

To use the script, navigate to the directory where the script is located and run the following command in the terminal or command prompt:

```
python resizer.py /path/to/your/images width height
 
```

You can also specify if you want to delete the original images after conversion with the -d option (1 to delete, 0 to keep):

```
python resizer.py /path/to/your/images width height -d 1
```
## Contributing

Contributions to `resizer.py` are welcome! Whether it's reporting a bug, discussing improvements, or submitting pull requests, all contributions are appreciated. Please feel free to contribute as per the standard GitHub workflow.

## Troubleshooting/FAQ

No questions yet!

# Greetings

Now you have the power to resized your images with ease. Enjoy your newly resized images and the seamless compatibility they bring!

## Credits

Author: Hugo Escalpelo

In collaboration with OpenAI's ChatGPT, this script was brought to life, combining Hugo's vision and technical expertise with the language and coding assistance from ChatGPT. A true testament to the synergy between human creativity and AI capabilities.

## License

This project is licensed under the Creative Commons Attribution-NonCommercial (CC BY-NC) license. This allows for the redistribution, modification, and use of this work non-commercially as long as appropriate credit is given to the author, Hugo Escalpelo, and any derivative works carry the same license.

For more information, see [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

```
This README provides a clear and detailed guide for users to understand and use your JPG converter script. It includes installation instructions for Python and Pillow, as well as usage instructions for the script. The motivational closing phrase adds a friendly touch to the document.
```