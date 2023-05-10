import os


# считаем количество файлов в папке
def count_files_in_folder(folder_path):
    files = os.listdir(folder_path)
    return len([f for f in files if os.path.isfile(os.path.join(folder_path, f))])


# проверям наличие слов из pattern в text
def find_match(text, pattern):
    return any([word.lower() in text.lower() for word in pattern])
