import os
import ast
import subprocess
from ..utils.error_logging import (
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
    with open(file_path, "rb") as f:
        first_line = f.readline().strip()
        if first_line not in (b"#!/usr/bin/python3", b"#!/usr/bin/env python3"):
            flag = False
    return flag


def check_module_function_class_documentation(file_path):
    flag = True
    with open(file_path, "rb") as f:
        content = f.read()
        # remove shebang
        if content.startswith(b"#!"):
            content = content.split(b"\n", 1)[1]
        tree = ast.parse(content)
        # check module docstring
        if (
            not tree.body
            or not len(tree.body) > 0
            or not isinstance(tree.body[0], ast.Str)
        ):
            flag = False
            print_no_module_docstring(file_path)
        for node in tree.body:
            # check function docstring
            if isinstance(node, ast.FunctionDef) and not isinstance(
                node.body[0], ast.Str
            ):
                flag = False
                print_no_function_docstring(file_path, node.name)
            # check class docstring
            if isinstance(node, ast.ClassDef) and not isinstance(node.body[0], ast.Str):
                flag = False
                print_no_class_docstring(file_path, node.name)
    return flag


def pycodestyle_check(file_path):
    try:
        result = subprocess.run(
            ["pycodestyle", file_path], stdout=subprocess.STDOUT, text=True
        )
    except Exception:
        return False
    return result == 0
