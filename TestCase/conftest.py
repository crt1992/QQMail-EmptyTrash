import pytest
from business.login_business import loginBusiness
from selenium import webdriver
from tools.read_ini import read_ini
from util.save_screenshot import screenshot
from util.log import log
import time

@pytest.fixture(scope='class', autouse=False)
def login():
    log.logging(msg='Initialize', level="INFO")
    driver_path = read_ini(file_path='/data.ini').read_elements_data(node="driver", key="path")
    driver = webdriver.Chrome(driver_path)
    driver.maximize_window()
    driver.get("https://mail.qq.com/")
    screenshot().save_rt_screenshot(driver=driver, file_name='打开qq邮箱登陆页.png')
    log_in = loginBusiness(driver)
    log_in.login_in()
    yield driver
    log.logging(msg='End of test! TearDown!', level='INFO')
    time.sleep(3)
    driver.close()