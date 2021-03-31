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

    @pytest.mark.usefixtures('login')
    @pytest.mark.run(order=1)
    def test_del_deleted_mail(self, login):
        """
        清空已删除里的所有邮件
        :return:
        """
        driver = login
        mb = mainBusiness(driver)
        ope_result = mb.qc_empyt_all_deleted_mail(comfirm_flag=False, onebyone_flag=True)
        log.logging(msg="assert {}={}".format(mb.get_deleted_num(),ope_result))
        #print(str(TestDelmail.test_del_deleted_mail.__name__))
        assert mb.get_deleted_num() == ope_result

    @pytest.mark.run(order=2)
    def test_del_trash_mail(self, login):
        """
        清空垃圾箱里的所有邮件
        :return:
        """
        driver = login
        mb = mainBusiness(driver)
        ope_result = mb.qc_empyt_all_trash_mail(comfirm_flag=False, onebyone_flag=True)
        if ope_result:
            assert mb.get_trash_num() == 0

if __name__ == '__main__':
    pytest.main(["del_all_deleted_mail.py", "-v", "-s"])


