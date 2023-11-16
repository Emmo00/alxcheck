import os
import shutil
import unittest
from ..checks import (
    check_file_present,
    check_file_not_empty,
    check_file_ends_with_new_lines,
)


class TestGeneralChecks(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        # create folder to be tested upon and set cwd
        os.mkdir("alx-project")
        os.chdir("alx-project")

    def tearDown(self) -> None:
        super().tearDown()
        # delete folder and reset cwd
        os.chdir("..")
        shutil.rmtree("alx-project")

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
        self.assertFalse(check_file_ends_with_new_lines("file"))
        f = open("file", "wb")
        f.write(b"line\n\n")
        f.close()
        self.assertTrue(check_file_ends_with_new_lines("file"))
