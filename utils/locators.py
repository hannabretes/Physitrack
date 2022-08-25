from selenium.webdriver.common.by import By

class MainPageLocators(object):
    BACK_TO_DEMO_BUTTON = (By.CLASS_NAME,'link-back-to-demo')
    BIRD_DOG_EXERCISE = (By.XPATH, '/html/body/div[8]/div[1]/div/div[2]/div[2]/div[1]/div[2]/a/span/span')
    CLOSE_POPUP = (By.XPATH,'//div[contains(@class, "current")]//a[@rel="modal:close"]')
    ADD_TO_CARD_BUTTON = (By.CLASS_NAME, 'cart w-inline-block btn-link-icon pad-left')
    ASSIGN_PROGRAM = (By.ID, 'assign-program-modal-button')
    SELECT_PROGRAM = (By.CLASS_NAME, 'react-select__value-container css-1hwfws3')
    SELECT_USER = (By.XPATH, '//span[@class="ladda-label"]')