import sys,os
import logging
import logging.config
import datetime
import colorlog

class log:
    _log_colors_config = {
        'DEBUG': 'white',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
    _logger = logging.getLogger("UI_AUTO_TEST")  # 设置日志器
    _logger.setLevel(logging.DEBUG)  # 设置日志器的日志等级

    @classmethod
    def _set_handler_formatter(cls, filename, lineandfunc):
        cls._stream_handler = logging.StreamHandler(sys.stdout)  # 设置控制器 StreamHandler流控制器，sys.stdout控制台输出
        cls._stream_handler.setLevel(logging.DEBUG)  # 设置控制器的日志等级为DEBUG
        cls._console_formatter = colorlog.ColoredFormatter(
            fmt='%(log_color)s[%(asctime)s.%(msecs)d] {filename} -> {line_func} [%(levelname)s] : %(message)s'.format(
                filename=filename, line_func=lineandfunc),
            datefmt='%Y-%m-%d  %H:%M:%S',
            log_colors=cls._log_colors_config
        )  # 控制台输出不同等级不同显示颜色
        cls._stream_handler.setFormatter(cls._console_formatter)
        cls._file_handler = logging.handlers.TimedRotatingFileHandler(os.path.abspath(os.path.dirname(os.getcwd())) + '/log' + "/runtime.log",
                                                                  when='midnight', interval=1,
                                                                  backupCount=20,
                                                                  atTime=datetime.time(0, 0, 0, 0))
        cls._file_handler.setFormatter(logging.Formatter(
            "[%(asctime)s.%(msecs)d] {filename} -> {line_func} [%(levelname)s] : %(message)s".format(
                filename=filename, line_func=lineandfunc)))

    @classmethod
    def _add_handler(cls):
        cls._logger.addHandler(cls._stream_handler)
        cls._logger.addHandler(cls._file_handler)

    @classmethod
    def _remove_handler(cls):
        cls._logger.removeHandler(cls._stream_handler)
        cls._logger.removeHandler(cls._file_handler)

    @classmethod
    def logging(cls, msg, level="INFO"):
        _fileName = sys._getframe(1).f_code.co_filename.split('/')[-1]  # 获取调用的文件名
        _lineandfunc = sys._getframe(1).f_code.co_name +":" + str(sys._getframe(1).f_lineno)    # 获取调用的函数名和调用的文件行号
        cls._set_handler_formatter(_fileName,_lineandfunc)
        cls._add_handler()
        level_dict = {'INFO':cls._logger.info,
                      'DEBUG':cls._logger.debug,
                      'WARNING':cls._logger.warning,
                      'ERROR':cls._logger.error,
                      'CRITICAL':cls._logger.critical}
        level_dict[level](msg)
        cls._remove_handler()

if __name__ == '__main__':
    a = log()
    a.logging(msg='test', level='INFO')