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
    #pytest.main(['login_test.py', '-v', '-x', "--alluredir=/Users/chenrongtao/.jenkins/workspace/QQmail-UI-Test/allure-results","--clean-alluredir"])
    pytest.main(['login_test.py', '-v', '-s', "--alluredir=/Users/chenrongtao/PycharmProjects/port", "--clean-alluredir"])
