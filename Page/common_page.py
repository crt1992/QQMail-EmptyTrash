from tools.find_elements import find_elements

class common_page:

    main_frame_flag = 0
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, driver):
        self.fe = find_elements(driver)

    def __switch_to_frame(self):
        if not self.main_frame_flag:
            a = self.fe.find_element('main_frame')
            self.fe.switch_to_frame(a)
            self.main_frame_flag = 1

    def __switch_to_parent_frame(self):
        self.fe.switch_to_parent_frame()

    #垃圾箱按钮
    def get_trash_btn(self):
        return self.fe.find_element('deleted_btn')

    #删除按钮
    def get_qc_del_btn(self):
        self.__switch_to_frame()
        return self.fe.find_element('quick_del_main_btn')

    #彻底删除按钮
    def get_cp_del_btn(self):
        self.__switch_to_frame()
        return self.fe.find_element('completely_del_main_btn')

    #全选按钮
    def get_quick_choose_all_btn(self):
        self.__switch_to_frame()
        return self.fe.find_element('quick_choose_all')

    #确认对话框-取消按钮
    def get_del_mail_cancel_btn(self):
        self.__switch_to_parent_frame()
        #self.main_frame_flag=0
        return self.fe.find_element('del_mail_cancel_btn')

    #确认对话框-确认按钮
    def get_del_mail_confirm_btn(self):
        self.__switch_to_parent_frame()
        #self.main_frame_flag=0
        return self.fe.find_element('del_mail_confirm_btn')

    #点击home图标
    def get_home_page_btn(self):
        self.__switch_to_parent_frame()
        return self.fe.find_element("home_page_btn")

    #列表中所有邮件
    def choose_mail_onebyeone(self):
        self.__switch_to_frame()
        for i in self.fe.find_elements('choose_mail_onebyone'):
            yield i