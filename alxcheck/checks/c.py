import subprocess
from ..utils.error_logging import print_please_install_betty


def betty_check(file_path):
    try:
        result = subprocess.run(["betty", file_path])
    except Exception:
        print_please_install_betty()
        return False
    return result.returncode == 0
