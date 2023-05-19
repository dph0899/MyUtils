"""Work with folder"""
import os
import shutil


def delete_folder_content(temp_folder_path: str):
    """Delete the content of a specified folder."""
    try:
        # This will remove the directory itself and all its children
        shutil.rmtree(temp_folder_path)
        os.makedirs(temp_folder_path)  # This will re-create the directory
        print("Temporary folder content deleted successfully.")
    except OSError as err:
        print(f"Error deleting temporary folder content: {err}")
