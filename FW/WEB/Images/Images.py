import allure
from selenium.webdriver.common.by import By

from FW.WEB.AnyPage import AnyPage


class Locator:
    search_result = (By.XPATH, '//*[@id="search-result"]')


class Images(AnyPage):

    @allure.step('click images list item ({index})')
    def click_images_list_item(self, index=1):
        by = By.XPATH
        locator = f'(//*[@class="PopularRequestList"]//*[@data-grid-text])[{index}]'
        self.click((by, locator))
        return self.manager.images_search



