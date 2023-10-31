# `nbconvert-hide-input-batch-convert-html`

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

git clone https://github.com/kenzend94/nbconvert-hide-input-batch-convert-html.git

2. Navigate to the directory containing the Python script:

cd nbconvert-hide-input-batch-convert-html

3. Run the script:

python nbconvert-hide-input-batch-convert-html.py

4. Follow the on-screen instructions.

The script will automatically search for `.ipynb` files in the current directory and all subdirectories, converting them to HTML format without the input code.

## Benefits

The main advantage of this batch process is to save users significant time when they need to convert multiple notebooks, especially when they are scattered across different subdirectories. Additionally, by excluding the input code, the generated HTMLs offer a cleaner view focused on outputs, results, or visualizations, ensuring the content's privacy.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [Issues page](https://github.com/kenzend94/nbconvert-hide-input-batch-convert-html/issues).


