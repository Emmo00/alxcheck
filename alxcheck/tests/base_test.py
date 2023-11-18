import os, shutil


class BaseTest:
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
