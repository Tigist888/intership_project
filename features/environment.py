from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from app.appilication import Application



def browser_init(context):
    """
    :param context: Behave context
    """
    browser_choice = "firefox"  # Change this to 'chrome' if you want to use Chrome

    if browser_choice == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode (optional)
        chrome_options.add_argument("--window-size=1920,1080")
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)
        context.driver = webdriver.Chrome(service=service, options=chrome_options)
        print("Using Chrome browser in HEADLESS mode.")  # Print message for Chrome


    elif browser_choice == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.headless = False  # Set to False for non-headless mode
        firefox_options.add_argument("--window-size=1920,1080")
        driver_path = GeckoDriverManager().install()
        service = FirefoxService(driver_path)
        context.driver = webdriver.Firefox(service=service, options=firefox_options)

        print("Using Firefox browser in NON-HEADLESS mode.")  # Print message for Firefox
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app=Application(context.driver)


#
# driver_path = ChromeDriverManager().install()
#     service = Service(driver_path)
#     context.driver = webdriver.Chrome(service=service)
#
#     context.driver.maximize_window()
#     context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
