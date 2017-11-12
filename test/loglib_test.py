import import_module
from PYSTUDY.loglib import Logger
from PYSTUDY.unittestlib import run_one_test, TestCase
from PYSTUDY.oslib import getcwd
from PYSTUDY.threadinglib import create_thread, active_count

def write_log(logger, msg):
    for i in range(100000):
        logger.log(msg)

class LoglibTest(TestCase):
    def test_logfile(self):
        fileName = getcwd() + '/log_data/' + 'test_logfile.log'
        log = Logger('test_logfile', fileName)
        tasks = []
        for i in range(100):
            t = create_thread(True, write_log, log, "mm5201314_%d" % i)
            t.start()
            tasks.append(t)
        for t in tasks:
            t.join()

if __name__ == '__main__':
    run_one_test(LoglibTest, 'test_logfile')
