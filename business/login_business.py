import sys,os
from selenium import webdriver
from tools.read_ini import read_ini
from time import sleep
from Handler.login_handler import loginHandler
from business.main_business import mainBusiness
from util.get_mail_login_info import mail_login_info
from util.save_screenshot import screenshot
from util.log import log
import traceback

class loginBusiness:
    def __init__(self, driver):
        self.driver = driver
        self._username = mail_login_info.get_username()
        self._pwd = mail_login_info.get_pwd()

    def login_in(self):
        try:
            self.handler = loginHandler
            log_in = self.handler(driver=self.driver)
            case_name = '{}case:{}{}'.format(' <',sys._getframe(1).f_code.co_name,'>')
            log.logging(msg='input username'+case_name, level='INFO')
            log_in.send_username(self._username)
            log.logging(msg='input password'+case_name, level='INFO')
            log_in.send_pwd(self._pwd)
            screenshot().save_rt_screenshot(driver=self.driver, file_name='输入用户名密码.png')
            log.logging(msg='click login button'+case_name, level='INFO')
            log_in.click_login_btn()
            sleep(1)
            screenshot().save_rt_screenshot(driver=self.driver, file_name='点击登陆进入滑动验证页面.png')
            result = log_in.slide_verify_btn()
            screenshot().save_rt_screenshot(driver=self.driver, file_name='登陆成功.png')
            return result
        except:
            log.logging(msg=traceback.format_exc(), level="ERROR")
            return result

if __name__ == '__main__':
    driver_path = read_ini(file_path='/data.ini').read_elements_data(node="driver" , key="path")
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.maximize_window()
    driver.get("https://mail.qq.com/")
    screenshot().save_rt_screenshot(driver=driver, file_name='打开qq邮箱登陆页.png')
    log_in = loginBusiness(driver)
    main_opera = mainBusiness(driver)
    log_in.login_in()
    main_opera.qc_empyt_all_deleted_mail(comfirm_flag=False, onebyone_flag=True)