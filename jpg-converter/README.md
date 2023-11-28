# JPG Converter

Have you ever had a good time saving beautiful images only to find most of them are in WEBP? Well, this script will convert all non-JPG images into JPG, so you can be happy. In my case, I wanted to have them all in JPG so my Smart TV could slideshow them.

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

The `jpg-converter.py` script is designed to easily convert images from various formats (such as PNG, GIF, BMP, TIFF, JFIF, and WEBP) to JPG. This utility is especially useful for making images compatible with devices or software that primarily support JPG format. It's a versatile tool that can be used across multiple operating systems including Windows, Linux, and Mac, thanks to the cross-platform nature of Python and its libraries.

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
python jpg-converter.py /path/to/your/images
```

You can also specify if you want to delete the original images after conversion with the -d option (1 to delete, 0 to keep):

```
python jpg-converter.py /path/to/your/images -d 1
```
## Contributing

Contributions to `jpg-converter.py` are welcome! Whether it's reporting a bug, discussing improvements, or submitting pull requests, all contributions are appreciated. Please feel free to contribute as per the standard GitHub workflow.

## Troubleshooting/FAQ

No questions yet!

# Greetings

Now you have the power to convert your images with ease. Enjoy your newly converted JPG images and the seamless compatibility they bring!

## Credits

Author: Hugo Escalpelo

In collaboration with OpenAI's ChatGPT, this script was brought to life, combining Hugo's vision and technical expertise with the language and coding assistance from ChatGPT. A true testament to the synergy between human creativity and AI capabilities.

## License

This project is licensed under the Creative Commons Attribution-NonCommercial (CC BY-NC) license. This allows for the redistribution, modification, and use of this work non-commercially as long as appropriate credit is given to the author, Hugo Escalpelo, and any derivative works carry the same license.

For more information, see [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

```
This README provides a clear and detailed guide for users to understand and use your JPG converter script. It includes installation instructions for Python and Pillow, as well as usage instructions for the script. The motivational closing phrase adds a friendly touch to the document.
```