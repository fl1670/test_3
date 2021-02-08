from selenium.webdriver.common.by import By

from FW.WEB.AnyPage import AnyPage


class Locator:
    search = (By.XPATH, '//*[@id="text"]')
    popup_visible = (By.XPATH, "//div[contains(@class, 'mini-suggest__popup_visible')]")
    images = (By.XPATH, "//*[@data-id='images']")

class MainPage(AnyPage):

    def input_text_in_search(self, text):
        self.send_keys(Locator.search, text)
        self.find_element(Locator.popup_visible)
        return self

    def click_element_in_search_popup(self, name=None, index=None):
        if name:
            self.click((Locator.popup_visible[0], Locator.popup_visible[1] + f'//li[@data-text="{name}"]'))
            return self.manager.search
        elif index:
            self.click((Locator.popup_visible[0], Locator.popup_visible[1] + f'//li[@data-index="{index-1}"]'))
            return self.manager.search

    def get_text_in_search_popup(self, index_element):
        return self.get_tag_attribute((Locator.popup_visible[0], Locator.popup_visible[1] + f'//li[@data-index="{index_element}"]'), 'data-text')

    def click_images(self):
        self.click(Locator.images)
        self.switch_to_window_in_browser()
        return self.manager.images



