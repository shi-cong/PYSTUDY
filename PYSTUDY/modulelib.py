"""
模块库
"""

import inspect


def get_curent_module_classes(module):
    """
    获取制定模块的所有类
    :param module: 模块
    :return: 类的列表
    """
    classes = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            classes.append(obj)
    return classes
    # print(inspect.getmembers(sys.modules[module.__name__], inspect.isclass))


def is_subclass(obj, cls):
    """
    判断某一个类或者对象是否是某一个类的子类
    :param obj: 类或对象
    :param cls: 类
    :return: True or False
    """
    try:
        for i in obj.__bases__:
            if i is cls or isinstance(i, cls):
                return True
        for i in obj.__bases__:
            if isinstance(i, cls):
                return True
    except AttributeError:
        return isinstance(obj.__class__, cls)
    return False

def get_module_path(module_name):
    """
    获得一个模块的路径
    :param module_name: pyobject
    :return: 路径字符串
    """
    return module_name.__path__[0]
