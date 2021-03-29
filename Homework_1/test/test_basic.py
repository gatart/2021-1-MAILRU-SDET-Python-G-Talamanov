import pytest
from ui.locators import locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base import BaseCase


@pytest.mark.ui
class TestAuth(BaseCase):
    @pytest.mark.skip(reason='no need')
    def test_good_auth(self):
        self.auth_page.auth('talamanov01@mail.ru', "qwerty123456")
        wait = WebDriverWait(self.driver, timeout=20)
        wait.until(EC.presence_of_element_located(locators.AuthPageLocators.AUTH_LOCATOR))
        wait.until(EC.visibility_of_element_located(locators.AuthPageLocators.AUTH_LOCATOR))

    @pytest.mark.skip(reason='no need')
    def test_bad_auth(self):
        self.auth_page.auth('talamanov01@mail.ru', 'hgfjhagjdfsd')
        assert "Invalid login or password" in self.driver.page_source

    @pytest.mark.skip(reason='no need')
    def test_logout(self, auto_auth):
        self.driver = auto_auth
        self.auth_page.logout()
        self.auth_page.wait(10).until(EC.presence_of_element_located(locators.AuthPageLocators.BUTTON_LOCATOR))


@pytest.mark.ui
class TestGoTo(BaseCase):
    @pytest.mark.skip(reason='no need')
    @pytest.mark.parametrize("checks",
                             ((locators.SegmentLocators.SEGMENT_LOCATOR, locators.SegmentLocators.SEGMENT_CHECK_1),
                              (locators.ProfileLocators.PROF_LOCATOR, locators.ProfileLocators.FIO_LOCATOR)))
    def test(self, checks, auto_auth):
        self.driver = auto_auth
        self.auth_page.click(checks[0], 20)
        self.auth_page.wait(20).until(EC.presence_of_element_located(checks[1]))


@pytest.mark.ui
class TestProfile(BaseCase):
    @pytest.mark.skip(reason='no need')
    def test_change(self, auto_auth):
        self.driver = auto_auth
        self.auth_page.click(locators.ProfileLocators.PROF_LOCATOR, 20)

        pass