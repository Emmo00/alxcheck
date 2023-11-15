import subprocess


def betty_check():
    result = subprocess.run(
        ["betty", "*.c"],
        stdout=subprocess.STDOUT,
        stderr=subprocess.STD_ERROR_HANDLE,
        text=True,
    )
    return result.returncode == 0
