import selenium
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
import time


@given('Open the main page')
def main_page(context):
    context.app.main_page.open_main_page()


@when('Log in to the page')
def login(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,  "#email-2")))

    # Fill in the username and password
    context.app.login_page.enter_username('test@gmail.com')
    context.app.login_page.enter_password("*******")

    # Click the login button
    context.app.login_page.click_login()


@when('Click on the “Secondary” option on the left side menu')
def secondary_option_on_left_side_menu(context):
   context.app.main_page.click_secondary_side()

@then('Verify that the right page opened')
def verify_right_page_opens(context):
   context.app.secondary_page.verify_right_page_opened()

@when('Click on Filters')
def click_filters(context):
   context.app.secondary_page.click_filter_button()

@when('Filter the products by “want to buy"')
def filter_text(context):
    context.APP.filters_page.click_want_to_buy()


@when('Click on Apply Filter')
def apply_filter(context):
    context.app.filters_page.click_apply_filter()

@then( 'Verify all cards have a “Want to buy” tag')
def verify_all_tags(context):
    context.app.secondary_page.want_to_buy_tag()


