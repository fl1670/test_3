import allure
from allure_commons.types import AttachmentType

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseFW(object):

    time_element_Wait = 10

    def __init__(self, application_manager):
        self.manager = application_manager

    def get_driver(self):
        if self.manager.driver_instance.driver is None:
            self.manager.driver_instance.get_driver_instance()
        return self.manager.driver_instance.driver

    @allure.step('Открыть главную страницу')
    def open_main_page(self, main_page):
        title = self.get_driver().title
        if main_page not in title:
            self.get_driver().get(main_page)

    @allure.step('click')
    def click(self, locator):
        self.find_element(locator).click()

    @allure.step('send_keys')
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('clear_and_send_keys_by_xpath')
    def clear_and_send_keys(self, locator, text):
        self.clear(locator)
        self.find_element(locator).send_keys(text)

    def get_tag_text(self, locator):
        text = self.find_element(locator).text
        return text

    def get_tag_attribute(self, locator, attribute_name):
        return self.find_element(locator).get_attribute(attribute_name)

    def scroll_to_element(self, locator):
        try:
            temp = self.find_element(locator).location_once_scrolled_into_view
            self.get_driver().execute_script("window.scrollBy(" + str(temp['x']) + ", " + str(temp['y']) + ")")
        except StaleElementReferenceException as e:
            self.allure_element_not_visible_exception(e)

    @allure.step("move_to_element")
    def move_to_element(self, locator):
        actions = ActionChains(self.get_driver())
        element = self.find_element(locator)
        actions.move_to_element(element)
        actions.perform()

    @allure.step('Очистка текстового поля')
    def clear(self, locator):
        try:
            self.find_element(locator).clear()
        except ElementNotVisibleException as e:
            self.allure_element_not_visible_exception(e)
        except NoSuchElementException as e:
            self.allure_no_such_element_exception(e)

    def get_current_url(self):
        return self.get_driver().current_url

    @allure.step('Нажатие правой кнопкой мыши')
    def right_click(self, locator):
        try:
            self.scroll_to_element(locator)
            action_chains = ActionChains(self.get_driver())
            action_chains.context_click(self.find_element(locator)).perform()
        except ElementNotVisibleException as e:
            self.allure_element_not_visible_exception(e)
        except NoSuchElementException as e:
            self.allure_no_such_element_exception(e)

    @allure.step('refresh_page')
    def refresh_the_page(self):
        self.get_driver().refresh()

    @allure.step('screenshot')
    def allure_screenshot(self, driver):
        try:
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except Exception as e:
            self.allure_exception(e)

    @allure.step("select_element_by_visible_text:")
    def select_element_by_visible_text(self, select_locator, text):
        select = Select(self.find_element(select_locator))
        select.select_by_visible_text(text)

    @allure.step('switch_to_window_in_browser')
    def switch_to_window_in_browser(self, i=None):
        windows_list = self.get_driver().window_handles
        if i is None:
            i = len(windows_list) - 1
            self.get_driver().switch_to.window(windows_list[i])
        else:
            self.get_driver().switch_to.window(windows_list[i])

    # остановщик теста при ошибке
    @allure.step('ElementNotVisibleException')
    def allure_element_not_visible_exception(self, exeption_text):
        assert False

    # остановщик теста при ошибке
    @allure.step('NoSuchElementException')
    def allure_no_such_element_exception(self, exeption_text):
        assert False

    # остановщик теста при ошибке
    @allure.step('Exception')
    def allure_exception(self, Exception):
        assert False

    def find_element(self, locator):
        return WebDriverWait(self.get_driver(), self.time_element_Wait).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.get_driver(), self.time_element_Wait).until(EC.presence_of_all_elements_located(locator))
