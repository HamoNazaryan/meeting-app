import time
import unittest
import HtmlTestRunner
from testing.Project.Pages.signUpPage import SignUpPage
from testing. Project.Pages.homePage import HomePage
from testing.config import BaseConfig, htmlOutPutUrl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
from parameterized import parameterized
from testing.Project.Locators.locatorsSignUpPage import LocatorsSignUpPage



class SignUpTest(BaseConfig):
    def setUp(self):
        self.page = SignUpPage(self.driver)
        self.driver.get("http://127.0.0.1:5000/signup")

    def tearDown(self):
        time.sleep(2)

    def test_01_check_elements(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,self.page.signup_title_selector)))
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID,self.page.fname_id)))
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, self.page.lname_id)))
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, self.page.email_id)))
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, self.page.password_id)))
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, self.page.confirm_password_id)))
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, self.page.signup_button_id)))
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.page.have_account_block_selector)))
        title = self.page.title_text()
        self.assertEqual(title, "Sign Up")
        have_text = self.page.have_an_account_block_text()
        self.assertEqual(have_text, "Already Have An Account? Sign In")
        signin_text = self.page.signin_text()
        self.assertEqual(signin_text, "Sign In")

    def test_02_signup_valid(self):
        self.page.enter_text(self.page.fname_id, "Garik")
        self.page.enter_text(self.page.lname_id, "Gabrielyan")
        self.page.enter_text(self.page.email_id, "garik88@yopmail.com")
        self.page.enter_text(self.page.password_id, "Gevorg555")
        self.page.enter_text(self.page.confirm_password_id, "Gevorg555")
        self.page.signup_click()
        url = self.page.current_url()
        self.assertEqual(url, "http://127.0.0.1:5000/home")
        home = HomePage(self.driver)
        home.click_menu()
        home.click_logout()

    def test_03_taken_email(self):
        self.page.enter_text(self.page.fname_id, "Poxos")
        self.page.enter_text(self.page.lname_id, "Poxosyan")
        self.page.enter_text(self.page.email_id, "gevorg@yopmail.com")
        self.page.enter_text(self.page.password_id, "Poxos555")
        self.page.enter_text(self.page.confirm_password_id, "Poxos555")
        self.page.signup_click()
        msg = self.page.error_value(self.page.email_id)
        self.assertEqual(msg, "The email is taken. Please choose a different one.")

    def test_04_invalid_email(self):
        self.page.enter_text(self.page.fname_id, "Poxos")
        self.page.enter_text(self.page.lname_id, "Poxosyan")
        self.page.enter_text(self.page.email_id, self.makeIncorrectEmail())
        self.page.enter_text(self.page.password_id, "Poxos555")
        self.page.enter_text(self.page.confirm_password_id, "Poxos555")
        self.page.signup_click()
        msg = self.page.error_value(self.page.email_id)
        self.assertEqual(msg, "Invalid email address.")


    @parameterized.expand([
        ("first_name",  LocatorsSignUpPage.fname_id, "", "Gasparyan" , "gevorg@yopmail.com" , "Gevorg555", "Gevorg555"),
        ("last_name", LocatorsSignUpPage.lname_id, "Gevorg", "", "gevorg@yopmail.com", "Gevorg555", "Gevorg555"),
        ("email", LocatorsSignUpPage.email_id, "Gevorg", "Gasparyan", "", "Gevorg555", "Gevorg555"),
        ("password", LocatorsSignUpPage.password_id, "Gevorg", "Gasparyan", "gevorg@yopmail.com", "", "Gevorg555"),
        ("confirm_password", LocatorsSignUpPage.confirm_password_id, "Gevorg", "Gasparyan", "gevorg@yopmail.com", "Gevorg555", ""),
    ])
    def test_05_empty_text(self, _, id, fname, lname, email, password, conf_password):
        if fname: self.page.enter_text(self.page.fname_id, fname)
        if lname: self.page.enter_text(self.page.lname_id, lname)
        if email: self.page.enter_text(self.page.email_id, email)
        if password: self.page.enter_text(self.page.password_id, password)
        if conf_password: self.page.enter_text(self.page.confirm_password_id, conf_password)
        self.page.signup_click()
        msg = self.driver.find_element_by_id(id).get_attribute("validationMessage")
        self.assertEqual(msg, "Please fill out this field.")

    @parameterized.expand([
        ("first_name", LocatorsSignUpPage.fname_id),
        ("last_name", LocatorsSignUpPage.lname_id),
        ("password", LocatorsSignUpPage.password_id),
        ("confirm_password", LocatorsSignUpPage.confirm_password_id)
    ])
    def test_06_no_more_than_60_char(self,_, input_id):
        n = random.randint(61, 70)
        chars = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=n))
        self.page.enter_text(input_id, chars)
        val = self.page.field_value(input_id)
        self.assertEqual(len(val), 60)
        count = self.page.counter_val(input_id)
        self.assertEqual(count, "60/60")

    @parameterized.expand([
        ("first_name", LocatorsSignUpPage.fname_id),
        ("last_name", LocatorsSignUpPage.lname_id),
        ("password", LocatorsSignUpPage.password_id),
        ("confirm_password", LocatorsSignUpPage.confirm_password_id)
    ])
    def test_07_character_counter(self, _, input_id):
        chars = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=11))
        self.page.enter_text(input_id, chars)
        count = self.page.counter_val(input_id)
        self.assertEqual(count, "11/60")

    @parameterized.expand([
        ("first_name", LocatorsSignUpPage.fname_id, "Field must be between 2 and 60 characters long."),
        ("last_name", LocatorsSignUpPage.lname_id, "Field must be between 2 and 60 characters long."),
        ("password", LocatorsSignUpPage.password_id, "Field must be between 6 and 60 characters long."),
        ("confirm_password", LocatorsSignUpPage.confirm_password_id, "Field must be equal to password.")
    ])
    def test_08_character_counter_less_than_2_char(self, _, input_id, expected):
        chars = ''.join(random.choices(string.ascii_lowercase, k=1))
        self.page.enter_text(input_id, chars)
        self.page.blank_click()
        msg = self.page.error_value(input_id)
        self.assertEqual(msg, expected)

    def test_09_password_equal_to_confirm_password(self):
        n = random.randint(4,20)
        chars = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=n))
        self.page.enter_text(self.page.password_id, "Poxos555")
        self.page.enter_text(self.page.confirm_password_id, chars)
        self.page.blank_click()
        msg = self.page.error_value(self.page.confirm_password_id)
        self.assertEqual(msg, "Field must be equal to password.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=htmlOutPutUrl))

    
# if __name__ == "__main__":
#     unittest.main()