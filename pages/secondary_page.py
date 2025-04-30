from time import sleep

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page


class SecondaryPage(Page):

    verify_open_secondary_page=(By.XPATH, "//div[@class='g-menu-text' and text()='Secondary']")
    secondary_button=(By.XPATH, "//div[@class='g-menu-text' and text()='Secondary']")
    filter_button=(By.XPATH, "//div[@class='filter-button']")
    all_want_to_buy_tag=(By.XPATH, "//div[@wized='saleTagMLS' and contains(text(), 'Want to buy')]")


    def click_secondary_button(self):
        try:
            # Wait until the "Secondary" button is clickable
            secondary_button_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.secondary_button)
            )
            secondary_button_element.click()
            print("Clicked on the 'Secondary' button.")
        except TimeoutException:
            print(f"Timeout occurred while waiting for the Secondary button to be clickable.")
        except Exception as e:
            print(f"An error occurred while clicking the Secondary button: {str(e)}")

    def verify_partial_url(self, expected_url_part):
        """
        Verifies if the current URL contains the expected URL part (partial match).
        """
        assert expected_url_part in self.driver.current_url, f"URL does not contain '{expected_url_part}'"
        print(f"Page URL contains the expected part: {expected_url_part}")

    def verify_secondary_page_opened(self):
        # Verify the URL contains "secondary-listings"
        self.verify_partial_url("secondary-listings")

        # Wait until the secondary page is loaded and the element is visible
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self. verify_open_secondary_page)
        )

        # Assert the element is displayed
        assert element.is_displayed(), "Secondary page not opened"
        print("Secondary page is opened.")

    def click_filter_button(self):
        self.driver.find_element(*self.filter_button).click()

    def want_to_buy_tag(self):
       tags= self.driver.find_elements(*self.all_want_to_buy_tag)
       for tag in tags:
           assert "Want to buy" in tag.text, f"Unexpected tag found: {tag.text}"



