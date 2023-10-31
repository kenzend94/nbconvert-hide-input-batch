import os
import subprocess


# Check if nbconvert is installed, if not, install it
def install_nbconvert():
    answer = input("jupyter nbconvert is not installed. Do you want to install it now? (yes/no) ").strip().lower()
    if answer == "yes":
        try:
            # Run pip install nbconvert
            subprocess.run(["pip", "install", "nbconvert"], check=True)
            print("jupyter nbconvert installed successfully!")
            return True
        # If pip install nbconvert failed, subprocess.CalledProcessError will be raised
        except subprocess.CalledProcessError:
            print("Error installing jupyter nbconvert.")
            return False
    # If user does not want to install nbconvert, return False
    else:
        return False


# Check if nbconvert is installed
def is_nbconvert_installed():
    try:
        # Run nbconvert --version
        subprocess.run(["jupyter", "nbconvert", "--version"], check=True, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
        return True
    # If nbconvert is not installed, subprocess.CalledProcessError will be raised
    except subprocess.CalledProcessError:
        return False


def convert_notebooks_to_html_batch(root_dir="."):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".ipynb"):
                full_path = os.path.join(root, file)
                print(f"Converting: {full_path}")

                # Convert using nbconvert
                cmd = [
                    "jupyter",
                    "nbconvert",
                    "--to", "html",
                    "--TemplateExporter.exclude_input=True",
                    full_path
                ]

                subprocess.run(cmd)


if __name__ == "__main__":
    if not is_nbconvert_installed():
        if not install_nbconvert():
            print("Exiting script as jupyter nbconvert is not available.")
            exit()

    convert_notebooks_to_html_batch()
