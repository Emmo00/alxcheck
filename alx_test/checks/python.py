import os
import ast
import subprocess
from utils.error_logging import (
    print_no_module_docstring,
    print_no_function_docstring,
    print_no_class_docstring,
)


def check_file_is_executable(file_path):
    flag = True
    if not os.access(file_path, os.X_OK):
        flag = False
    return flag


def check_python_shebang(file_path):
    flag = True
    with open(file_path, "r") as f:
        first_line = f.readline().strip()
        if first_line not in ("#!/usr/bin/python3", "#!/usr/bin/env python3"):
            flag = False
    return flag


def check_module_function_class_documentation(file_path):
    flag = True
    with open(file_path, "r") as f:
        content = f.read()
        # remove shebang
        if content.startswith("#!"):
            content = content.split("\n", 1)[1]
        tree = ast.parse(content)
        # check module docstring
        if not tree.body and not isinstance(tree.body[0].value, ast.Str):
            flag = False
            print_no_module_docstring()
        for node in tree:
            # check function docstring
            if isinstance(node, ast.FunctionDef) and not isinstance(
                node.body[0].value, ast.Str
            ):
                flag = False
                print_no_function_docstring(file_path, node.name)
            # check class docstring
            if isinstance(node, ast.ClassDef) and not isinstance(
                node.body[0].value, ast.Str
            ):
                flag = False
                print_no_class_docstring(file_path, node.name)
    return flag


def pycodestyle_check(file_path):
    result = subprocess.run(
        ["pycodestyle", file_path], stdout=subprocess.STDOUT, text=True
    )
