from selenium import webdriver
from tools.read_ini import read_ini
from tools.find_elements import find_elements

class logout:

    def __init__(self, driver):
        self.fe = find_elements(driver)

    def get_relogin_element(self):
        return self.fe.find_element('relogin')