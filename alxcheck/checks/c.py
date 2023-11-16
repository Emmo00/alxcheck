import subprocess


def betty_check(file_path):
    try:
        result = subprocess.run(
            ["betty", file_path],
            stdout=subprocess.STDOUT,
            stderr=subprocess.STD_ERROR_HANDLE,
            text=True,
        )
    except Exception:
        return False
    return result.returncode == 0
