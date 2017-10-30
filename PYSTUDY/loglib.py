"""
日志模块
"""
from PYSTUDY.timelib import get_current_timestamp, timestamp_to_time

class Logger(object):
    def __init__(self, startName, fileName=None):
        """
        初始化日志类
        :params startName: 若为"DEBUG"，则会打印log开头以DEBUG开始
        :params fileName: 需要写入日志的文件名
        """
        self.startName = startName
        self.fileName = fileName

    def log(self, message):
        """
        打印或写日志
        :params message: 要打印或要写的日志
        """
        theLog = '[日志名:%s] [时间:%s] \n[内容:\n%s]\n\n' % (
                self.startName, timestamp_to_time(get_current_timestamp()),  message)
        if not self.fileName:
            print(theLog)
        else:
            # TODO 
            # 由于文件存在读写锁，并且，多线程和多进程存在文件纠纷。
            # 暂时没有很好的想法，先放放。
            pass


if __name__ == '__main__':
    l = Logger('app1')
    l.log('执行这个')
    l.log('执行这个')
    l.log('执行这个')
    l.log('执行这个')
