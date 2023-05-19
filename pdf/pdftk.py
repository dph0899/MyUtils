"""Work with pdftk."""
import os
import re
import subprocess


def dump_data(pdf_file_path: str, dump_data_file_path: str):
    """Dump data from a PDF file using pdftk."""
    try:
        subprocess.run(
            [
                "pdftk",
                pdf_file_path,
                "dump_data_utf8",
                "output",
                dump_data_file_path
            ],
            check=True
        )
    except subprocess.CalledProcessError as err_msg:
        print('Error:', err_msg.stderr)


def extract_outline_data(dump_data_file_path: str, outline_data_file_path: str):
    """Extract only outline data from a dump_data file to a text file."""

    with open(dump_data_file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    start_pattern = r"NumberOfPages: (\d+)"
    end_pattern = r"PageMediaBegin"
    start_match = re.search(start_pattern, file_content)
    end_match = re.search(end_pattern, file_content)
    if start_match and end_match:
        start_index = start_match.end()
        end_index = end_match.start()
        lines = file_content[start_index:end_index].strip().split('\n')
        with open(outline_data_file_path, 'w', encoding='utf-8') as output_file:
            for line in lines:
                output_file.write(line + '\n')


def update_outline_data(dump_data_file_path: str, outline_data_file_path: str):
    """Get content of outline_data_file_path and use it as outline data in dump_data_file_path."""

    # Read the outline data file
    with open(outline_data_file_path, 'r', encoding='utf-8') as outline_file:
        outline_content = outline_file.read()

    # Read the dump data file
    with open(dump_data_file_path, 'r', encoding='utf-8') as dump_file:
        dump_content = dump_file.readlines()

    # Find the index of the first PageMediaBegin line
    page_media_begin_index = dump_content.index("PageMediaBegin\n")

    # Insert the outline content right after the NumberOfPages line
    updated_content = dump_content[:page_media_begin_index]
    updated_content.append(outline_content)
    updated_content.extend(dump_content[page_media_begin_index:])

    # Write the updated content back to the dump data file
    with open(dump_data_file_path, 'w', encoding='utf-8') as updated_file:
        updated_file.writelines(updated_content)


def run_pdftk_update_info_utf8(pdf_file_path: str, info_file_path: str, output_file_path: str):
    """Use info_file_path as a info data file to update pdf_file_path's info data"""
    try:
        subprocess.run(["pdftk", pdf_file_path, "update_info_utf8",
                       info_file_path, "output", output_file_path], check=True)
    except subprocess.CalledProcessError as err_msg:
        print('Error:', err_msg.stderr)
