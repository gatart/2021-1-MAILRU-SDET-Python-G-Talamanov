from ui.pages.auth_page import AuthPage
from ui.locators import locators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


class SegmentPage(AuthPage):
    def create(self, name):
        self.click(locators.SegmentLocators.SEGMENT_LOCATOR, timeout=15)

        try:
            self.click(locators.SegmentLocators.CREATE_LOCATOR_1, timeout=7)
        except TimeoutException:
            self.click(locators.SegmentLocators.CREATE_LOCATOR_2, timeout=7)
            self.click(locators.SegmentLocators.TYPE_LOCATOR)

        self.click(locators.SegmentLocators.CHECKBOX_LOCATOR)
        self.click(locators.SegmentLocators.BUTTON_1_LOCATOR)
        self.input(name, locators.SegmentLocators.NAME_LOCATOR)
        self.click(locators.SegmentLocators.BUTTON_2_LOCATOR)

    def delete(self, name):
        element = self.input(name, locators.SegmentLocators.SEARCH)
        element.send_keys(Keys.RETURN)
        try:
            self.click(locators.SegmentLocators.LIST_ALL)
        except TimeoutException:
            self.click(locators.SegmentLocators.LIST_ONE)
        self.click(locators.SegmentLocators.CHECKBOX)
        self.click(locators.SegmentLocators.ACTION_LOCATOR)
        self.click(locators.SegmentLocators.DELETE_LOCATOR)
