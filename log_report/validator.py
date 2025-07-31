import os

def validate_file_paths(file_paths):
    for path in file_paths:
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Файл не найден: {path}")
