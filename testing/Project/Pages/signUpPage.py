from testing.Project.Locators.locatorsSignUpPage import LocatorsSignUpPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class SignUpPage(LocatorsSignUpPage):

    def __init__(self, driver):
        self.driver = driver


    def title_text(self):
        return self.driver.find_element_by_css_selector(self.signup_title_selector).text

    def have_an_account_block_text(self):
        return self.driver.find_element_by_css_selector(self.have_account_block_selector).text

    def signin_text(self):
        return self.driver.find_element_by_css_selector(self.signin_selector).text

    def enter_text(self, input_id, text):
        self.driver.find_element_by_id(input_id).clear()
        self.driver.find_element_by_id(input_id).send_keys(text)

    def signup_click(self):
        self.driver.find_element_by_id(self.signup_button_id).click()

    def field_value(self, field_id):
        return self.driver.find_element_by_id(field_id).get_attribute("value")

    def counter_val(self, field_id):
        return self.driver.find_element_by_css_selector("#" + field_id + self.char_counter_selector).text

    def blank_click(self):
        self.driver.find_element_by_css_selector(self.signup_title_selector).click()

    def error_value(self, field):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ("#" + field + self.error_fields_selector))))
        return element.get_attribute("data-error")

    def current_url(self):
        return self.driver.current_url
