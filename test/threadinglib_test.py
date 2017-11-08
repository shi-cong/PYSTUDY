import import_module
from PYSTUDY.unittestlib import run_one_test, TestCase
from PYSTUDY.threadinglib import create_thread, active_count
from PYSTUDY.pprintlib import pfomart
from PYSTUDY.loglib import Logger
from PYSTUDY.timelib import sleep
from PYSTUDY.net.fingerlib import get_host_finger
import socket


LOG = Logger('threadinglibtest')

def conn(host, port):
    try:
        fg = get_host_finger(host, port)
        LOG.log(pfomart([host, port, fg]))
    except Exception as e:
        print(e)


class ThreadinglibTest(TestCase):
    def test_thread(self):
        host = 'www.whsjyr.net'
        i = 0
        while i < 100:
            if active_count() <= 100: 
                # 这里将False改为True，线程都不会运行，不是说不运行，主线程退出，其它线程都死掉了
                create_thread(False, conn, host, i).start()
                i += 1
            else:
                sleep(2)


if __name__ == '__main__':
    run_one_test(ThreadinglibTest, 'test_thread')
