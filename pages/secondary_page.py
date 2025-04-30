from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page


class SecondaryPage(Page):

    open_secondary_page= (By.XPATH, "//div[@class='page-title listing' and text()='Listings']")
    filter_button=(By.XPATH, "//div[@class='filter-button']")
    all_want_to_buy_tag=(By.XPATH, "//div[@wized='saleTagMLS' and contains(text(), 'Want to buy')]")

    def verify_secondary_page_opened(self):
        element=self.driver.find_element(*self.open_secondary_page)
        assert element.is_displayed(),"secondary page not opened"
        sleep(3)


    def click_filter_button(self):
        self.driver.find_element(*self.filter_button).click()

    def want_to_buy_tag(self):
       tags= self.driver.find_elements(*self.all_want_to_buy_tag)
       for tag in tags:
           assert "Want to buy" in tag.text, f"Unexpected tag found: {tag.text}"



