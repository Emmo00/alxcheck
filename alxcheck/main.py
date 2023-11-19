import sys
from .checks import *
from .utils.helpers import *
from .utils.error_logging import *


def main():
    try:
        if not check_file_present("README.md"):
            print_file_not_present("README.md")
            sys.exit(1)
        if not check_file_not_empty("README.md"):
            print_file_empty("README.md")
        for root, dirs, files in os.walk("."):
            # exclude virtual environment folders
            for dir in dirs:
                if is_python_virtual_env_folder(dir):
                    dirs.remove(dir)
                    break
            # exclude .git folder
            if ".git" in dirs:
                dirs.remove(".git")
            for file in files:
                file_path = os.path.join(root, file)
                if file_path.endswith(
                    (".c", ".py", ".js", ".m", ".h", ".mjs", ".jsx", ".json")
                ):
                    if not check_file_ends_with_new_line(file_path):
                        if not is_empty_init_py(file_path):
                            print_no_ending_new_line(file_path)
                # c and c header files
                if file.endswith((".c", ".h")):
                    betty_check(file_path)
                # python checks
                if file_path.endswith(".py") and not is_empty_init_py(file_path):
                    if not check_file_is_executable(file_path):
                        print_file_not_executable(file_path)
                    if not is_empty_init_py(file_path) and not check_python_shebang(
                        file_path
                    ):
                        print_no_shebang(file_path)
                    check_module_function_class_documentation(file_path)
                    pycodestyle_check(file_path)
                # javascript checks
                if file.endswith(".js"):
                    if is_nodejs_project():
                        if not check_file_is_executable(file_path):
                            print_file_not_executable(file_path)
                        if not check_javascript_shebang(file_path):
                            print_no_shebang(file_path)
                    if not check_no_var(file_path):
                        print_var_was_used(file_path)
                    semistandard_check(file_path)
    except Exception as e:
        print_uncaught_exception()
        sys.stderr = open("./error.txt", "w")
        raise


if __name__ == "__main__":
    main()
