import os
import subprocess


# TODO: Scan directories and ask user any directory they want to ignore
def install_nbconvert():
    # Check if pip is installed
    try:
        subprocess.run(["pip", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("pip is not installed. Cannot proceed with installing nbconvert.")
        return False

    answer = input("jupyter nbconvert is not installed. Do you want to install it now? (yes/no) ").strip().lower()
    if answer == "yes":
        try:
            subprocess.run(["pip", "install", "nbconvert"], check=True)
            print("jupyter nbconvert installed successfully!")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Error installing jupyter nbconvert.")
            return False
    else:
        return False


def is_nbconvert_installed():
    try:
        subprocess.run(["jupyter", "nbconvert", "--version"], check=True, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def convert_notebooks_to_html_batch(directory, excluded_subfolders):
    # Initialize overwrite_all to None
    overwrite_all = None

    for root, dirs, files in os.walk(directory):
        # Remove the excluded subfolders from the list of directories to search
        dirs[:] = [d for d in dirs if d not in excluded_subfolders]
        for file in files:
            # Check if the file is a notebook
            if file.endswith(".ipynb"):
                full_path = os.path.join(root, file)
                output_file = os.path.join(root, file.replace(".ipynb", ".html"))

                # If we haven't already set overwrite_all, check if the output file already exists
                if overwrite_all is None and os.path.exists(output_file):
                    answer = input(
                        f"Output file {output_file} already exists. Do you want to overwrite it? (yes/no/all): "
                    ).strip().lower()
                    if answer == "all":
                        overwrite_all = True
                    elif answer == "yes":
                        overwrite_all = False
                    else:
                        print(f"Skipping {full_path}.")
                        continue

                # If overwrite_all is False, we continue to the next file without overwriting
                elif overwrite_all is False and os.path.exists(output_file):
                    print(f"Skipping {full_path}.")
                    continue

                print(f"Converting: {full_path}")
                cmd = [
                    "jupyter",
                    "nbconvert",
                    "--to", "html",
                    "--TemplateExporter.exclude_input=True",
                    full_path
                ]

                try:
                    subprocess.run(cmd, check=True)
                except (subprocess.CalledProcessError, FileNotFoundError):
                    print(f"Error converting {full_path}. Moving on to next notebook.")


def get_directory_from_user():
    # Get directory path from user
    dir_input = input("Enter the directory path (or press Enter to use the current directory): ").strip()

    # If the user did not enter anything, use the current directory
    if not dir_input:
        return "."

    # Check if the path is valid
    if not os.path.exists(dir_input) or not os.path.isdir(dir_input):
        print(f"Error: The path '{dir_input}' is not a valid directory.")
        return None

    return dir_input


def get_subfolders_to_exclude(directory):
    print("Subfolders in '{}':".format(directory))

    # Get the list of subfolders
    subfolders = [f.name for f in os.scandir(directory) if f.is_dir()]

    # Print the list of subfolders
    for idx, folder in enumerate(subfolders):
        print("[{}] {}".format(idx, folder))

    while True:
        indices_input = input("Enter the indices of subfolders to exclude, separated by commas (e.g., '0,3'): ").strip()
        if not indices_input:
            print("No subfolders will be excluded.")
            return []  # No input means no exclusions

        # Split the input by commas and strip whitespace from each part
        parts = indices_input.split(',')
        if all(part.strip().isdigit() for part in parts):  # Check if all parts are digits after stripping whitespace
            try:
                indices = [int(part.strip()) for part in parts]
                # Check if all indices are within the valid range
                if all(0 <= idx < len(subfolders) for idx in indices):
                    excluded_subfolders = [subfolders[idx] for idx in indices]
                    # Print the confirmation message
                    print("You have chosen to exclude the following subfolders:")
                    for folder in excluded_subfolders:
                        print(folder)
                    return excluded_subfolders
                else:
                    print("Invalid indices. Some indices are out of range. Please enter valid indices separated by commas.")
            except ValueError:  # Just as an extra precaution
                print("Invalid input. Please enter numeric indices separated by commas.")
        else:
            print("Invalid input. Make sure to use commas to separate indices and only enter numbers.")


# Main script
if __name__ == "__main__":
    if not is_nbconvert_installed():
        if not install_nbconvert():
            print("Exiting script as jupyter nbconvert is not available.")
            exit()

    directory = get_directory_from_user()
    if directory:
        excluded_subfolders = get_subfolders_to_exclude(directory)  # Get the list of subfolders to exclude
        convert_notebooks_to_html_batch(directory, excluded_subfolders)
    else:
        print("Operation aborted due to invalid directory.")