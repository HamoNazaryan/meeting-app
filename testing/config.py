from selenium import webdriver
import unittest
from pathlib import Path
import random
import string

path = Path(__file__).parents[0]
outpath =str(path / 'webdriver'/'chrome_83'/'chromedriver_win32'/'chromedriver.exe')
htmlOutPutUrl = str(path/'Reports/')

class BaseConfig(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=outpath)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complated")

    def makeEmail(self):
        extensions = ['com', 'net', 'org', 'gov']
        domains = ['gmail', 'yahoo', 'hotmail', 'outlook']

        ext = extensions[random.randint(0, len(extensions) - 1)]
        dom = domains[random.randint(0, len(domains) - 1)]
        acclen = random.randint(1, 20)
        acc = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(acclen))
        finale = acc + "@" + dom + "." + ext
        return finale

    def makeIncorrectEmail(self):
        extensions = ['com', 'net', 'org', 'gov']
        domains = ['gmail', 'yahoo', 'hotmail', 'outlook']
        sp_char = [" ", "(", ")", ",", ":", ";", "<", ">", "@", "[", "\\", "]"]

        ext = extensions[random.randint(0, len(extensions) - 1)]
        dom = domains[random.randint(0, len(domains) - 1)]
        simb = sp_char[random.randint(0, len(sp_char)-1)]

        acclen = random.randint(1, 4)
        acc = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(acclen))
        finale = acc + simb + "@" + dom + "." + ext
        return finale

