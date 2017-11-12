from PYSTUDY.unittestlib import TestCase, run_one_test
import import_module
from PYSTUDY.oslib import parent_dir, listdir, getsize


class OSlibTestCase(TestCase):
    def test_parent_dir(self):
        cwd = __file__
        print('cwd:', cwd)
        print(parent_dir(cwd))
        prd = parent_dir("/PYSTUDY/a")
        print('prd:', prd)

    def test_listdir(self):
        print(listdir('.'))

    def test_getsize(self):
        cwd = __file__
        print(getsize(cwd))
        print(1024 * 1024  * 100)

if __name__ == '__main__':
    run_one_test(OSlibTestCase, 'test_getsize')
