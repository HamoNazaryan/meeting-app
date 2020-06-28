from selenium import webdriver
import unittest
import HtmlTestRunner

PATH = r"./webdriver/chrome_83/chromedriver_win32/chromedriver.exe"

class MeetingApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=PATH)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_serch_automationstepbystep(self):
        self.driver.get("http://127.0.0.1:5000")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'./Reports'))

