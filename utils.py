import os


def count_files_in_folder(folder_path):
    files = os.listdir(folder_path)
    return len([f for f in files if os.path.isfile(os.path.join(folder_path, f))])


def find_match(text, pattern):
    return any([word in text.lower() for word in pattern])
