from functools import wraps
from time import time


def is_video(ext: str):
    """
    Returns true if ext exists in allowed_exts for video files.
    Args:
        ext:'.mp4', '.webm', '.ogg', '.avi', '.wmv', '.mkv', '.3gp'
    Returns: True or False
    """
    # 允许的后缀列表, 在此列表中认定为视频
    allowed_exts = ('.mp4', '.webm', '.ogg', '.avi', '.wmv', '.mkv', '.3gp')
    return any((ext.endswith(x) for x in allowed_exts))  # 满足1个就返回True


def tik_tok(func):
    """
    keep track of time for each process. 装饰器添加计时功能
    Args:
        func: 要装饰的函数
    Returns:
        添加装饰后的函数对象
    """

    # 在不改变原有功能代码的基础上,添加额外的功能. --计时
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = time()
        try:
            return func(*args, **kwargs)
        finally:
            end_ = time()
            # 时间太段容易发生除0异常
            print("time: {:.04f}s, fps: {:.04f}".format(end_ - start, 1 / (end_ - start)))

    return _time_it  # 返回此函数对象, 通过它可调用附加了计时功能的func
