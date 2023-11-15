import os
from checks import *


def main():
    check_readme_present()
    check_readme_not_empty()
    for root, dirs, files in os.walk("."):
        for file in files:
            file_path = os.path.join(root, file)
            check_file_ends_with_new_lines(file_path)
            if file_path.endswith(".py"):
                # python checks
                check_file_is_executable_and_python_shebang(file_path)
                check_module_function_class_documentation(file_path)
                pycodestyle_check(file_path)
            if file.endswith(".js"):
                # javascript checks
                check_file_is_executable_and_javascript_shebang(file_path)
                check_no_var(file_path)
                semistandard_check(file_path)
    betty_check()
