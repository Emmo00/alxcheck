import os
import sys
from .checks import *
from .utils.error_logging import *


def main():
    if not check_file_present("README.md"):
        print_file_not_present("README.md")
        sys.exit(1)
    if not check_file_not_empty("README.md"):
        print_file_empty("README.md")
    betty_check()
    for root, dirs, files in os.walk("."):
        if "venv" in dirs:
            dirs.remove("venv")
        if "env" in dirs:
            dirs.remove("env")
        for file in files:
            file_path = os.path.join(root, file)
            if not check_file_ends_with_new_lines(file_path):
                print_no_ending_new_line(file_path)
            if file_path.endswith(".py"):
                # python checks
                if not check_file_is_executable(file_path):
                    print_file_not_executable(file_path)
                if not check_python_shebang(file_path):
                    print_no_shebang(file_path)
                check_module_function_class_documentation(file_path)
                pycodestyle_check(file_path)
            if file.endswith(".js"):
                # javascript checks
                if not check_file_is_executable(file_path):
                    print_file_not_executable(file_path)
                if not check_javascript_shebang(file_path):
                    print_no_shebang(file_path)
                if not check_no_var(file_path):
                    print_var_was_used(file_path)
                semistandard_check(file_path)


if __name__ == "__main__":
    main()
