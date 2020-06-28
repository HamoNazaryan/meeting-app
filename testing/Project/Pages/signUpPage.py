from testing.Project.Locators.locatorsSignUpPage import LocatorsSignUpPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SignUpPage:
    def __init__(self, driver):
        self.driver = driver

        self.signup_title_selector = LocatorsSignUpPage.signup_title_selector
        self.body_selector = LocatorsSignUpPage.body_selector
        self.fname_id = LocatorsSignUpPage.fname_id
        self.lname_id = LocatorsSignUpPage.lname_id
        self.email_id = LocatorsSignUpPage.email_id
        self.password_id = LocatorsSignUpPage.password_id
        self.confirm_password_id = LocatorsSignUpPage.confirm_password_id
        self.signup_button_id = LocatorsSignUpPage.signup_button_id
        self.have_account_block_selector = LocatorsSignUpPage.have_account_block_selector
        self.signin_selector = LocatorsSignUpPage.signin_selector
        self.char_counter_selector = LocatorsSignUpPage.char_counter_selector
        self.error_fields_selector = LocatorsSignUpPage.error_fields_selector

    def title_text(self):
        return self.driver.find_element_by_css_selector(self.signup_title_selector).text

    def have_an_account_block_text(self):
        return self.driver.find_element_by_css_selector(self.have_account_block_selector).text

    def signin_text(self):
        return self.driver.find_element_by_css_selector(self.signin_selector).text

    def enter_fname(self, fname):
        self.driver.find_element_by_id(self.fname_id).clear()
        self.driver.find_element_by_id(self.fname_id).send_keys(fname)

    def enter_lname(self, lname):
        self.driver.find_element_by_id(self.lname_id).clear()
        self.driver.find_element_by_id(self.lname_id).send_keys(lname)

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_id).clear()
        self.driver.find_element_by_id(self.email_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def enter_confirm_password(self, current_password):
        self.driver.find_element_by_id(self.confirm_password_id).clear()
        self.driver.find_element_by_id(self.confirm_password_id).send_keys(current_password)

    def signup_click(self):
        self.driver.find_element_by_id(self.signup_button_id).click()

    def field_value(self, field_id):
        return self.driver.find_element_by_id(field_id).get_attribute("value")

    def counter_val(self, field_id):
        return self.driver.find_element_by_css_selector("#" + field_id + self.char_counter_selector).text

    def blank_click(self):
        self.driver.find_element_by_css_selector(self.body_selector).click()

    def error_value(self, field):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ("#" + field + self.error_fields_selector))))
        return element.get_attribute("data-error")
