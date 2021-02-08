import allure
from selenium.webdriver.common.by import By

from FW.WEB.AnyPage import AnyPage


class Locator:
    button_next = (By.XPATH, '//div[contains(@class, "CircleButton_type_next ")]')
    button_prev = (By.XPATH, '//div[contains(@class, "CircleButton_type_prev ")]')
    image_preview = (By.XPATH, '//img[contains(@class, "MMImage-Preview")]')


class ImagesSearch(AnyPage):

    @allure.step('click images list item ({index})')
    def click_image_by_index(self, index):
        by = By.XPATH
        locator = f'(//div[contains(@class, "serp-item__preview")])[{index}]'
        self.click((by, locator))
        return self

    @allure.step('click button next')
    def click_button_next(self):
        self.click(Locator.button_next)
        return self

    @allure.step('click button prev')
    def click_button_prev(self):
        self.click(Locator.button_prev)
        return self

    @allure.step('get image href')
    def get_image_href(self):
        return self.get_tag_attribute(Locator.image_preview, "src")


