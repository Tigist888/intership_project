import selenium
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
import time


@given('Open the main page')
def open_main_page(context):
    context.driver.get('https://soft.reelly.io')

@when('Log in to the page')
def login(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,  "#email-2")))

    # Fill in the username and password
    context.driver.find_element(By.CSS_SELECTOR,  "#email-2").send_keys("test@gmail.com")
    context.driver.find_element(By.CSS_SELECTOR, "#field").send_keys("*********")

    # Click the login button
    context.driver.find_element(By.CSS_SELECTOR, ".login-button.w-button").click()

   # context.driver.find_element(By.XPATH, "// div[ @class ='g-menu-logo-name']")

@when('Click on the “Secondary” option on the left side menu')
def secondary_option_on_left_side_menu(context):
    # Wait for the element to be clickable

    try:

        # Then wait for 'Secondary' to be clickable
         WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Secondary')]"))
        ).click()

    except Exception as e:
        print(f"Error: {e}")

        # Generate timestamp
        timestamp = time.strftime("%Y%m%d-%H%M%S")

        # Save screenshot with timestamp
        context.driver.save_screenshot(f'secondary_click_error_{timestamp}.png')

        raise


@then('Verify that the right page opened')
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
        try:
            # Refind the element in each iteration to prevent StaleElementReferenceException
            print(tag.text)
        except selenium.common.exceptions.StaleElementReferenceException:
            print("Element became stale, trying again...")
            # Optionally, refind the element if needed
            tag = context.driver.find_element(By.XPATH,  "//div[@wized='saleTagMLS' and contains(text(), 'Want to buy')]")
            print(tag.text)