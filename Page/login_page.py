from selenium import webdriver
from tools.read_ini import read_ini
from tools.find_elements import find_elements
from util.singleton import singleton
@singleton
class login:
    login_frame_flag = 0
    verify_frame_flag = 0
    def __init__(self, driver):
        self.fe = find_elements(driver)

    def __switch_to_login_frame__(self):
        if not self.login_frame_flag:
            a = self.fe.find_element('login_frame')
            self.fe.switch_to_frame(a)
            self.login_frame_flag = 1

    def __switch_to_verify_frame__(self):
        if not self.verify_frame_flag:
            a = self.fe.find_element('lgoin_verify_frame')
            self.fe.switch_to_frame(a)
            self.verify_frame_flag = 1

    def get_username_element(self):
        self.__switch_to_login_frame__()
        return self.fe.find_element('login_name')

    def get_pwd_element(self):
        self.__switch_to_login_frame__()
        return self.fe.find_element('login_pwd')

    def get_login_btn_element(self):
        self.__switch_to_login_frame__()
        return self.fe.find_element('login_btn')

    def get_verify_element(self):
        self.__switch_to_verify_frame__()
        return self.fe.find_element('login_verify_slideBar')

    def get_driver(self):
        return self.fe.get_driver()

if __name__ == '__main__':
    driver_path = read_ini(file_path='/driver.ini', node='driver').read_elements_data('path')
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get("https://mail.qq.com/")
    a = login(driver=driver)
