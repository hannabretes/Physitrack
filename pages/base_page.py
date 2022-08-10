from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# this Base class is serving basic attributes for every single page inherited from Page class
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, url):
        self.driver.get(url)

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()