"""
进程模块
"""
from multiprocessing import Process

Process = Process

def create_process(daemon, name, callback, *callbackParams):
    """创建进程
    :param daemon: True主进程关闭而关闭, False主进程必须等待子进程结束
    :param name: 进程名称
    :param callback: 回调函数
    :param callbackParams: 回调函数参数
    :return: 返回一个进程对象
    """
    bp = Process(daemon=daemon, name=name, target=callback, args=callbackParams)
    return bp


def start_process(pro):
    """启动进程
    :param pro: 进程对象
    """
    pro.start()


def join_process(pro):
    """运行直到进程结束
    :parma pro: 进程对象
    """
    pro.join()

def terminate_process(pro):
    pro.terminate()

def get_process_pid(pro):
    return pro.pid

def get_process_name(pro):
    return pro.name
