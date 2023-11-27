import subprocess
from ..utils.error_logging import print_please_install_betty

def betty_check(file_path):
    try:
        result = subprocess.run(["betty", file_path])
    except Exception:
        print_please_install_betty()
        return False
    # because it have different ouput meaning looking for errors
    try:
        result1 = subprocess.run(["betty", file_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except subprocess.CalledProcessError as e:
        return False

    if "ERROR:" in result1.stdout or "ERROR:" in result1.stderr:
        return False

    return result.returncode == 0

