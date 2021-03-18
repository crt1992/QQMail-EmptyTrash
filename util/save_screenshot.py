import os
import sys
import time
class screenshot:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            screenshot_dir = os.path.abspath(os.path.dirname(os.getcwd())) + '/screenshot'          #os.path.abspath(os.path.dirname(os.getcwd()))获取当前的项目的根目录
            if os.path.exists(screenshot_dir):
                local_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
                cls._main_dir = screenshot_dir + "/" + local_time
                cls._failed_dir = cls._main_dir + "/failed_screenshots"
                cls._runtime_dir = cls._main_dir + "/runtime_screenshots"
                os.mkdir(cls._main_dir)
                if not os.path.exists(cls._failed_dir):
                    os.mkdir(cls._failed_dir)
                if not os.path.exists(cls._runtime_dir):
                    os.mkdir(cls._runtime_dir)
            else:
                os.mkdir(screenshot_dir)
                cls()
            cls._instance = object.__new__(cls)
        return cls._instance

    def save_rt_screenshot(self, driver, file_name):
        if "." not in file_name:
            file_name += ".png"
        file_path = self._runtime_dir + "/" + file_name
        driver.save_screenshot(file_path)

    def save_fail_screenshot(self, driver, file_name):
        if "." not in file_name:
            file_name += ".png"
        file_path = self._failed_dir + "/" + file_name
        driver.save_screenshot(file_path)

if __name__ == '__main__':
    a = screenshot()
    a.save_rt_screenshot(driver=1, file_name="test")


