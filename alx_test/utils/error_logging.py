from colorama import Fore, Back


def print_file_not_present(file_path):
    print(Fore.RED + f"{file_path} file Not Found" + Fore.RESET)


def print_file_empty(file_path):
    print(Fore.RED + f"{file_path} File is Empty" + Fore.RESET)


def print_no_ending_new_line(file_path):
    print(Fore.RED + f"No new line at end of file: {file_path}" + Fore.RESET)


def print_file_not_executable(file_path):
    print(Fore.RED + f"{file_path} is not Executable", +Fore.RESET)


def print_no_shebang(file_path):
    print(Fore.RED + f"No shebang in {file_path}" + Fore.RESET)


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


def print_please_install_semistandard():
    print(
        Fore.RED
        + "Please Install Semistandard with the following command:\n\t"
        + Fore.RESET
        + Back.RED
        + "npm i semistandard -g"
        + Back.RESET
    )


def print_please_install_betty():
    print(
        Fore.RED
        + "Please make sure "
        + Back.RED
        + " Betty "
        + Back.RESET
        + " is Installed"
    )
