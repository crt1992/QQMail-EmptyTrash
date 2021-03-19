import allure
import pytest
from business.login_business import loginBusiness
from selenium import webdriver
from tools.read_ini import read_ini
from util.save_screenshot import screenshot
from business.main_business import mainBusiness
import time
from util.log import log
import traceback

class TestRelogin:

    @allure.story('初始化')
    def setup_class(self):
        log.logging(msg='Initialize', level="INFO")
        self._case_name = " {}case:{}{}".format('<', TestRelogin.test_login.__name__, '>')
        self._case_name1 = " {}case:{}{}".format('<', TestRelogin.test_logout.__name__, '>')
        try:
            driver_path = read_ini(file_path='/data.ini').read_elements_data(node="driver", key="path")
            self.driver = webdriver.Chrome(driver_path)
            self.driver.maximize_window()
            self.driver.get("https://mail.qq.com/")
            screenshot().save_rt_screenshot(driver=self.driver, file_name='打开qq邮箱登陆页.png')
            self.main_ope = mainBusiness(self.driver)
            self.login = loginBusiness(self.driver)
        except:
            log.logging(msg=traceback.format_exc(), level='ERROR')

    @allure.story('登陆用例结束')
    def teardown_class(self):
        log.logging(msg='End of test! TearDown!', level='INFO')
        time.sleep(3)
        self.driver.close()

    @allure.story('执行登陆操作')
    @pytest.mark.run(order=1)
    def test_login(self):
        with allure.step('打印日志'):
            log.logging(msg='perform test_login case'+self._case_name, level='INFO')
        #log_in = loginBusiness(self.driver)
        with allure.step('进行登陆操作'):
            login_result = self.login.login_in()
        assert login_result

    @allure.story('执行退出登陆操作')
    @pytest.mark.run(order=1)
    def test_logout(self):
        log.logging(msg='perform test_logout case' + self._case_name1, level='INFO')
        result = self.main_ope.logout()
        assert result

    @allure.story('再次执行登陆操作')
    @pytest.mark.run(order=3)
    def test_login1(self):
        log.logging(msg='perform test_login case again' + self._case_name, level='INFO')
        time.sleep(2)
        login_result = self.login.login_in()
        assert login_result

if __name__ == '__main__':
    pytest.main(['login_relogin_test.py', '-v', '-s'])
