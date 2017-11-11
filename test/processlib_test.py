import import_module

from PYSTUDY.processlib import create_process, start_process, get_process_pid
from PYSTUDY.unittestlib import TestCase, run_one_test

def f():
    i = 0
    while True:
        print(i)
        i += 1


class ProcesslibTest(TestCase):
    def test_process(self):
        bp = create_process(True, 'test', f)
        start_process(bp)


if __name__ == '__main__':
    run_one_test(ProcesslibTest, 'test_process')
    input()
