import os
from utils.error_logging import (
    print_no_ending_new_line,
    print_no_readme_file,
    print_readme_file_empty,
)


def check_readme_present():
    if not os.path.exists("README.md"):
        print_no_readme_file()
        return False
    return True


def check_readme_not_empty():
    with open("README.md", "r") as f:
        if os.stat("README.md").st_size == 0:
            print_readme_file_empty()
            return False
        return True


def check_file_ends_with_new_lines(file_path):
    with open(file_path, "rb") as f:
        f.seek(-2, os.SEEK_END)
        if f.read() != b"\n":
            print_no_ending_new_line(file_path)
            return False
        return True
