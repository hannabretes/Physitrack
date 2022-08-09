from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class MainPageLocators(object):
    LOGIN = (By.CLASS_NAME, 'button button-small w-button')
    COUNTRY_USA = (By.CSS_SELECTOR, '#country_us')
    SELECT_COUNTRY = (By.CLASS_NAME, 'btn-link pad-top choose-server')
    BACK_TO_DEMO_BUTTON = (By.CLASS_NAME,'link-back-to-demo')
    BIRD_DOG_EXERCISE = (By.XPATH, '//span[contains(text(),"Bird dog" Core/abdominal stabilization; 01)]')
    ADD_TO_CARD_BUTTON = (By.CLASS_NAME, 'cart w-inline-block btn-link-icon pad-left')
    ASSIGN_PROGRAM = (By.ID, 'assign-program-modal-button')
    SELECT_PROGRAM = (By.CLASS_NAME, 'react-select__value-container css-1hwfws3')
    SELECT_USER = (By.XPATH, '//span[@class="ladda-label"]')