# `private-notebook-converter`

Convert Jupyter notebooks in the current directory and its subdirectories to HTML format without displaying the input code. This batch process is designed to save time and ensure the privacy of the notebook's input code.

## Features

- **Batch Processing**: Convert all `.ipynb` files in a directory (and its subdirectories) in one go.
- **Privacy First**: Outputs HTML without showing the input code of the Jupyter notebook.
- **Dependency Check**: Before the conversion process, the script checks if `jupyter nbconvert` is installed and prompts the user for installation if required.

## Requirements

- Python
- Jupyter (specifically `jupyter nbconvert`)

## Usage

1. Clone the repository:
