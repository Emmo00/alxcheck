import os
import unittest
from .base_test import BaseTest
from ..checks import check_javascript_shebang, check_file_is_executable, check_no_var


class TestJavascriptChecks(BaseTest, unittest.TestCase):
    def test_javascript_shebang_check(self):
        js_file = open("script.js", "w")
        js_file.close()
        self.assertFalse(check_javascript_shebang("script.js"))
        js_file = open("script.js", "w")
        js_file.write("#!/usr/bin/node\n")
        js_file.close()
        self.assertTrue(check_javascript_shebang("script.js"))

    def test_file_executable_check(self):
        f = open("script.js", "w")
        f.close()
        os.chmod("script.js", 0o777)
        self.assertTrue(check_file_is_executable("script.js"))

    def test_no_var(self):
        f = open("script.js", "w")
        f.write("var a = 10;")
        f.close()
        self.assertFalse(check_no_var("script.js"))
        f = open("script.js", "w")
        f.write("let a = 10;")
        f.close()
        self.assertTrue(check_no_var("script.js"))


if __name__ == "__main__":
    unittest.main()
