"""
日志模块
"""
from PYSTUDY.timelib import get_current_timestamp, timestamp_to_time
from PYSTUDY.oslib import getsize, rename
from PYSTUDY.threadinglib import Lock


class Logger(object):
    def __init__(self, startName, fileName=None):
        """
        初始化日志类
        :params startName: 若为"DEBUG"，则会打印log开头以DEBUG开始
        :params fileName: 需要写入日志的文件名
        """
        self.startName = startName
        self.fileName = fileName
        if self.fileName:
            self.__f = open(self.fileName, 'a')

    lock = Lock()

    def check_log_file_size(self):
        """如果日志文件超过100M，先保存源文件，再将原日志文件名后加“_时间戳”保存，再
        重新以原文件名以追加模式创建，这样就实现了，只要日志文件超过100M就自动备份。
        从而实现了控制日志文件大小的效果，由于在多线程进行同一个文件写入的时候，如果
        文件大小超过了100m，而这一时刻，也有很多线程监测到了文件大小超限制，所以这时
        那些知道超过了限制的线程就会改名文件，然后以追加方式重新打开文件，这样就会造成
        改名后的文件的大小有的字节数在0字节这个范围，所以，我引入了锁来控制。
        """
        with self.lock:
            if getsize(self.fileName) >= 1024 * 1024 * 1024:
                # 关闭文件
                self.__f.close()
                # 改名
                rename(self.fileName, self.fileName + '_' + str(get_current_timestamp()))
                # 重新创建日志
                self.__f = open(self.fileName, 'a')

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
            # 由于这里有很多的线程都要经过这道线程锁的控制，所以不会出现问题
            self.check_log_file_size()
            self.__f.write(theLog)


if __name__ == '__main__':
    l = Logger('app1')
    l.log('执行这个')
    l.log('执行这个')
    l.log('执行这个')
    l.log('执行这个')
