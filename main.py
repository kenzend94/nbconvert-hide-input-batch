import os
import subprocess

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
    convert_notebooks_to_html_batch()
