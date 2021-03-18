import configparser
import sys,os
from util.singleton import singleton

@singleton
class read_ini:
    """读取配置文件信息"""
    def __init__(self, file_path = None):
        self.path = file_path
        if file_path == None:
            raise Exception("配置文件节点不能为空")
        self.cf = self.__load_file__(os.path.abspath(os.path.dirname(os.getcwd()))+"/configFile"+self.path)


    def __load_file__(self,file_path):
        cf = configparser.ConfigParser()
        cf.read(file_path)
        return cf

    def read_elements_data(self, node , key):
        return self.cf.get(section=node, option=key)

if __name__ == '__main__':
    a = read_ini(file_path="/data.ini")
    print(a.read_elements_data("Elements","login_frame"))