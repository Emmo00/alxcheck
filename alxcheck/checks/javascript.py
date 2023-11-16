import subprocess
from ..utils.error_logging import print_please_install_semistandard


def check_javascript_shebang(file_path):
    flag = True
    with open(file_path, "r") as f:
        first_line = f.readline().strip()
        if first_line not in ("#!/usr/bin/node", "#!/usr/bin/env node"):
            flag = False
    return flag


def semistandard_check(file_path):
    try:
        result = subprocess.run(["semistandard", file_path])
    except Exception:
        print_please_install_semistandard()
        return False
    return result == 0


def check_no_var(file_path):
    with open(file_path, "r") as f:
        content = f.read()
        lines = content.split("\n")
        for line in lines:
            if line.strip().startswith("var "):
                return False
        return True
