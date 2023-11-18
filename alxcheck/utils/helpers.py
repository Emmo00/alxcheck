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
