import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--verbose")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield
    driver.quit()
@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)



