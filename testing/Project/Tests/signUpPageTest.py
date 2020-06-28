import time
import unittest
from testing.Project.Pages.signUpPage import SignUpPage
from testing. Project.Pages.homePage import HomePage
from testing.config import BaseConfig, htmlOutPutUrl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
from parameterized import parameterized

class SignUpTest(BaseConfig, SignUpPage):
    def setUp(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/signup")

    def tearDown(self):
        time.sleep(2)

    # def test_01_check_elements(self):
    #     signup =SignUpPage(self.driver)
    #     WebDriverWait(self.driver, 5).until(
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, signup.signup_title_selector)))
    #     WebDriverWait(self.driver, 5).until(
    #         EC.visibility_of_element_located((By.ID, signup.fname_id)))
    #     WebDriverWait(self.driver, 5).until(
    #         EC.visibility_of_element_located((By.ID, signup.lname_id)))
    #     WebDriverWait(self.driver, 5).until(
    #         EC.visibility_of_element_located((By.ID, signup.email_id)))
    #     WebDriverWait(self.driver, 5).until(
    #         EC.visibility_of_element_located((By.ID, signup.password_id)))
    #     WebDriverWait(self.driver, 5).until(
    #         EC.visibility_of_element_located((By.ID, signup.confirm_password_id)))
    #     WebDriverWait(self.driver, 5).until(
    #         EC.visibility_of_element_located((By.ID, signup.signup_button_id)))
    #     WebDriverWait(self.driver, 5).until(
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, signup.have_account_block_selector)))
    #     title = signup.title_text()
    #     self.assertEqual(title, "Sign Up")
    #     have_text = signup.have_an_account_block_text()
    #     self.assertEqual(have_text, "Already Have An Account? Sign In")
    #     signin_text = signup.signin_text()
    #     self.assertEqual(signin_text, "Sign In")
    #
    # def test_02_signup_valid(self):
    #     signup = SignUpPage(self.driver)
    #     signup.enter_fname("Gevorg")
    #     signup.enter_lname("Gasparyan")
    #     signup.enter_email("gevorg@yopmail.com")
    #     signup.enter_password("Gevorg555")
    #     signup.enter_confirm_password("Gevorg555")
    #     signup.signup_click()
    #
    #     home = HomePage(self.driver)
    #     home.click_menu()
    #     home.click_logout()

    def test_03_empty_fname(self):
        signup = SignUpPage(self.driver)
        # signup.enter_fname("Gevorg")
        signup.enter_lname("Gasparyan")
        signup.enter_email("gevorg@yopmail.com")
        signup.enter_password("Gevorg555")
        signup.enter_confirm_password("Gevorg555")
        signup.signup_click()
        msg = self.driver.find_element_by_id("fname").get_attribute("validationMessage")
        self.assertEqual(msg, "Please fill out this field.")

    def test_04_fname_no_more_than_60_char(self):
        signup = SignUpPage(self.driver)
        n = random.randint(61, 70)
        chars = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=n))
        signup.enter_fname(chars)
        val = signup.field_value(signup.fname_id)
        self.assertEqual(len(val), 60)
        count = signup.counter_val(signup.fname_id)
        self.assertEqual(count, "60/60")

    def test_05_fname_character_counter(self):
        signup = SignUpPage(self.driver)
        chars = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=11))
        signup.enter_fname(chars)
        count = signup.counter_val(signup.fname_id)
        self.assertEqual(count, "11/60")

    def test_06_fname_character_counter_less_than_2_char(self):
        signup = SignUpPage(self.driver)
        chars = ''.join(random.choices(string.ascii_lowercase, k=1))
        signup.enter_fname(chars)
        signup.blank_click()
        msg = signup.error_value(signup.fname_id)
        self.assertEqual(msg, "Field must be between 2 and 60 characters long.")

    @parameterized.expand([
        ("2 and 3", 2, 3, 5),
        ("3 and 5", 2, 3, 5),
    ])
    def test_add(self, _, a, b, expected):
        self.assertEqual(a + b, expected)



if __name__ == "__main__":
    unittest.main()