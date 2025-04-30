from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page


class FiltersPage(Page):
    title_more_filter=(By.XPATH,   "//div[@class='h1-filters']")
    want_to_buy_button=(By.XPATH,    "//div[@class='tag-text-filters'][normalize-space()='Want to buy']")
    apple_filter_button =(By.XPATH,    "//a[normalize-space()='Apply filter']")


    def wait_for_more_filter(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TITLE_MORE_FILTER)
        )


    def click_want_to_buy(self):
        self.find_element(*self.want_to_buy_button).click()

    def click_apple_filter(self):
        self.find_element(*self.apple_filter_button).click()