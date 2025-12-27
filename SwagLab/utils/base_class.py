import json
import os
import inspect
import logging
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseClass:

    @staticmethod
    def get_logger():
        log_path = f"logs/swag_lab_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        logger.setLevel(logging.DEBUG)

        if not logger.handlers:
            file_handler = logging.FileHandler(log_path)
            file_handler.setLevel(logging.DEBUG)

            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)

            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        logger.propagate = True
        return logger

    def wait_for_element_visibility(self, element, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(element))

    @staticmethod
    def get_data_from_json(filename, key=None):
        file_path = os.path.abspath(os.path.join("testData", filename))
        with open(file_path, "r") as f:
            data = json.load(f)
        return data[key] if key else data