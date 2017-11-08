from threading import Thread, active_count, Lock

active_count = active_count
Lock = Lock


def synchronized_func(lock, callback, *callbackParams):
    """同步运行某方法, 同一时刻只允许一个线程访问某方法
    :param lock: 锁
    :param callback: 回调函数
    :param callback: 回调函数参数
    """
    with lock:
        callback(*callbackParams)


def create_thread(daemon, callback, *callbackParams):
    """创建一个线程
    :param daemon: True表示线程随着主线程关闭而关闭，False表示主线程必须等待子线程结束
    :param callback: 线程的回调函数
    :param callbackParams: 回调函数的形式参数
    :return: 一个线程类，初始状态为未启动，已经创建
    """
    task = Thread(target=callback, args=callbackParams)
    task.setDaemon(daemon)
    return task
