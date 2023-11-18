import os
import sys


def is_python_virtual_env_folder(folder_path):
    return os.path.exists(f"{folder_path}/pyvenv.cfg")


def is_nodejs_project():
    """Checks for node.js command line switches"""
    switches = ("-js", "--nodejs-checks")
    for switch in switches:
        if switch in sys.argv:
            return True
    return False


def is_empty_init_py(file_path):
    """Checks if file is empty __init__.py"""
    if file_path.endswith('__init__.py'):
        from ..checks.general import check_file_not_empty
        if not check_file_not_empty(file_path):
            return True
    return False
