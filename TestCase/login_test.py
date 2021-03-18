import sys, os
sys.path.append(os.pardir)
"""
terminal运行时将当前系统的工作目录加入到python运行环境的path中
所以terminal运行脚本时需要进入TestCase文件夹下运行脚本，否则仍然会出现import model导报错误
os.pardir指当前目录的父目录
因为在～项目完整的工作目录是～/PycharmProjects/QQMail—EmptyTrash/TestCase
terminal进入～/TestCase目录下执行脚本，os.pardir就是～/PycharmProjects/QQMail—EmptyTrash
导包就是从～/PycharmProjects/QQMail—EmptyTrash去寻找
目录错误就会找不到导入的包，然后报错
"""
import allure
import pytest
from business.login_business import loginBusiness
from selenium import webdriver
from tools.read_ini import read_ini
from util.save_screenshot import screenshot
import time
from util.log import log
import traceback

class Testlogin:

    @allure.story('初始化')
    def setup_class(self):
        log.logging(msg='Initialize', level="INFO")
        self._case_name = " {}case:{}{}".format('<', Testlogin.test_login.__name__, '>')
        try:
            driver_path = read_ini(file_path='/data.ini').read_elements_data(node="driver", key="path")
            self.driver = webdriver.Chrome(driver_path)
            self.driver.maximize_window()
            self.driver.get("https://mail.qq.com/")
            screenshot().save_rt_screenshot(driver=self.driver, file_name='打开qq邮箱登陆页.png')
        except:
            log.logging(msg=traceback.format_exc(), level='ERROR')

    @allure.story('登陆用例结束')
    def teardown_class(self):
        log.logging(msg='End of test! TearDown!', level='INFO')
        time.sleep(3)
        self.driver.close()

    @allure.story('执行登陆操作')
    def test_login(self):
        with allure.step('打印日志'):
            log.logging(msg='perform test_login case'+self._case_name, level='INFO')
        log_in = loginBusiness(self.driver)
        with allure.step('进行登陆操作'):
            login_result = log_in.login_in()
        assert login_result

if __name__ == '__main__':
    pytest.main(['login_test.py', '-v', '-x', "--alluredir=/Users/chenrongtao/.jenkins/workspace/QQmail-UI-Test/allure-results","--clean-alluredir"])


