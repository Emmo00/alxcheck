import unittest
from .base_test import BaseTest
from ..checks import (
    check_file_present,
    check_file_not_empty,
    check_file_ends_with_new_line,
)


class TestGeneralChecks(BaseTest, unittest.TestCase):
    def test_readme_present_check(self):
        self.assertFalse(check_file_present("README.md"))
        readme_fd = open("README.md", "w")
        readme_fd.close()
        self.assertTrue(check_file_present("README.md"))

    def test_readme_not_empty_check(self):
        readme_fd = open("README.md", "w+")
        readme_fd.close()
        self.assertFalse(check_file_not_empty("README.md"))
        readme_fd = open("README.md", "w+")
        readme_fd.write("Project description")
        readme_fd.close()
        self.assertTrue(check_file_not_empty("README.md"))

    def test_files_with_new_line_check(self):
        f = open("file", "w")
        f.close()
        self.assertFalse(check_file_ends_with_new_line("file"))
        f = open("file", "wb")
        f.write(b"line\n\n")
        f.close()
        self.assertTrue(check_file_ends_with_new_line("file"))


if __name__ == "__main__":
    unittest.main()
