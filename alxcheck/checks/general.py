import os


def check_file_present(file_path):
    if not os.path.exists(file_path):
        return False
    return True


def check_file_not_empty(file_path):
    if not check_file_present(file_path):
        return False
    if os.stat(file_path).st_size == 0:
        return False
    return True


def check_file_ends_with_new_lines(file_path):
    if not check_file_not_empty(file_path):
        # skip empty __init__.py
        if file_path.endswith('__init__.py'):
            return True
        return False
    with open(file_path, "r") as f:
        return f.read()[-1] == "\n"
