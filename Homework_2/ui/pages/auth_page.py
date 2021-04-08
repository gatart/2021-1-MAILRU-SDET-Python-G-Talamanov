from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from ui.locators import locators


class AuthPage(object):
    locs = locators.AuthPageLocators()

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        self.find(locator, timeout)
        self.wait(timeout).until(EC.element_to_be_clickable(locator)).click()

    def input(self, put, locator):
        field = self.find(locator)
        field.clear()
        field.send_keys(put)
        return field

    def auth(self, login, password):
        self.click(locators.AuthPageLocators.BUTTON_LOCATOR)
        self.auth_locat(login, password, self.locs.LOGIN_LOCATOR, self.locs.PASSWORD_LOCATOR)

    def auth_2(self, login, password):
        self.auth_locat(login, password, self.locs.LOG_LOC_2, self.locs.PAS_LOC_2)

    def wait(self, timeout=None):

        if timeout is None:
            timeout = 5

        return WebDriverWait(self.driver, timeout, ignored_exceptions=StaleElementReferenceException)

    def auth_locat(self, login, password, Log_loc, Pas_log):
        self.input(login, Log_loc)
        element = self.input(password, Pas_log)
        element.send_keys(Keys.RETURN)
