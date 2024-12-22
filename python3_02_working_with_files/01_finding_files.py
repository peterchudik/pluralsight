import os
import fnmatch
from pathlib import Path

def list_files(folder):
    for file in os.listdir(folder):
        print(file)

# list_files("./files")

def list_files_end_with(folder, file_type):
    for file in os.listdir(folder):
        if file.endswith(file_type):
            print(file)

# list_files_end_with("./files", "txt")


def list_files_start_with(folder, file_type):
    for file in os.listdir(folder):
        if file.startswith(file_type):
            print(file)

# list_files_start_with("./files", "01_test")


def match(folder, search_pattern):
    for file in os.listdir(folder):
        if fnmatch.fnmatch(file, search_pattern):
            print(file)

# match("./files", "*1*test*.csv")

def glob_match(folder, search_pattern):
    p = Path(folder)
    for file in p.glob(search_pattern):
        print(file)

glob_match("./files", "*1*test*.csv")
