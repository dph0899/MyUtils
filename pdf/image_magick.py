"""Work with ImageMagick."""
import os
import subprocess


def convert_pdf_to_pngs(pdf_file_path: str, pngs_folder_path: str, temp_folder_path: str):
    """Convert a PDF file to PNGs using ImageMagick."""
    env = os.environ.copy()
    env['MAGICK_TEMPORARY_PATH'] = temp_folder_path
    try:
        subprocess.run(
            [
                "convert", "-density", "300", pdf_file_path,
                "-quality", "100",
                os.path.join(pngs_folder_path, "output-%03d.png")
            ],
            check=True,
            env=env
        )
    except subprocess.CalledProcessError as err_msg:
        print('Error:', err_msg.stderr)

def create_pdf_from_pngs(pngs_folder_path: str, output_pdf_path: str):
    """Create a PDF file from the PNG files using ImageMagick's convert command."""
    try:
        subprocess.run(
            [
                "convert", os.path.join(pngs_folder_path, "*.png"), output_pdf_path
            ],
            check=True
        )
        print("PDF file created successfully.")
    except subprocess.CalledProcessError as err:
        print('Error:', err.stderr)
