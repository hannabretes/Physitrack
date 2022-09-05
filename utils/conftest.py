import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.select_country_page import SelectCountryPage
from pages.add_program_page import AddProgramPage
@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--verbose")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
@pytest.fixture
def login_page(driver):
    return LoginPage(driver)
@pytest.fixture()
def select_country_page(driver):
    return SelectCountryPage(driver)
@pytest.fixture()
def add_program_page(driver):
    return AddProgramPage(driver)
