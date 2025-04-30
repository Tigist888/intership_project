from selenium.webdriver.common.by import By

from pages.base_page import Page

class LoginPage(Page):


    USERNAME_INPUT=(By.CSS_SELECTOR, "#email-2")
    PASSWORD_INPUT=(By.CSS_SELECTOR, "#field")
    LOGIN_BUTTON=(By.CSS_SELECTOR, ".login-button.w-button")


    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()



