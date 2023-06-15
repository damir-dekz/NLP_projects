import os
import shutil
import zipfile
import pandas as pd
import re

# DO NOT CHANGE
data_path = "./data/bcc"
zip_path = './data/bbc-fulltext.zip'


# DO NOT CHANGE
def prepare_files():
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(data_path)
    # Define the file extension to look for
    file_extension = ".txt"
    # Initialize an empty list to store the file paths
    file_paths = []
    # Use os.walk to traverse through the directory and subdirectories
    for dirpath, dirnames, filenames in os.walk(data_path):
        for filename in filenames:
            if filename.endswith(file_extension):
                # Construct the full file path
                file_path = os.path.join(dirpath, filename)
                # Append the file path to the list
                file_paths.append(file_path)
    return file_paths


def find_proper_names(text):
    result_name = re \
        .findall(
        '(?:like|firms)?\s(?:[A-Z]\w+|the)(?:\s[A-Z]\w+(?:\'s))+'
        '|(?:like|firms)?\s(?:[A-Z]\w+)(?:\s[A-Z]\w+)+'
        '|(?:[A-Z]+){2,4}'  # ex: AA,AAA,AAAA
        '|Mr [A-Z]\w+'
        '|(?:[A-Z]\w+ )*(?:[A-Z][a-z]+)*\s(?:[A-Z]\')*[A-Z][a-z]+\'s' # ex: Alan Bennett's, Amazon's, Van Doren Stern's
        '|[A-Z]\'[A-Z]\w+'
        '|(?:legend|leader)\s\w+(?:\s\w+)?'
        '|\s[0-9][0-9](?:\s[A-Z][a-z]+){2}'
        '|(?:[A-Z][a-z]+)+\sand\s(?:[A-Z][a-z]+)+'
        '|(?:[A-Z]|\$[0-9]+)\.(?:[A-Z]\.|[0-9][a-z]+)'
        '|\s(?:in|on)\s[A-Z]\w+'
        '|[A-z]\w+\.com'
        '|(?:[Ff]or|at)\s[A-Z]\w+'
        '|the(?:\s[A-Z]\w+){2,}'
        , text)

    # result_name2 = re.findall('(?:[A-Z][a-z]+)*\s(?:[A-Z]\')*[A-Z][a-z]+\'s', text)
    result_name = [name
                   .replace("legend ", "")
                   .replace("and ", "")
                   .replace("And ", "")
                   .replace(" in ", "")
                   .replace(" on ", "")
                   .replace("$", "")
                   .replace("leader ", "")
                   .replace("like ", "")
                   .replace("for ", "")
                   .replace("at ", "")
                   # .replace('""', "")
                   for name in result_name]
    result_name = [re
                   .sub(r'((?:[A-Z][a-z]+)+)\sand\s((?:[A-Z][a-z]+)+)', r'\1\r\2', name)
                   for name in
                   result_name]
    result_name = [re
                   .sub(r'((?:[A-Z]\w+an))\s((?:[A-Z]\w+)(?:\s[A-Z]\w+)+)', r'\1\r\2', name)
                   for name in
                   result_name]
    # result_name2 = [re
    #                 .sub(r'([A-Z]\w+)\'s', r'\1', name)
    #                 for name in
    #                 result_name2]
    # result_name3 = result_name + result_name2
    return result_name


# Function to process a single file
def process_files(files):
    res = []
    unique_names = []
    for file_path in files:
        with open(file_path, "r", encoding='unicode_escape') as text_file:
            # Read the text from the file
            text = text_file.read()
            # TODO process test and extract names, write code below
            proper_names = find_proper_names(text)
            if proper_names:
                res.append(proper_names)
                for lists in res:
                    for items in lists:
                        unique_names.append((items.strip()))
    unique_names = list(set(unique_names))
    for i in range(len(unique_names)):
        z = re.match('(?:the )?(?:([A-Z]\w+)\'s)', unique_names[i])
        # z_the = re.match('(?:[T]he )?((?:[A-Z]\w+))', unique_names[i])
        if z:
            unique_names[i] = z.groups()[0]
        # elif z_the:
        #     unique_names[i] = z_the.groups()[0]
    # end code
    return unique_names


# DO NOT CHANGE
def safe_names_to_csv(unique_names):
    df = pd.DataFrame()
    df["names"] = unique_names
    df = df.drop_duplicates()
    df = df.sort_values(by="names")
    df.to_csv("./result/B_01.csv", index=False, header=False)


# DO NOT CHANGE
def main():
    files = prepare_files()
    unique_names = process_files(files)
    safe_names_to_csv(unique_names)
    shutil.rmtree(data_path, ignore_errors=False, onerror=None)


if __name__ == "__main__":
    main()
