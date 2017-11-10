import import_module
from PYSTUDY.unittestlib import run_one_test, TestCase
from PYSTUDY.threadinglib import create_thread, active_count
from PYSTUDY.pprintlib import pfomart
from PYSTUDY.loglib import Logger
from PYSTUDY.timelib import sleep
from PYSTUDY.net.fingerlib import get_host_finger
from PYSTUDY.debuglib import trace_info


LOG = Logger('threadinglibtest')

def conn(protocol, host, port):
    try:
        fg = get_host_finger(protocol, host, port)
        LOG.log(pfomart([host, port, fg]))
    except Exception as e:
        print(trace_info())


class ThreadinglibTest(TestCase):
    def setUp(self):
        self.host = '180.101.192.249'

    def test_thread(self):
        # host = 'www.whsjyr.net'
        i = 1
        protocol = 'udp'
        while i < 65536:
            if active_count() <= 100: 
                # 这里将False改为True，线程都不会运行，不是说不运行，主线程退出，其它线程都死掉了
                create_thread(False, conn, protocol, self.host, i).start()
                i += 1
            else:
                sleep(2)

    def test_udp(self):
        conn('udp', self.host, 27019)

    def test_udp_raw_sock(self):
        import socket
        import logging
        logging.basicConfig(level=logging.DEBUG)
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(10)
        s.sendto(b'', ('localhost', 8000))
        LOG.log(s.recv(1024))
        LOG.log('等待主机返回信息')
        s.close()


if __name__ == '__main__':
    # run_one_test(ThreadinglibTest, 'test_thread')
    run_one_test(ThreadinglibTest, 'test_udp_raw_sock')
