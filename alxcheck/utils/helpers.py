import os


def is_python_virtual_env_folder(folder_path):
    return os.path.exists(f"{folder_path}/pyvenv.cfg")
