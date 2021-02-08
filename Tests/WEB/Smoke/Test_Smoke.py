import allure
from Tests.TestBase import TestBase


@allure.feature('Web')
@allure.story('Smoke tests')
class TestSmoke(TestBase):

    @allure.title('Тест 1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('https://yandex.ru/')
    def test_01_smoke(self):
        search_text = 'perfect art'

        main_page = self.APP.main_page
        main_page.input_text_in_search(search_text)

        assert search_text == main_page.get_text_in_search_popup(0)

        main_page.click_element_in_search_popup(index=1)

        search_page = self.APP.search
        search_page.click_element_by_index(1)
        current_url = search_page.get_current_url()
        assert 'https://perfectart.ru/' == current_url

    @allure.title('Тест 2')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('https://yandex.ru/')
    def test_02_smoke(self):
        main_page = self.APP.main_page
        images_page = main_page.click_images()
        images_search_page = images_page.click_images_list_item()

        images_search_page.click_image_by_index(2)
        image_href_1 = images_search_page.get_image_href()
        images_search_page.click_button_next()
        image_href_2 = images_search_page.get_image_href()
        assert image_href_1 != image_href_2

        images_search_page.click_button_prev()
        image_href_new = images_search_page.get_image_href()
        assert image_href_new == image_href_1
