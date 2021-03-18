import pytest
from business.login_business import loginBusiness
from selenium import webdriver
from tools.read_ini import read_ini
from util.save_screenshot import screenshot
import time
from business.main_business import mainBusiness
from util.log import log
import traceback

class TestDelmail:

    def setup_class(self):
        """
        初始化登陆操作
        :return:
        """
        log.logging(msg='Initialize', level="INFO")
        self._deleted_name = " {}case:{}{}".format('<', TestDelmail.test_del_deleted_mail.__name__, '>')
        #self._trash_name2 = " {}case:{}{}".format('<', TestDelmail.test_del_trash_mail.__name__, '>')
        driver_path = read_ini(file_path='/data.ini').read_elements_data(node="driver", key="path")
        self.driver = webdriver.Chrome(driver_path)
        self.driver.maximize_window()
        self.driver.get("https://mail.qq.com/")
        screenshot().save_rt_screenshot(driver=self.driver, file_name='打开qq邮箱登陆页.png')
        log_in = loginBusiness(self.driver)
        log_in.login_in()

    def teardown_class(self):
        """
        用例执行结束关闭浏览器
        :return:
        """
        log.logging(msg='End of test! TearDown!', level='INFO')
        time.sleep(3)
        self.driver.close()

    @pytest.mark.run(order=1)
    def test_del_deleted_mail(self):
        """
        清空已删除里的所有邮件
        :return:
        """
        mb = mainBusiness(self.driver)
        ope_result = mb.qc_empyt_all_deleted_mail(comfirm_flag=False, onebyone_flag=True)
        log.logging(msg="assert {}={}".format(mb.get_deleted_num(),ope_result)+self._deleted_name)
        assert mb.get_deleted_num() == ope_result

    # @pytest.mark.run(order=2)
    # def test_del_trash_mail(self):
    #     """
    #     清空垃圾箱里的所有邮件
    #     :return:
    #     """
    #     mb = mainBusiness(self.driver)
    #     ope_result = mb.qc_empyt_all_trash_mail(comfirm_flag=False, onebyone_flag=True)
    #     if ope_result:
    #         assert mb.get_trash_num() == 0

if __name__ == '__main__':
    pytest.main(["del_all_deleted_mail.py", "-v"])


