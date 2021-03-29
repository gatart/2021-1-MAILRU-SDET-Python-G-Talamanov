from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from ui.locators import locators

CLICK_RETRY = 3


class AuthPage(object):
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator, timeout)
                if i < 2:
                    self.driver.refresh()
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def input(self, put, locator):
        field = self.find(locator)
        field.clear()
        field.send_keys(put)
        return field

    def auth(self, login, password):
        self.click(locators.AuthPageLocators.BUTTON_LOCATOR)
        self.input(login, locators.AuthPageLocators.LOGIN_LOCATOR)
        element = self.input(password, locators.AuthPageLocators.PASSWORD_LOCATOR)
        element.send_keys(Keys.RETURN)

    def wait(self, timeout=None):

        if timeout is None:
            timeout = 10

        return WebDriverWait(self.driver, timeout)

    def logout(self):
        self.click(locators.AuthPageLocators.LOGOUT_MENU)
        element = self.wait(10).until(EC.element_to_be_clickable(locators.AuthPageLocators.LOGOUT_BUTTON))
        element.click()
