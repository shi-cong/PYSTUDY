import import_module
from PYSTUDY.unittestlib import run_one_test, TestCase
from PYSTUDY.threadinglib import create_thread, active_count
from PYSTUDY.pprintlib import pfomart
from PYSTUDY.loglib import Logger
from PYSTUDY.timelib import sleep
import socket


LOG = Logger('threadinglibtest')

def conn(host, port):
    client = socket.socket()
    try:
        client.connect((host, port))
        LOG.log(pformat([host, port]))
    except:
        pass
    finally:
        client.close()


class ThreadinglibTest(TestCase):
    def test_thread(self):
        host = 'www.whsjyr.net'
        i = 0
        while i < 65536:
            if active_count() <= 200: 
                create_thread(False, conn, host, i).start()
                i += 1
            else:
                LOG.log('[*] 线程达到上限！')
                sleep(2)


if __name__ == '__main__':
    run_one_test(ThreadinglibTest, 'test_thread')
