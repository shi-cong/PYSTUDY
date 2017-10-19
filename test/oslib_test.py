from unittest import TestCase
from PYSTUDY.oslib import parent_dir


class OSlibTestCase(TestCase):
    def test_parent_dir(self):
        cwd = __file__
        print('cwd:', cwd)
        print(parent_dir(cwd))
        prd = parent_dir("/PYSTUDY/a")
        print('prd:', prd)
