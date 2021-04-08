from ui.locators import locators
from ui.pages.auth_page import AuthPage
from selenium.webdriver.common.keys import Keys
import time


class ProfPage(AuthPage):
    def change(self):
        self.profile()
        self.input("George", locators.ProfileLocators.FIO_LOCATOR)
        self.input("+77777777777", locators.ProfileLocators.NUM_LOCATOR)
        element = self.find(locators.ProfileLocators.EMAIL_BUTTON)
        element.click()
        self.input("hahaha@mail.ru", locators.ProfileLocators.EMAIL_LOCATOR)
        element = self.save_but()
        element.click()
        self.back()

    def check(self):
        self.profile()
        assert "George" == self.value(self.fio())
        assert "+77777777777" == self.value(self.num())
        assert "hahaha@mail.ru" == self.value(self.email())

    def clear(self):
        field = self.fio()
        field.send_keys(Keys.BACK_SPACE * 15)
        field = self.num()
        field.send_keys(Keys.BACK_SPACE * 15)
        field = self.email()
        field.send_keys(Keys.BACK_SPACE * 15)
        element = self.save_but()
        element.click()
        time.sleep(10)
        self.back()
        time.sleep(10)

    def fio(self):
        return self.find(locators.ProfileLocators.FIO_LOCATOR)

    def num(self):
        return self.find(locators.ProfileLocators.NUM_LOCATOR)

    def email(self):
        return self.find(locators.ProfileLocators.EMAIL_LOCATOR)

    def save_but(self):
        return self.find(locators.ProfileLocators.SAFE_BUTTON)

    def profile(self):
        self.click(locators.ProfileLocators.PROF_LOCATOR, 20)

    def back(self):
        self.click(locators.ProfileLocators.BACK_LINK)

    def value(self, el):
        return el.get_attribute('value')
