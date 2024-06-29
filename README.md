# PDF to PNG Converter

Convert your PDF files to PNG images easily with this automated Python script in bulk. Each page of the PDF is rendered as a separate PNG image, suitable for various applications where image formats are preferred over document formats.

## Features

- **Batch Conversion**: Converts all PDF files located in the same directory as the script.
- **Multi-Page Support**: Handles the conversion of multiple pages within PDF documents.
- **Organized Output**: Saves the converted PNG images in a dedicated `output` folder, named according to the source PDF and page number.

## Requirements

- Python 3.x
- `pdf2image`
- File system access for reading PDFs and writing PNGs

## Installation of dependencies

Ensure Python is installed on your system, and then install the `pdf2image` library using pip:

```bash
pip install pdf2image
```

## Usage

-  Place the `pdf_to_png.py` script in the same directory as the PDF files you wish to convert.
-  Run the script using the command `python pdf_to_png.py`.
-  The PNG images will be saved in the `output` folder within the same directory.


