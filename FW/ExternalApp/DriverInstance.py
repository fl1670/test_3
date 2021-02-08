from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import FirefoxOptions, ChromeOptions
from Data.GroupData import group_data


class DriverInstance:

    driver = None

    def __init__(self):
        self.group_data = group_data

    def get_driver_instance(self):
        if self.driver is None:
            if self.group_data.GLOBAL['Browser']['Name'] == 'firefox':
                firefox_options = FirefoxOptions()
                firefox_options.add_argument(argument='--width=1920')
                firefox_options.add_argument(argument='--height=1080')
                if self.group_data.GLOBAL['Browser']['headless'] is True:
                    firefox_options.headless = True
                    firefox_options.add_argument("--window-size=1920,1080")

                if self.group_data.GLOBAL['Browser']['Remote'] is True:
                    self.driver = webdriver.Remote(
                        command_executor='http://127.0.0.1:4444/wd/hub',
                        options=firefox_options,
                        desired_capabilities=DesiredCapabilities.FIREFOX,
                        browser_profile=None,
                        proxy=None,
                        keep_alive=False,
                        file_detector=None
                    )
                else:
                    self.driver = webdriver.Firefox(options=firefox_options, desired_capabilities=DesiredCapabilities.FIREFOX)

                self.driver = webdriver.Remote(
                    command_executor='http://127.0.0.1:4444/wd/hub',
                    desired_capabilities=DesiredCapabilities.FIREFOX,
                    options=firefox_options,
                )

            if self.group_data.GLOBAL['Browser']['Name'] == 'chrome':
                # Chrome browser options
                options = ChromeOptions()
                options.set_capability("acceptInsecureCerts", True)
                if self.group_data.GLOBAL['Browser']['headless'] is True:
                    options.headless = True
                    options.add_argument(argument='--width=1920')
                    options.add_argument(argument='--height=1080')
                    options.add_argument("--window-size=1920,1080")

                    # chrome_options.add_argument('--ignore-certificate-errors')
                else:
                    options.headless = False

                capabilities = DesiredCapabilities.CHROME
                capabilities['goog:loggingPrefs'] = {'browser': 'ALL',
                                                     'performance': 'ALL',
                                                     'server': 'ALL',
                                                     'client': 'ALL'}

                if self.group_data.GLOBAL['Browser']['Remote'] is True:
                    self.driver = webdriver.Remote(
                        command_executor='http://127.0.0.1:4444/wd/hub',
                        proxy=None,
                        options=options,
                        desired_capabilities=capabilities,
                    )
                else:
                    self.driver = webdriver.Chrome(options=options, desired_capabilities=capabilities)
            if self.group_data.GLOBAL['Browser']['headless'] is False:
                self.driver.maximize_window()
        return self.driver

    def stop_test(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
