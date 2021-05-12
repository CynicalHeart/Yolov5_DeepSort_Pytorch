import logging


def get_logger(name='root'):
    # 规定输出格式 时间(年-月-日 时分秒) [日志等级] : 日志信息
    formatter = logging.Formatter(
        # fmt='%(asctime)s [%(levelname)s]: %(filename)s(%(funcName)s:%(lineno)s) >> %(message)s')
        fmt='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    handler = logging.StreamHandler()  # 输出到控制台
    handler.setFormatter(formatter)  # 设置格式

    logger = logging.getLogger(name)  # 获取日志名
    logger.setLevel(logging.INFO)  # 设置显示日志等级 INFO
    logger.addHandler(handler)  # 添加handler
    return logger  # 返回日志对象
