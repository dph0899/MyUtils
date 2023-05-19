"""With a path to a folder containing pdfs downloaded from the internet,
process the pdfs and output cleaned pdfs"""
import os
import shutil

from common.folder import delete_folder_content
from pdf import image_magick, pdftk


def process_pdfs(pdfs_folder_path: str):
    """ Steps:
    1. Move pdfs into original_pdfs
        1.1 Create a folder named 'original_pdfs' inside 'pdfs_folder_path'
        1.2 Move all pdfs into 'original_pdfs'
    2. Create dump files of original pdfs
        2.1. Create a folder named 'original_dump_files' inside 'pdfs_folder_path'
        2.2. Run pdftk dump_data on files in 'original_pdfs' and output to 'original_dump_files'
    3. Prepare outline data for pdfs
        3.1. Create a folder named 'outline_files' inside 'pdfs_folder_path'
        3.2. Create outline data files
    4. Create clean pdfs
        4.1. Create a folder named 'clean_pdfs' inside 'pdfs_folder_path'
        4.2. Create clean pdfs
    5. Create dump files of clean pdfs
        5.1. Create a folder named 'clean_dump_files' inside 'pdfs_folder_path'
        5.2. Run pdftk dump_data on files in 'clean_pdfs' and output to 'clean_dump_files'
    6. Add outline data to dump files of clean pdfs
    7. Update outline data for clean pdfs
        7.1. Create a folder named 'clean_outline_pdfs' inside 'pdfs_folder_path'
        7.2. Run pdftk update_info on files in 'clean_pdfs' and output to 'clean_outline_pdfs'
    """
    # Steps 1: Move pdfs into original_pdfs
    # 1.1: Create a folder named 'original_pdfs' inside 'pdfs_folder_path'
    original_pdfs_folder_path = os.path.join(pdfs_folder_path, "original_pdfs")
    os.makedirs(original_pdfs_folder_path, exist_ok=True)

    # 1.2: Move all pdfs into 'original_pdfs'
    for file_name in os.listdir(pdfs_folder_path):
        if file_name.endswith(".pdf"):
            pdf_file_path = os.path.join(pdfs_folder_path, file_name)
            shutil.move(pdf_file_path, original_pdfs_folder_path)

    # Step 2: Create dump_files for original pdfs
    # 2.1: Create a folder named 'original_dump_files' inside 'pdfs_folder_path'
    original_dump_files_folder_path = os.path.join(
        pdfs_folder_path, "original_dump_files")
    os.makedirs(original_dump_files_folder_path, exist_ok=True)

    # 2.2: Run pdftk dump_data on files in 'original_pdfs' and output to 'original_dump_files'
    for file_name in os.listdir(original_pdfs_folder_path):
        if file_name.endswith(".pdf"):
            pdf_file_path = os.path.join(original_pdfs_folder_path, file_name)
            dump_data_file_path = os.path.join(
                original_dump_files_folder_path, file_name.replace(".pdf", ".txt"))
            pdftk.dump_data(pdf_file_path, dump_data_file_path)

    # Step 3: Prepare outline data for pdfs
    # 3.1: Create a folder named 'outline_files' inside 'pdfs_folder_path'
    outline_files_folder_path = os.path.join(pdfs_folder_path, "outline_files")
    os.makedirs(outline_files_folder_path, exist_ok=True)

    # 3.2: Create outline data files
    for file_name in os.listdir(original_dump_files_folder_path):
        if file_name.endswith(".txt"):
            dump_data_file_path = os.path.join(
                original_dump_files_folder_path, file_name)
            outline_data_file_path = os.path.join(
                outline_files_folder_path, file_name)
            pdftk.extract_outline_data(
                dump_data_file_path, outline_data_file_path)

    # Step 4: Create clean pdfs
    # 4.1: Create a folder named 'clean_pdfs' inside 'pdfs_folder_path'
    clean_pdfs_folder_path = os.path.join(pdfs_folder_path, "clean_pdfs")
    os.makedirs(clean_pdfs_folder_path, exist_ok=True)

    # 4.2: Create clean pdfs
    pngs_folder_path = os.path.join(pdfs_folder_path, "pngs")
    os.makedirs(pngs_folder_path, exist_ok=True)
    temp_folder_path = '/data/tmp'
    for file_name in os.listdir(original_pdfs_folder_path):
        if file_name.endswith(".pdf"):
            pdf_file_path = os.path.join(original_pdfs_folder_path, file_name)
            output_pdf_file_path = os.path.join(
                clean_pdfs_folder_path, file_name)
            image_magick.convert_pdf_to_pngs(
                pdf_file_path, pngs_folder_path, temp_folder_path)
            image_magick.create_pdf_from_pngs(
                pngs_folder_path, output_pdf_file_path)
            delete_folder_content(pngs_folder_path)
            delete_folder_content(temp_folder_path)

    # Step 5: Create dump files for clean pdfs
    # 5.1: Create a folder named 'clean_dump_files' inside 'pdfs_folder_path'
    clean_dump_files_folder_path = os.path.join(
        pdfs_folder_path, "clean_dump_files")
    os.makedirs(clean_dump_files_folder_path, exist_ok=True)

    # 5.2: Run pdftk dump_data on files in 'clean_pdfs' and output to 'clean_dump_files'
    for file_name in os.listdir(clean_pdfs_folder_path):
        if file_name.endswith(".pdf"):
            pdf_file_path = os.path.join(clean_pdfs_folder_path, file_name)
            dump_data_file_path = os.path.join(
                clean_dump_files_folder_path, file_name.replace(".pdf", ".txt"))
            pdftk.dump_data(pdf_file_path, dump_data_file_path)
            # Step 6: Add outline data to dump files of clean pdfs
            pdftk.update_outline_data(dump_data_file_path, os.path.join(
                outline_files_folder_path, file_name.replace(".pdf", ".txt")))

    # Step 7: Update outline data for clean pdfs
    # 7.1: Create a folder named 'clean_outline_pdfs' inside 'pdfs_folder_path'
    clean_outline_pdfs_folder_path = os.path.join(
        pdfs_folder_path, "clean_outline_pdfs")
    os.makedirs(clean_outline_pdfs_folder_path, exist_ok=True)

    # 7.2: Run pdftk update_info on files in 'clean_pdfs' and output to 'clean_outline_pdfs'
    for file_name in os.listdir(clean_pdfs_folder_path):
        if file_name.endswith(".pdf"):
            pdf_file_path = os.path.join(clean_pdfs_folder_path, file_name)
            dump_data_file_path = os.path.join(
                clean_dump_files_folder_path, file_name.replace(".pdf", ".txt"))
            pdftk.run_pdftk_update_info_utf8(pdf_file_path, dump_data_file_path, os.path.join(
                clean_outline_pdfs_folder_path, file_name))

    print("PDF processing completed.")
