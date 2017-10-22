from unittest import TestCase, main
import import_module
from PYSTUDY.oslib import parent_dir, listdir


class OSlibTestCase(TestCase):
    def test_parent_dir(self):
        cwd = __file__
        print('cwd:', cwd)
        print(parent_dir(cwd))
        prd = parent_dir("/PYSTUDY/a")
        print('prd:', prd)

    def test_listdir(self):
        print(listdir('.'))

if __name__ == '__main__':
    main()
