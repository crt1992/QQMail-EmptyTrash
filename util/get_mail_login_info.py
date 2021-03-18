from tools.read_ini import read_ini
from util.singleton import singleton

class mail_login_info:

    @classmethod
    def get_username(self):
        return read_ini(file_path="/data.ini").read_elements_data(node="mail_login", key='username')

    @classmethod
    def get_pwd(self):
        return read_ini(file_path="/data.ini").read_elements_data(node="mail_login", key='pwd')

if __name__ == '__main__':
    mail_login_info.get_pwd()
