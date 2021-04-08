import pytest
from ui.locators import locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base import BaseCase


@pytest.mark.UI
class TestAuth(BaseCase):
    def test_good_auth(self):
        self.auth_page.auth('talamanov01@mail.ru', "qwerty123456")
        wait = WebDriverWait(self.driver, timeout=20)
        wait.until(EC.presence_of_element_located(locators.AuthPageLocators.AUTH_LOCATOR))
        wait.until(EC.visibility_of_element_located(locators.AuthPageLocators.AUTH_LOCATOR))

    def test_logout(self, auto_auth):
        self.driver = auto_auth
        self.auth_page.logout()
        self.auth_page.wait(10).until(EC.presence_of_element_located(locators.AuthPageLocators.BUTTON_LOCATOR))


@pytest.mark.UI
class TestGoTo(BaseCase):
    @pytest.mark.parametrize("checks",
                             ((locators.SegmentLocators.SEGMENT_LOCATOR, locators.SegmentLocators.SEGMENT_CHECK_1),
                              (locators.ProfileLocators.PROF_LOCATOR, locators.ProfileLocators.FIO_LOCATOR)))
    def test(self, checks, auto_auth):
        self.driver = auto_auth
        self.auth_page.click(checks[0], 20)
        self.auth_page.wait(20).until(EC.presence_of_element_located(checks[1]))


@pytest.mark.UI
class TestProfile(BaseCase):
    def test_change(self, auto_auth):
        self.driver = auto_auth
        self.prof_page.change()
        self.prof_page.check()
        self.prof_page.clear()
