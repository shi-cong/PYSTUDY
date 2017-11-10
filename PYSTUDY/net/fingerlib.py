"""
指纹相关模块
"""
import socket


def get_host_finger(protocol, ip, port, timeout=5):
    """
    获取远程主机特定端口下服务的指纹
    :param protocol: 协议，tcp / udp
    :params ip: ip
    :params port: 端口
    :return: 服务器指纹
    """
    client = None
    msg = b"Hello, Server\r\n"
    if protocol == 'tcp':
        # tcp 协议
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(timeout)
        client.connect((ip, port))
        client.send(msg)
    elif protocol == 'udp':
        # udp 协议
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.settimeout(timeout)
        client.sendto(msg, (ip, port))
    else:
        raise Exception('协议不支持')

    serverFinger = client.recv(1024)
    client.close()
    return serverFinger
