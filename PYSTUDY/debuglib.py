"""
调试模块
"""

import traceback

def trace_info():
    """
    打印异常完整堆栈报错信息
    :return:
    """
    return traceback.format_exc()