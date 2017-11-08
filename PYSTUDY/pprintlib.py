"""
pprint 模块
"""
import pprint


def pfomart(obj):
    """格式化输出某对象
    :param obj: obj对象
    :return: 格式化出处的字符串
    """
    return pprint.pformat(obj)
