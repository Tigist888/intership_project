from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page


# pages--package name
# base_page ---file name for class page
# Page class name under base_page
#

class MainPage(Page):
    url = 'https://soft.reelly.io'
    SECONDARY_side_OPTION=(By.XPATH, "//div[contains(text(),'Secondary')]")


    def open_main_page(self):
        self.goto_home(self.url)

    def click_secondary_side(self):

        try:
            # Wait for the element to be visible
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.SECONDARY_side_OPTION)
            )
            print("Element is visible.")

            # Wait for the element to be clickable
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.SECONDARY_side_OPTION)
            ).click()
            print("Clicked on the Secondary side option.")

        except TimeoutException:
            print("Timeout: Element not found or clickable.")