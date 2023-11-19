from colorama import Fore, Back


def print_file_not_present(file_path):
    print(Fore.RED + f"{file_path} file Not Found" + Fore.RESET)


def print_file_empty(file_path):
    print(Fore.RED + f"{file_path} file is Empty" + Fore.RESET)


def print_no_ending_new_line(file_path):
    print(Fore.RED + f"No new line at end of file: {file_path}" + Fore.RESET)


def print_file_not_executable(file_path):
    print(Fore.RED + f"{file_path} is not Executable" + Fore.RESET)


def print_no_shebang(file_path):
    print(Fore.RED + f"No shebang in {file_path}" + Fore.RESET)


def print_no_module_docstring(file_path):
    print(Fore.RED + f"{file_path} does not have Module DocString" + Fore.RESET)


def print_no_function_docstring(file_path, function_name):
    print(
        Fore.RED
        + f"In {file_path}, the {function_name} function has no Function DocString"
        + Fore.RESET
    )


def print_no_class_docstring(file_path, class_name):
    print(
        Fore.RED
        + f"In {file_path}, the {class_name} class has no Class DocString"
        + Fore.RESET
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
        + Fore.RESET
        + Back.RED
        + " Betty "
        + Back.RESET
        + Fore.RED
        + " is Installed"
        + Fore.RESET
    )


def print_var_was_used(file_path):
    print(Fore.RED + f"In {file_path}, 'var' was used." + Fore.RESET)


def print_check_docstrings(file_path):
    print(Fore.RED + f"Error: Check docstrings in {file_path}" + Fore.RESET)


def print_error_parsing_file(file_path):
    import ast

    try:
        with open(file_path, "r") as f:
            ast.parse(f.read())
    except SyntaxError as syntax_error:
        print(
            Fore.RED
            + f"SyntaxError\n\tFile: {file_path}\n\tLine: {syntax_error.lineno}\tMessage: {syntax_error.msg}"
            + Fore.RESET
        )
    except Exception as e:
        print(Fore.RED + f"Error Parsing File:\n\t{type(e)}" + Fore.RESET)


def print_uncaught_exception():
    print(
        Fore.YELLOW
        + "Uncaught Exception: Please raise an issue here with the contents of './error.txt'\n\thttps://github.com/Emmo00/alxcheck/issues"
        + Fore.RESET
    )
