import os
import shutil

import pandas as pd
import zipfile
from typing import List, Tuple
import re

root_dir = "."
data_path = f"{root_dir}/data/spamlord"
zip_path = f'{root_dir}/data/spamlord.zip'


# TODO: Implement your approach here!
def find_phone_numbers(full_text: str) -> List[str]:
    result_phone = re \
        .findall('[()]?[\d]{3}[\s()-]+[\d]{3}[-\s]+[\d]{4}', full_text)

    result_phone = [re
                    .sub(r'[()]?([\d]{3})[\s()-]+([\d]{3})[-\s]+([\d]{4})', r'\1-\2-\3', phone)
                    for phone in
                    result_phone]
    return result_phone


# TODO: Implement your approach here!
def find_emails(full_text: str) -> List[str]:
    result_email = re \
        .findall(
        "(?:\w|\w-)+(?:(?:\.\w+)*(?:@| @ )|&#x40;)(?:\w|[\-]?\w-)+\.(?:\w|[\-]?\w[\-]?)+(?:\.\w+|)*"
        "|[a-z]+\s(?:at|where)\s[a-z]+\s(?:dot|dom)\s[a-z]+(?:\sdot\sedu)?"
        "|[a-z]+\sat\s[a-z]+(?:[;\s]+|\.|\s)[a-z]+(?:[;\s]|\.|\s)+(?:edu|com)"
        , full_text.lower())

    result_email = [re.sub(r'([a-z]+)\sat\s([a-z]+)\s([a-z]+)\sedu', r'\1@\2.\3.edu', email) for email in
                    result_email]

    result_email = [email
                    .replace('&#x40;', '@')
                    .replace(' at ', '@')
                    .replace(' where ', '@')
                    .replace(' dt ', '.')
                    .replace(' dot ', '.')
                    .replace('.dot', '')
                    .replace(' dom ', '.')
                    .replace(';', '.')
                    .replace(' ', '')
                    .replace('-', '')
                    for email in result_email]
    return result_email


# DO NOT CHANGE
def prepare_files():
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(data_path)
    # Define the file extension to look for
    file_extension = ".html"
    # Initialize an empty list to store the file paths
    file_paths = []
    # Use os.walk to traverse through the directory and subdirectories
    for dirpath, dirnames, filenames in os.walk(data_path):
        for filename in filenames:
            if filename.endswith(file_extension):
                # Append the file path to the list
                file_paths.append((dirpath, filename))
    return file_paths


# DO NOT CHANGE
# Function to process a single file
def process_files(files) -> List[Tuple]:
    res = []
    for data_directory, filename in files:
        filename_no_ext, ext = filename.split('.')
        absolute_file_path = os.path.join(data_directory, filename)
        with open(absolute_file_path, 'r', encoding='ISO-8859-1') as file:
            # Read the full text
            full_text = file.read()

            # Call find_emails
            emails = [(filename_no_ext, 'e', e) for e in find_emails(full_text)]

            # Call find_phone_numbers
            phone_numbers = [(filename_no_ext, 'p', p) for p in find_phone_numbers(full_text)]

            # Add the newly extracted emails and phone numbers to our list
            res += emails + phone_numbers
    return res


# DO NOT CHANGE
def safe_results_to_csv(results: List[Tuple]):
    df = pd.DataFrame(results, columns=['file', 'type', 'data'])
    df = df.drop_duplicates()
    df = df.sort_values(by="file")
    df.to_csv(f'{root_dir}/result/C_01.csv', index=False, header=False, sep="|")


# DO NOT CHANGE
def main():
    files = prepare_files()
    results = process_files(files)
    safe_results_to_csv(results)
    shutil.rmtree(data_path, ignore_errors=False, onerror=None)
    print("Output is saved")


if __name__ == "__main__":
    main()
