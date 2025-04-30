from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from app.appilication import Application
import os

def browser_init(context):
    """
    Initialize browser locally or on BrowserStack based on environment variable.
    """
    use_browserstack = os.getenv("BROWSERSTACK", "false").lower() == "true"
    browser_choice = os.getenv("BROWSER", "firefox").lower()

    if use_browserstack:
        # BrowserStack credentials
        USERNAME = os.getenv("BROWSERSTACK_USERNAME")
        ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

        desired_cap = {
            'browser': 'Safari',
            'os': 'OS X',
            'os_version': 'Ventura',  # or another macOS version supported
            'name': 'Behave test on macOS Safari',
            'build': 'BrowserStack macOS run',
            'browserstack.debug': True
        }

        # desired_cap = {
        #     'browser': browser_choice.capitalize(),
        #     'os': 'Windows',
        #     'os_version': '10',
        #     'name': 'Behave Test',  # Test name
        #     'build': 'BrowserStack Build',  # Grouping tests
        #     'browserstack.debug': True,
        # }

        url = f"http://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"
        context.driver = webdriver.Remote(command_executor=url, desired_capabilities=desired_cap)
        print(f"Running on BrowserStack with {browser_choice.capitalize()}")

    else:
        if browser_choice == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--headless")  # Optional
            chrome_options.add_argument("--window-size=1920,1080")
            service = ChromeService(ChromeDriverManager().install())
            context.driver = webdriver.Chrome(service=service, options=chrome_options)
            print("Using Chrome browser in HEADLESS mode.")

        elif browser_choice == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.headless = True  # Optional
            firefox_options.add_argument("--window-size=1920,1080")
            service = FirefoxService(GeckoDriverManager().install())
            context.driver = webdriver.Firefox(service=service, options=firefox_options)
            print("Using Firefox browser in NON-HEADLESS mode.")

        else:
            raise ValueError(f"Unsupported browser: {browser_choice}")
    try:
        context.driver.maximize_window()
    except Exception as e:
        print(f"Could not maximize window: {e}")
        context.driver.set_window_size(1920, 1080)
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    context.driver.quit()