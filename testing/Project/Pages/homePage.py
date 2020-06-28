from testing.Project.Locators.locatorsHomePage import LocatorsHomePage


# pagination_block = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
#     (By.CSS_SELECTOR, "span.b-pagination__item.b-pagination__item--next.js-pagination-next")))

class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.menu_class_name = LocatorsHomePage.menu_class_name
        self.logout_selector = LocatorsHomePage.logout_selector

    def click_menu(self):
        self.driver.find_element_by_class_name(self.menu_class_name).click()

    def click_logout(self):
        self.driver.find_element_by_css_selector(self.logout_selector).click()
