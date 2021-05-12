from os import environ  # 获得系统的信息


# os.environ['HOMEPATH']:当前用户主目录。
# os.environ['TEMP']:临时目录路径。
# os.environ[PATHEXT']:可执行文件。
# os.environ['SYSTEMROOT']:系统主目录。
# os.environ['LOGONSERVER']:机器名。
# os.environ['PROMPT']:设置提示符。

def assert_in(file, files_to_check):
    if file not in files_to_check:
        raise AssertionError("{} does not exist in the list".format(str(file)))
    return True


def assert_in_env(check_list: list):
    for item in check_list:  # 遍历输入的列表
        assert_in(item, environ.keys())  # 判断每个输入是否在环境的字典中, 不在就会抛出异常
    return True
