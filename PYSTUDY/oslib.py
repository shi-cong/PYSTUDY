"""
文件操作模块
"""
import os
import os.path
import shutil
import platform

SEP = os.path.sep


def parent_dir(dirname):
    """
    返回上级目录
    文件名可以是文件夹或者文件
    :param dirname: 文件名
    :return:
    """
    return os.path.dirname(dirname)

def getcwd():
    """
    获取当前脚本路径
    :return:
    """
    return os.getcwd()

def system(cmd):
    """
    执行系统命令
    :param cmd: 命令字符串
    :return:
    """
    os.system(cmd)

def walk(direc):
    """
    递归文件夹
    :param direc: 文件夹名称
    :return:
    """
    return os.walk(direc)

def isdir(filename):
    """
    判断文件是否为文件夹
    :param filename: 文件名称
    :return: True 为文件夹，False不为文件夹
    """
    return os.path.isdir(filename)

def isfile(filename):
    """
    判断文件是否为文件
    :param filename:文件名称
    :return:True 是，False不是
    """
    return os.path.isfile(filename)

def join(paths):
    """
    拼接文件夹
    :param paths: 文件路径的列表
    :return: 拼接后的文件名称
    """
    return os.path.join(*paths)

def getsize(filename):
    """
    获得文件的大小
    :param filename: 文件名
    :return: 文件大小
    """
    return os.path.getsize(filename)

def exists(filename):
    """
    是否存在文件或者目录
    :param filename: 文件或目录名称
    :return: 存在返回True,不存在返回False
    """
    return os.path.exists(filename)

def split_ext(filename):
    """
    分离文件名和扩展名
    :param filename: 文件名
    :return: 元组 文件名称和扩展名
    """
    return os.path.splitext(filename)

def base_name(filename):
    """
    返回文件名
    :param filename:  文件名
    :return: 文件名
    """
    return os.path.basename(filename)

def curdir():
    """
    返回当前目录
    :return: 当前目录
    """
    return os.curdir

def mv(src, dst):
    """
    移动文件
    :param src:
    :param dst:
    :return:
    """
    shutil.move(src, dst)

def write_image(r, filename):
    """
    将流式数据存储在文件中
    :param r: 响应
    :param filename: 文件名
    :return:
    """
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(1024):
            fd.write(chunk)

def listdir(directory):
    """
    列出文件夹中的内容
    :param directory: 文件夹名
    :return: 文件名数组
    """
    tmp = []
    for f in os.listdir(directory):
            tmp.append(f)
    return tmp


def get_os_version():
    """
    获取操作系统版本号
    """
    return platform.platform()

def set_env(envName, envValue):
    """
    设置环境变量
    :params envName: env名字
    :params envValue: 值
    """
    os.environ[envName] = os.environ[envName] + ':' + envValue
