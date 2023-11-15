from colorama import Fore


def print_no_readme_file():
    print(Fore.RED + "README.md file Not Found" + Fore.RESET)


def print_readme_file_empty():
    print(Fore.RED + "README.md File is Empty")


def print_no_ending_new_line(file_path):
    print(Fore.RED + f"No new line at end of file: {file_path}" + Fore.RESET)


def print_file_not_executable(file_path):
    print(Fore.RED + f"{file_path} is not Executable", +Fore.RESET)


def print_no_shebang(file_path):
    print(Fore.RED + f"No shebang in {file_path}")


def print_no_module_docstring(file_path):
    print(Fore.RED + f"{file_path} does not have Module DocString" + Fore.RESET)


def print_no_function_docstring(file_path, function_name):
    print(
        Fore.RED
        + f"In {file_path}, {function_name} has no Function DocString"
        + Fore.RESET
    )


def print_no_class_docstring(file_path, class_name):
    print(
        Fore.RED + f"In {file_path}, {class_name} has no Class DocString" + Fore.RESET
    )
