import inspect
import logging

import pytest


@pytest.mark.usefixtures("get_driver","get_url")
class BaseClass:

    def get_logger(self):
        test_method_name = inspect.stack()[1][3]
        thislogger = logging.getLogger(test_method_name)
        #ts = time.strftime("%Y%m%d-%H%M%S")
        filehandler = logging.FileHandler("log.txt")
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")
        filehandler.setFormatter(formatter)
        if thislogger.hasHandlers():
            thislogger.handlers.clear()
        thislogger.addHandler(filehandler)
        thislogger.setLevel(logging.INFO)
        return thislogger

    def log_testdata_info(self, log, testdata):
        log.info("Test data:")
        for x, y in testdata.items():
            log.info(f"  {x}={y}")
