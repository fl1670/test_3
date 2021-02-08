import time
import allure
from selenium.common.exceptions import NoSuchElementException

from FW.BaseFW import BaseFW


class AnyPage(BaseFW):

    def check_item(self, locator):
        try:
            self.find_element(locator)
            return True
        except NoSuchElementException:
            return False






