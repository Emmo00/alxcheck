import os


def check_file_present(file_path):
    if not os.path.exists(file_path):
        return False
    return True


def check_file_not_empty(file_path):
    if os.stat(file_path).st_size == 0:
        return False
    return True


def check_file_ends_with_new_lines(file_path):
    if not check_file_not_empty(file_path):
        return False
    with open(file_path, "r") as f:
        last_line = f.readlines()[-1]
        if last_line != "\n":
            return False
        return True
