from selenium import webdriver
from Page.login_page import login
from time import sleep
from tools.find_elements import find_elements
from util.log import log
import traceback
import sys

class loginHandler:
    def __init__(self, driver):
        self.driver = login(driver)

    def clear_input_box(self,element):
        element.clear()

    def send_username(self, username):
        ur_element = self.driver.get_username_element()
        self.clear_input_box(ur_element)
        ur_element.send_keys(username)

    def send_pwd(self, pwd):
        self.driver.get_pwd_element().send_keys(pwd)

    def click_login_btn(self):
        self.driver.get_login_btn_element().click()
        self.driver.login_frame_flag = 0
        self.driver.verify_frame_flag = 0

    def slide_verify_btn(self):
        count = 1
        y = 170
        case_name = "{}case:{}{}".format('<', sys._getframe(2).f_code.co_name, '>')
        while True:
            try:
                log.logging(msg='start to login verify ---->%d time %s' %(count,case_name), level='INFO')
                count += 1
                sleep(2)
                slide_bar = self.driver.get_verify_element()
                action = webdriver.ActionChains(self.driver.get_driver())
                sleep(1)
                action.click_and_hold(slide_bar).perform()
                action.move_by_offset(y, 0).perform()
                sleep(1)
                action.release(on_element=slide_bar).perform()
                sleep(6)
            except:
                log.logging(msg=traceback.format_exc())
                return False
            try:
                find_elements(self.driver.get_driver()).find_element('trash_bth')
                return True
            except:
                if count >= 10:
                    return False
                y += 5