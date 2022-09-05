from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
# this Base class is serving basic attributes for every single page inherited from Page class
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
    def open(self, url):
        self.driver.get(url)

    def do_click(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def do_send_keys(self, locator, text):
        self.wait.until(ec.visibility_of_element_located(locator)).send_keys(text)

    def do_clear(self, locator):
        self.wait.until(ec.visibility_of_element_located(locator)).clear()

    def get_text(self, locator):
       return self.wait.until(ec.visibility_of_element_located(locator)).text
