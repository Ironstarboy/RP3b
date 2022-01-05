'''
没有指针机制，没法实现多线程需要的跨文件全局变量。维护一个字典
'''

global _global_dict
_global_dict = {'d':100}


def set(key, value):
    _global_dict[key] = value


def get(key):
    return _global_dict.get(key,None)