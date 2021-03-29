from ui.locators import locators
from ui.pages.auth_page import AuthPage
import time

class ProfPage(AuthPage):
    def change(self):
        self.click(locators.ProfileLocators.PROF_LOCATOR, 20)
        self.input("George", locators.ProfileLocators.FIO_LOCATOR)
        self.input("+77777777777", locators.ProfileLocators.NUM_LOCATOR)
        self.input("hahaha@mail.ru", locators.ProfileLocators.EMAIL_LOCATOR)
        element = self.find(locators.ProfileLocators.SAFE_BUTTON)
        element.click()
        self.click(locators.ProfileLocators.BACK_LINK)

    def check(self):
        self.click(locators.ProfileLocators.PROF_LOCATOR, 20)
        input_el = self.find(locators.ProfileLocators.FIO_LOCATOR)
        assert "George" == input_el.get_attribute('value')
        input_el = self.find(locators.ProfileLocators.NUM_LOCATOR)
        assert "+77777777777" == input_el.get_attribute('value')
        input_el = self.find(locators.ProfileLocators.EMAIL_LOCATOR)
        assert "hahaha@mail.ru" == input_el.get_attribute('value')

    def clear(self):
        self.input("", locators.ProfileLocators.FIO_LOCATOR)
        self.input("", locators.ProfileLocators.NUM_LOCATOR)
        self.input("", locators.ProfileLocators.EMAIL_LOCATOR)
        element = self.find(locators.ProfileLocators.SAFE_BUTTON)
        element.click()
        time.sleep(10)
        self.click(locators.ProfileLocators.BACK_LINK)
