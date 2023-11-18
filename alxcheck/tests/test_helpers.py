import unittest
import os
import subprocess
from .base_test import BaseTest
from ..utils.helpers import is_python_virtual_env_folder


class TestIsPythonVirtualEnvFolder(BaseTest, unittest.TestCase):
    def test_virtual_env_folder_exists(self):
        # Create a tmp virtual environment
        subprocess.run(["python", "-m", "venv", "venv"], stdout=subprocess.PIPE)

        # Test the function with the created folder
        venv_path = os.path.join(os.getcwd(), "venv")
        result = is_python_virtual_env_folder(venv_path)

        # Assert that the result is True, as the virtual environment folder exists
        self.assertTrue(result)

    def test_virtual_env_folder_does_not_exist(self):
        # Create a temporary directory without a virtual environment file
        folder_path = "temp_folder"
        os.makedirs(folder_path, exist_ok=True)

        # Test the function with the created folder
        result = is_python_virtual_env_folder(folder_path)

        # Assert that the result is False, as the virtual environment folder does not exist
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
