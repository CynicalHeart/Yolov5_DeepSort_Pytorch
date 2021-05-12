import os
import yaml
from easydict import EasyDict as edict


class YamlParser(edict):
    """
    This is yaml parser based on EasyDict.
    """

    def __init__(self, cfg_dict=None, config_file=None):
        if cfg_dict is None:
            cfg_dict = {}  # 若没有传入cfg文件, 则默认初始化为{}

        if config_file is not None:
            assert (os.path.isfile(config_file))  # 确认路径是否是文件
            with open(config_file, 'r') as fo:  # 读取文件
                cfg_dict.update(yaml.load(fo, Loader=yaml.FullLoader))  # 加载配置文件并载入dict

        super(YamlParser, self).__init__(cfg_dict)  # 调用EasyDict的初始化

    def merge_from_file(self, config_file):
        with open(config_file, 'r') as fo:
            self.update(yaml.load(fo, Loader=yaml.FullLoader))  # 初始化时没有文件, 后续融合文件信息

    def merge_from_dict(self, config_dict):
        self.update(config_dict)  # 融合dict信息


def get_config(config_file=None):
    return YamlParser(config_file=config_file)  # 读取yaml配置文件, 返回dict信息


if __name__ == "__main__":
    cfg = YamlParser()
    cfg.merge_from_file("../configs/deep_sort.yaml")
    print(cfg)
