from selenium import webdriver
from Page.qqmail_main_page import main_page
from Page.common_page import common_page
from Page.logout_page import logout
from Page.login_page import login
from tools.read_ini import read_ini
from time import sleep
from tools.find_elements import find_elements
from util.save_screenshot import screenshot
from util.log import log

class mainHandler:
    def __init__(self, driver):
        self.pure_dirver = driver
        self.driver = main_page(driver)
        self.common = common_page(driver)
        self.logout = logout(driver)
        self.login = login(driver)

    #点击垃圾箱
    def click_trash(self):
        """
        点击邮箱主页左侧导航了垃圾箱，进入垃圾箱列表
        """
        self.driver.switch_to_parent_frame()
        self.driver.get_trash_btn_element().click()
        self.common.main_frame_flag=0

    #点击已删除
    def click_deleted(self):
        """
        点击邮箱主页左侧导航了已删除，进入已删除列表
        """
        self.driver.switch_to_parent_frame()
        self.driver.get_deleted_btn_element().click()
        self.common.main_frame_flag=0

    def click_quick_delete_btn(self):
        """
        点击右侧iframe页面的删除按钮
        """
        self.common.get_qc_del_btn().click()

    #点击退出登陆按钮
    def click_logout_btn(self):
        self.driver.get_logout_btn_element().click()

    #点击重新登陆按钮
    def click_relogin_btn(self):
        self.logout.get_relogin_element().click()
        try:
            self.login.get_username_element()
            return True
        except:
            return False

    #一个个选中所有邮件
    def choose_mail_onebyone(self):
        for i in self.common.choose_mail_onebyeone():
            if not i.is_selected():
                i.click()
                sleep(1)

    #获取右侧垃圾箱显示个数
    def get_trash_num(self):
        return self.driver.get_trash_num()

    #点击iframe页面点击全选按钮
    def quick_choose_all_mail(self):
        self.common.get_quick_choose_all_btn().click()

    #点击回到主页
    def go_to_home_page(self):
        self.common.get_home_page_btn().click()

    #点击确认删除-确认按钮
    def click_comfirm_btn(self):
        self.common.get_del_mail_confirm_btn().click()
        self.common.main_frame_flag=0

    #点击确认删除-取消按钮
    def click_cancel_btn(self):
        self.common.get_del_mail_cancel_btn().click()
        self.common.main_frame_flag=0

    #获取当前iframe中邮件的个数
    def get_mail_count(self):
        all_mail = [i for i in self.common.choose_mail_onebyeone()]
        return len(all_mail)
