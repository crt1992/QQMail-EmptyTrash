from selenium import webdriver
from tools.read_ini import read_ini
from tools.find_elements import find_elements

class main_page:

    main_frame_flag = 0

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, driver):
        self.fe = find_elements(driver)

    def switch_to_mainframe(self):
        if not self.main_frame_flag:
            a = self.fe.find_element('main_frame')
            self.fe.switch_to_frame(a)
            self.main_frame_flag = 1

    def switch_to_parent_frame(self):
        self.fe.switch_to_parent_frame()

    def get_trash_btn_element(self):
        return self.fe.find_element('trash_bth')

    def get_deleted_btn_element(self):
        return self.fe.find_element('deleted_btn')

    # def get_all_delete_mail_elements(self):
    #     self.__switch_to_frame()
    #     for i in self.fe.find_elements('choose_deleted_mail_items'):
    #         yield i

    def get_trash_num(self):
        trash_num = self.fe.find_element('trash_num').text[1:-1]
        return int(trash_num)

    def get_quick_choose_mail_element(self):
        self.switch_to_mainframe()
        return self.fe.find_element('quick_choose_all')

    def get_del_mail_element(self):
        self.switch_to_mainframe()
        return self.fe.find_element('del_mail')
