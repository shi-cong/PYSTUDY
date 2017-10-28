"""
指纹相关模块
"""
import socket


def get_host_finger(ip, port):
    """
    获取远程主机特定端口下服务的指纹
    :params ip: ip
    :params port: 端口
    :return: 服务器指纹
    """
    client = socket.socket()
    client.connect((ip, port))
    client.send(b"Hello, Server\r\n")
    serverFinger = client.recv(1024)
    client.close()
    return serverFinger
