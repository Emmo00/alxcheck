import os
import unittest
from .test_general import TestGeneralChecks
from checks import check_python_shebang, check_file_is_executable


class TestPythonChecks(unittest.TestCase):
    def setUp(self) -> None:
        TestGeneralChecks().setUp()

    def tearDown(self) -> None:
        TestGeneralChecks().tearDown()

    def test_python_shebang_check(self):
        py_file = open("script.py", "w")
        py_file.close()
        self.assertFalse(check_python_shebang("script.py"))
        py_file = open("script.py", "w")
        py_file.write("#!/usr/bin/python3\n")
        py_file.close()
        self.assertTrue(check_python_shebang("script.py"))

    def test_file_executable_check(self):
        f = open("script.py", "w")
        f.close()
        os.chmod("script.py", 0o777)
        self.assertTrue(check_file_is_executable("script.py"))
