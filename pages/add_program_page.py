from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
class AddProgramPage(BasePage):
    close_popup = (By.XPATH, '//div[contains(@class, "current")]//a[@rel="modal:close"]')
    add_to_card_button = (By.XPATH, '//div[@class="w-inline-block inline-margin-fix"]')
    assign_program = (By.ID, 'assign-program-modal-button')
    select_program = (By.CLASS_NAME, 'react-select__value-container css-1hwfws3')
    select_user = (By.XPATH, '//span[@class="ladda-label"]')
    bird_dog_button = (By.XPATH, '/html/body/div[8]/div[1]/div/div[2]/div[2]/div[1]/div[2]/a/span/span')
    def __init__(self, driver):
        super(AddProgramPage, self).__init__(driver)
    def add_to_card(self):
        page = BasePage(self.driver)
        self.do_click(self.bird_dog_button)
        self.do_click(self.add_to_card_button)