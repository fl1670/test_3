import allure
from selenium.webdriver.common.by import By

from FW.WEB.AnyPage import AnyPage


class Locator:
    search_result = (By.XPATH, '//*[@id="search-result"]')
    popup_visible = (By.XPATH, "//div[contains(@class, 'mini-suggest__popup_visible')]")


class Search(AnyPage):

    @allure.step('click element by index ({index})')
    def click_element_by_index(self, index):
        locator = f'({Locator.search_result[1]}//h2/a[@href])[{index}]'
        self.click((Locator.search_result[0], locator))
        self.switch_to_window_in_browser(1)
        return self
