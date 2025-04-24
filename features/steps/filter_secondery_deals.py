from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait


@given  ('Open the main page')
def open_main_page(context):
    context.driver.get('https://soft.reelly.io')

@when('Log in to the page')
def login(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,  "#email-2")))

    # Fill in the username and password
    context.driver.find_element(By.CSS_SELECTOR,  "#email-2").send_keys("Test@gmail.com")
    context.driver.find_element(By.CSS_SELECTOR, "#field").send_keys("********")

    # Click the login button
    context.driver.find_element(By.CSS_SELECTOR, ".login-button.w-button").click()

   # context.driver.find_element(By.XPATH, "// div[ @class ='g-menu-logo-name']")

@when('Click on the “Secondary” option on the left side menu')
def secondary_option_on_left_side_menu(context):
    context.driver.find_element(By.XPATH, "//div[normalize-space()='Secondary']").click()

@then('Verify that the right page opens')
def verify_right_page_opens(context):
   context.driver.find_element(By.XPATH, "//div[@class='verified-section']")
   sleep(1)

@when('Click on Filters')
def click_filters(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//img[@class='top-bar-icon']"))
    ).click()

@when('Filter the products by “want to buy')
def buy_filter(context):
    context.driver.find_element(By.XPATH, "//div[contains(text(),'Want to buy')]")

@when('Click on Apply Filter')
def apply_filter(context):
    context.driver.find_element(By.XPATH, "//a[normalize-space()='Apply filter']").click()

@then('Verify all cards have a “Want to buy” tag')
def all_want_buy_filter(context):
    tags = context.driver.find_elements(By.XPATH, "//div[@wized='saleTagMLS' and contains(text(), 'Want to buy')]")
    for tag in tags:
        print(tag.text)
        print(f"Found {len(tags)} 'Want to buy' tags") #Check how many such elements are found: