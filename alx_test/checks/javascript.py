import os
import subprocess
from utils.error_logging import print_file_not_executable, print_no_shebang


def check_file_is_executable_and_javascript_shebang(file_path):
    flag = True
    if not os.access(file_path, os.X_OK):
        flag = False
        print_file_not_executable(file_path)
    with open(file_path, "r") as f:
        first_line = f.readline().strip()
        if first_line not in ("#!/usr/bin/node", "#!/usr/bin/env node"):
            flag = False
            print_no_shebang(file_path)
    return flag


def semistandard_check(file_path):
    result = subprocess.run(
        ["semistandard", file_path], stdout=subprocess.STDOUT, text=True
    )
    return result == 0


def check_no_var(file_path):
    with open(file_path, "r") as f:
        content = f.read()
        lines = content.split("\n")
        for line in lines:
            if line.strip().startswith("var "):
                return False
        return True
