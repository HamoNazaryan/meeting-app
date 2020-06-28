from testing.Project.Locators.locatorsLogin import LocatorsLogin

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = LocatorsLogin.username_textbox_id
        self.password_textbox_id = LocatorsLogin.password_textbox_id
        self.login_button_id = LocatorsLogin.login_button_id
        self.flash_message_selector = LocatorsLogin.flash_message_selector
        self.login_title_selector = LocatorsLogin.login_title_selector
        self.remember_id = LocatorsLogin.remember_id
        self.forgot_block_selector = LocatorsLogin.forgot_block_selector
        self.account_need_selector = LocatorsLogin.need_account_selector
        self.email_error_text_selector = LocatorsLogin.email_error_text_selector
        self.body_selector = LocatorsLogin.body_selector
        self.password_error_text_selector = LocatorsLogin.password_error_text_selector
        self.signup_link_selector = LocatorsLogin.signup_link_selector
        self.forgot_password_link_selector = LocatorsLogin.forgot_password_link_selector

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def invalid_username_message(self):
        msg = self.driver.find_element_by_css_selector(self.flash_message_selector).text
        return msg

    def invalid_password_message(self):
        msg = self.driver.find_element_by_css_selector(self.flash_message_selector).text
        return msg

    def title_text(self):
        msg = self.driver.find_element_by_css_selector(self.login_title_selector).text
        return msg

    def current_url(self):
        return self.driver.current_url

    def blank_click(self):
        self.driver.find_element_by_css_selector(self.body_selector).click()

    def password_input_value(self):
        return self.driver.find_element_by_id(self.password_textbox_id).get_attribute("value")

    def signup_link_click(self):
        self.driver.find_element_by_css_selector(self.signup_link_selector).click()

    def forgot_link_click(self):
        self.driver.find_element_by_css_selector(self.forgot_password_link_selector).click()

    def remember_block_click(self):
        self.driver.find_element_by_id(self.remember_id).click()

    def forgot_text(self):
        return self.driver.find_element_by_css_selector(self.forgot_password_link_selector).text

    def need_an_account_text(self):
        return self.driver.find_element_by_css_selector(self.account_need_selector).text

    def signup_text(self):
        return self.driver.find_element_by_css_selector(self.signup_link_selector).text