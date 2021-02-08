from FW.WEB.AnyPage import AnyPage
from FW.WEB.Images.Images import Images
from FW.WEB.Images.Search.ImagesSearch import ImagesSearch
from FW.WEB.MainPage import MainPage

from FW.WEB.Search.Search import Search
from FW.WEB.waitingFW import waitingFW
from FW.ExternalApp.work_with_time import work_with_time
from FW.ExternalApp.DriverInstance import DriverInstance
from Data.GroupData import group_data


class ApplicationManager:

    def __init__(self):
        self.group_data = group_data
        self.branch_settings = self.group_data.GLOBAL[self.group_data.branch]
        self.time = work_with_time()
        self.driver_instance = DriverInstance()
        self.waiting = waitingFW(self)

        self.any_page = AnyPage(self)
        self.main_page = MainPage(self)
        self.search = Search(self)
        self.images = Images(self)
        self.images_search = ImagesSearch(self)
