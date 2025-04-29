from pages.base_page import Page
from pages.main_page import MainPage
from  pages.secondary_page import SecondaryPage
from pages.filters_page import FiltersPage
from pages.login_page import LoginPage



class Application:
    def __init__(self, driver):
        self.driver = driver

        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.secondary_page = SecondaryPage(driver)
        self.filters_page = FiltersPage(driver)
        self.login_page = LoginPage(driver)