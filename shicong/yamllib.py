"""
yaml操作模块
"""
import yaml


class Yaml(object):
    def __init__(self, filename):
        f = open(filename, 'r')
        self.cfg = yaml.load(f.read())
        f.close()

    def get(self, key):
        return self.cfg[key]