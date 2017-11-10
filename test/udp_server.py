from socket import *

HOST = 'localhost'
PORT = 8000

s = socket(AF_INET,SOCK_DGRAM)
s.bind((HOST,PORT))
print('...waiting for message..')
while True:
    data,address = s.recvfrom(1024)
    print(data,address)
    # 下行注释之后，udp端口扫描将不会有信息返回，客户端会超时
    # s.sendto(b'this is the UDP server',address)
s.close()
