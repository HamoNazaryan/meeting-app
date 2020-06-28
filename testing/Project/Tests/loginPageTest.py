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
        driver = self.driver
        driver.get("http://127.0.0.1:5000")

    def tearDown(self):
        time.sleep(2)

    def test_01_check_elements(self):
        login = LoginPage(self.driver)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, login.login_title_selector)))
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, login.username_textbox_id)))
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, login.password_textbox_id)))
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, login.login_button_id)))
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, login.remember_id)))
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, login.account_need_selector)))
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, login.forgot_block_selector)))
        forgot_text = login.forgot_text()
        self.assertEqual(forgot_text, "Forgot Password?")
        need_account_text = login.need_an_account_text()
        self.assertEqual(need_account_text, "Need An Account? Sign Up")
        signup_text = login.signup_text()
        self.assertEqual(signup_text, "Sign Up")

    def test_02_check_title(self):
        login = LoginPage(self.driver)
        msg = login.title_text()
        self.assertEqual(msg, "Welcome Back!")

    def test_03_login_valid(self):
        login = LoginPage(self.driver)
        login.enter_username("gagik@yopmail.com")
        login.enter_password("Gagikyan555")
        login.click_login()

        home = HomePage(self.driver)
        home.click_menu()
        home.click_logout()

    def test_04_login_invalid_username(self):
        login = LoginPage(self.driver)
        login.enter_username("gagik7@yopmail.com")
        login.enter_password("Gagikyan555")
        login.click_login()
        msg = login.invalid_username_message()
        self.assertEqual(msg, "Login unsuccessful, please check email and password !")

    def test_05_login_invalid_password(self):
        login = LoginPage(self.driver)
        login.enter_username("gagik@yopmail.com")
        login.enter_password("Gagikyan5558")
        login.click_login()
        msg = login.invalid_password_message()
        self.assertEqual(msg, "Login unsuccessful, please check email and password !")

    def test_06_login_empty_username(self):
        login = LoginPage(self.driver)
        login.enter_username("gagik@yopmail.com")
        login.click_login()
        url = login.current_url()
        self.assertEqual(url, "http://127.0.0.1:5000/login")


    def test_07_login_empty_password(self):
        login = LoginPage(self.driver)
        login.enter_password("Gagikyan555")
        login.click_login()
        url = login.current_url()
        self.assertEqual(url, "http://127.0.0.1:5000/login")


    def test_08_check_email_error_field_content(self):
        login = LoginPage(self.driver)
        login.enter_username("")
        login.blank_click()
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, login.email_error_text_selector)))
        element = element.get_attribute("data-error")
        self.assertEqual(element, 'Invalid email address.')

    def test_09_check_password_error_field_content(self):
        login = LoginPage(self.driver)
        login.enter_password("")
        login.blank_click()
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, login.password_error_text_selector)))
        element = element.get_attribute("data-error")
        self.assertEqual(element, 'Field must be between 6 and 60 characters long.')

    def test_10_password_size_less_zan_6(self):
        login = LoginPage(self.driver)
        login.enter_username("gagik@yopmail.com")
        n = random.randint(1, 5)
        chars = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=n))
        login.enter_password(chars)
        login.click_login()
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, login.password_error_text_selector)))
        element = element.get_attribute("data-error")
        self.assertEqual(element, 'Field must be between 6 and 60 characters long.')

    def test_11_not_correct_email(self):
        login = LoginPage(self.driver)
        # login.enter_username("ex.abc@cba")
        login.enter_username(self.makeIncorrectEmail())
        login.enter_password("Gagikyan555")
        login.click_login()
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, login.email_error_text_selector)))
        element = element.get_attribute("data-error")
        self.assertEqual(element, 'Invalid email address.')

    def test_12_password_no_more_than_60_characters(self):
        login = LoginPage(self.driver)
        login.enter_username("gagik@yopmail.com")
        n = random.randint(61, 70)
        chars = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=n))
        login.enter_password(chars)
        pass_val = login.password_input_value()
        self.assertEqual(len(pass_val), 60)

    def test_13_open_signup_page(self):
        login = LoginPage(self.driver)
        login.signup_link_click()
        url = login.current_url()
        self.assertEqual(url, "http://127.0.0.1:5000/signup")

    def test_14_open_forgot_page(self):
        login = LoginPage(self.driver)
        login.forgot_link_click()
        url = login.current_url()
        self.assertEqual(url, "http://127.0.0.1:5000/reset_password")

    # def test_15_check_remember_me(self):
    #     login = LoginPage(self.driver)
    #     login.enter_username("gagik@yopmail.com")
    #     login.enter_password("Gagikyan555")
    #     login.remember_block_click()
    #     login.click_login()
    #     self.driver.close()
    #     # self.driver.quit()
    #     BaseConfig.setUpClass()
    #     driver = self.driver
    #     BaseConfig.driver.get("http://127.0.0.1:5000")

#
# if __name__ == "__main__":
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=htmlOutPutUrl))




if __name__ == "__main__":
    unittest.main()