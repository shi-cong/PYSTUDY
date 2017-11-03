from threading import Thread

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
