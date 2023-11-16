import subprocess


def betty_check():
    try:
        result = subprocess.run(
            ["betty", "*.c"],
            stdout=subprocess.STDOUT,
            stderr=subprocess.STD_ERROR_HANDLE,
            text=True,
        )
    except subprocess.CalledProcessError:
        return False
    return result.returncode == 0