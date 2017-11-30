"""
调试模块
"""

import traceback
import warnings

def trace_info():
    """
    打印异常完整堆栈报错信息
    :return:
    """
    return traceback.format_exc()

def ignore_warnings():
    """
    忽略warning
    """
    warnings.filterwarnings('ignore')
