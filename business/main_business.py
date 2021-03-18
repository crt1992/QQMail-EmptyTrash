from time import sleep
from Handler.main_handler import mainHandler
from util.save_screenshot import screenshot
from util.log import log
import sys
import traceback

class mainBusiness:
    def __init__(self, driver):
        self.driver = driver

    def get_trash_num(self):
        trash_num = mainHandler(self.driver).get_trash_num()
        return trash_num

    def get_deleted_num(self):
        deleted_num = mainHandler(self.driver).get_mail_count()
        return deleted_num

    def qc_empyt_all_trash_mail(self, comfirm_flag, onebyone_flag=False):
        if not isinstance(comfirm_flag, bool):
            raise Exception("comfirm参数必须是bool值")
        main_op = mainHandler(self.driver)
        main_op.click_trash()
        sleep(1)
        if main_op.get_mail_count() == 0:
            main_op.go_to_home_page()
        else:
            if onebyone_flag:
                main_op.choose_mail_onebyone()
            else:
                main_op.quick_choose_all_mail()
            sleep(1)
            main_op.click_quick_delete_btn()
            sleep(2)
            if comfirm_flag:
                main_op.click_comfirm_btn()
            else:
                main_op.click_cancel_btn()
            sleep(2)
            main_op.go_to_home_page()


    def qc_empyt_all_deleted_mail(self, comfirm_flag, onebyone_flag=False):
        try:
            case_name = '{}case:{}{}'.format(' <', sys._getframe(1).f_code.co_name, '>')
            if not isinstance(comfirm_flag, bool):
                raise Exception("comfirm参数必须是bool值")
            main_op = mainHandler(self.driver)
            log.logging(msg='click deleted button'+case_name)
            sleep(1)
            main_op.click_deleted()
            sleep(1)
            screenshot().save_rt_screenshot(driver=self.driver, file_name='点击已删除进入已删除邮箱列表页.png')
            if onebyone_flag:
                log.logging(msg='choose mail one by one'+case_name)
                main_op.choose_mail_onebyone()
            else:
                log.logging(msg='click choose all button'+case_name)
                main_op.quick_choose_all_mail()
            screenshot().save_rt_screenshot(driver=self.driver, file_name='选中所有邮件.png')
            sleep(1)
            log.logging(msg='click quick delete button'+case_name)
            main_op.click_quick_delete_btn()
            sleep(2)
            screenshot().save_rt_screenshot(driver=self.driver, file_name='点击删除按钮.png')
            if comfirm_flag:
                log.logging(msg='click comfirm button'+case_name)
                main_op.click_comfirm_btn()
                screenshot().save_rt_screenshot(driver=self.driver, file_name='确认删除.png')
            else:
                log.logging(msg='click cancel button'+case_name)
                main_op.click_cancel_btn()
                screenshot().save_rt_screenshot(driver=self.driver, file_name='取消删除.png')
            sleep(2)
            screenshot().save_rt_screenshot(driver=self.driver, file_name='回到主页.png')
            mail_num = main_op.get_mail_count()
            return mail_num
        except:
            log.logging(msg=traceback.format_exc(), level='ERROR')
            return False