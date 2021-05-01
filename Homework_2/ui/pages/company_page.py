import os
import time
from ui.pages.auth_page import AuthPage

from ui.locators import locators


class CompanyPage(AuthPage):
    def create(self, name):
        self.click(locators.CompanyLocators.COMPANY_BUTTON, timeout=7)
        self.click(locators.CompanyLocators.TYPE_LOCATOR, timeout=10)
        self.input("test.com", locators.CompanyLocators.LINK_LOCATOR)
        self.click(locators.CompanyLocators.FORMAT_LOCATOR)
        el = self.find(locators.CompanyLocators.UPLOAD)
        time.sleep(10)
        path = os.path.join(os.path.dirname(__file__), 'data', 'Smisol.jpg')
        el.send_keys(path)

        self.click(locators.CompanyLocators.LOAD_BUTTON)
        self.input(name, locators.CompanyLocators.COMPANY_NAME)
        self.click(locators.CompanyLocators.MAKE_BUTTON)

    def clear(self):
        self.wait(10)
        self.click(locators.CompanyLocators.CHECKBOX)
        self.click(locators.CompanyLocators.ACTION_LOCATOR)
        self.click(locators.CompanyLocators.DELETE_BUTTON)
