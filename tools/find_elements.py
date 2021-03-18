from tools.read_ini import read_ini
from selenium import webdriver
import sys
class find_elements:
    def __init__(self, driver):
        self.driver = driver
        self.rdfile = read_ini(file_path="/data.ini")
        self.node = "Elements"

    def find_element(self, key):
        a = self.rdfile.read_elements_data(node=self.node,key=key)
        data = a.split('->')
        if data[0] == 'xpath':
            return self.driver.find_element_by_xpath(data[1])
        if data[0] == 'id':
            pass

    def find_elements(self, key):
        a = self.rdfile.read_elements_data(node=self.node,key=key)
        data = a.split('->')
        if data[0] == 'xpath':
            return self.driver.find_elements_by_xpath(data[1])
        if data[0] == 'id':
            pass

    def switch_to_frame(self, key): #login_frame
        return self.driver.switch_to.frame(key)

    def switch_to_parent_frame(self):
        return self.driver.switch_to.parent_frame()

    def get_driver(self):
        return self.driver

if __name__ == '__main__':
    driver_path = read_ini(file_path='/data.ini').read_elements_data(node="Element", key='path')
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get("https://mail.qq.com/")
    a = find_elements(driver)
    a.find_element('login_frame')

