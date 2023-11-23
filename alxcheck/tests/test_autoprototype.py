import unittest
from unittest.mock import patch
import os, shutil
import subprocess
from alxcheck.checks.autoprototype import (
    check_ctags,
    generate_tags,
    filter_tags,
    create_header,
    delete_files,
    check_directory,
    check_header_file,
)
class TestYourFunctions(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = 'test_directory_1'
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)

    def tearDown(self):
        try:
            if os.path.exists(self.test_dir):
                shutil.rmtree(self.test_dir)
        except Exception as e:
            print(f"Error during cleanup: {e}")

    def test_check_ctags(self):
        # Mock the subprocess.run to simulate a successful run
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 0
            
            self.assertTrue(check_ctags())

        # Mock the subprocess.run to simulate a failed run
        with patch('subprocess.run') as mock_run:
            mock_run.side_effect = subprocess.CalledProcessError(returncode=1, cmd='')
            self.assertFalse(check_ctags())

    def test_generate_tags(self):
        # Mock the subprocess.run to simulate a successful run
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 0
            generate_tags(self.test_dir)
            mock_run.assert_called_once_with(['ctags', '-R', '--c-kinds=+p', '--fields=+S', '--extra=+q', self.test_dir], check=True)
    def test_create_header(self):
        # Test the create_header function

        # Create a sample filtered_tags content
        filtered_tags_content = "int func1();\nchar *func2();\n"

        # Define the header file path
        header_file_path = os.path.join(self.test_dir, 'test_header.h')

        # Call the create_header function
        create_header(header_file_path, filtered_tags_content)

        # Assert that the header file is created with the expected content
        expected_content = (
            '#ifndef TEST_HEADER_H\n'
            '#define TEST_HEADER_H\n\n'
            'int func1();\n'
            'char *func2();\n\n'
            '#endif\n'
        )

        with open(header_file_path, 'r') as header_file:
            actual_content = header_file.read()

        self.assertEqual(expected_content, actual_content)

    def test_check_directory(self):
        # Test when the directory exists
        self.assertTrue(check_directory(self.test_dir))
        

        # Test when the directory does not exist
        with patch('builtins.print') as mock_print:
            self.assertFalse(check_directory('/path/to/nonexistent/directory'))
            mock_print.assert_called_with("Error: Directory '/path/to/nonexistent/directory' does not exist.")

    def test_check_header_file(self):
        # Test a valid header file
        self.assertTrue(check_header_file('valid_header.h'))

        # Test an invalid header file
        with patch('builtins.print') as mock_print:
            self.assertFalse(check_header_file('invalid_header.txt'))
            mock_print.assert_called_with("Error: Invalid header file. It should have a '.h' extension.")


    # Additional test cases for different scenarios can be added as needed...

if __name__ == '__main__':
    unittest.main()
