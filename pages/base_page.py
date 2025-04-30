class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def goto_home(self,url):
        self.driver.get(url)

    def find_element(self,*locator):
        return self.driver.find_element(*locator)

    def find_elements(self,*locator):
        return self.driver.find_elements(*locator)

    def click(self,*locator):
        self.driver.find_element(*locator).click()

    def input_text(self,text,*locator):
       self.driver.find_element(*locator).send_keys(text)

