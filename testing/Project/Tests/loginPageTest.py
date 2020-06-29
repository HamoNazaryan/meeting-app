import time
import unittest
import HtmlTestRunner
from testing.Project.Pages.loginPage import LoginPage
from testing. Project.Pages.homePage import HomePage
from testing.config import BaseConfig, htmlOutPutUrl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

class LoginTest(BaseConfig):
    def setUp(self):
        self.page = LoginPage(self.driver)
        self.driver.get("http://127.0.0.1:5000")

    def tearDown(self):
        time.sleep(2)

    def test_01_check_elements(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.page.login_title_selector)))
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, self.page.username_textbox_id)))
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, self.page.password_textbox_id)))
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, self.page.login_button_id)))
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, self.page.remember_id)))
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.page.need_account_selector)))
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, self.page.forgot_block_selector)))
        forgot_text = self.page.forgot_text()
        self.assertEqual(forgot_text, "Forgot Password?")
        need_account_text = self.page.need_an_account_text()
        self.assertEqual(need_account_text, "Need An Account? Sign Up")
        signup_text = self.page.signup_text()
        self.assertEqual(signup_text, "Sign Up")

    def test_02_check_title(self):
        msg = self.page.title_text()
        self.assertEqual(msg, "Welcome Back!")

    def test_03_login_valid(self):
        self.page.enter_username("gagik@yopmail.com")
        self.page.enter_password("Gagikyan555")
        self.page.click_login()

        home = HomePage(self.driver)
        home.click_menu()
        home.click_logout()

    def test_04_login_invalid_username(self):
        self.page.enter_username("gagik7@yopmail.com")
        self.page.enter_password("Gagikyan555")
        self.page.click_login()
        msg = self.page.invalid_username_message()
        self.assertEqual(msg, "Login unsuccessful, please check email and password !")

    def test_05_login_invalid_password(self):
        self.page.enter_username("gagik@yopmail.com")
        self.page.enter_password("Gagikyan5558")
        self.page.click_login()
        msg = self.page.invalid_password_message()
        self.assertEqual(msg, "Login unsuccessful, please check email and password !")

    def test_06_login_empty_username(self):
        self.page.enter_username("gagik@yopmail.com")
        self.page.click_login()
        url = self.page.current_url()
        self.assertEqual(url, "http://127.0.0.1:5000/login")


    def test_07_login_empty_password(self):
        self.page.enter_password("Gagikyan555")
        self.page.click_login()
        url = self.page.current_url()
        self.assertEqual(url, "http://127.0.0.1:5000/login")


    def test_08_check_email_error_field_content(self):
        self.page.enter_username("")
        self.page.blank_click()
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.page.email_error_text_selector)))
        element = element.get_attribute("data-error")
        self.assertEqual(element, 'Invalid email address.')

    def test_09_check_password_error_field_content(self):
        self.page.enter_password("")
        self.page.blank_click()
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.page.password_error_text_selector)))
        element = element.get_attribute("data-error")
        self.assertEqual(element, 'Field must be between 6 and 60 characters long.')

    def test_10_password_size_less_zan_6(self):
        self.page.enter_username("gagik@yopmail.com")
        n = random.randint(1, 5)
        chars = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=n))
        self.page.enter_password(chars)
        self.page.click_login()
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.page.password_error_text_selector)))
        element = element.get_attribute("data-error")
        self.assertEqual(element, 'Field must be between 6 and 60 characters long.')

    def test_11_not_correct_email(self):
        # self.page.enter_username("ex.abc@cba")
        self.page.enter_username(self.makeIncorrectEmail())
        self.page.enter_password("Gagikyan555")
        self.page.click_login()
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.page.email_error_text_selector)))
        element = element.get_attribute("data-error")
        self.assertEqual(element, 'Invalid email address.')

    def test_12_password_no_more_than_60_characters(self):
        self.page.enter_username("gagik@yopmail.com")
        n = random.randint(61, 70)
        chars = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=n))
        self.page.enter_password(chars)
        pass_val = self.page.password_input_value()
        self.assertEqual(len(pass_val), 60)

    def test_13_open_signup_page(self):
        self.page.signup_link_click()
        url = self.page.current_url()
        self.assertEqual(url, "http://127.0.0.1:5000/signup")

    def test_14_open_forgot_page(self):
        self.page.forgot_link_click()
        url = self.page.current_url()
        self.assertEqual(url, "http://127.0.0.1:5000/reset_password")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=htmlOutPutUrl))


#
#
# if __name__ == "__main__":
#     unittest.main()