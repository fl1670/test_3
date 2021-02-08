from FW.Application_Manager import ApplicationManager


class TestBase:

    # new  branch

    APP = ApplicationManager()

    def setup_class(self):
        pass

    def teardown_class(self):
        self.APP.driver_instance.stop_test()

    def setup_method(self):
        self.APP.main_page.open_main_page(self.APP.branch_settings['main_page'])

    def teardown_method(self):
        pass
