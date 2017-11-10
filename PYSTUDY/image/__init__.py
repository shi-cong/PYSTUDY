"""
图形操作模块
"""

import imghdr

def what(pic_filename):
    """
    获得图片的真实类型
    :param pic_name: 图片文件名
    :return:
    """
    return imghdr.what(pic_filename)


__all__ = ['opencvlib', 'pillib']
