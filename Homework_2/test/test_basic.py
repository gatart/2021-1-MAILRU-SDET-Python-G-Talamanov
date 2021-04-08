import pytest
from ui.locators import locators
from selenium.common.exceptions import TimeoutException
from base import BaseCase


@pytest.mark.UI
class TestAuth(BaseCase):
    # @pytest.mark.skip(reason='no need')
    def test_bad_auth_1(self):
        self.auth_page.auth('talamanov01@mail.ru', 'hgfjhagjdfsd')
        assert "Invalid login or password" in self.driver.page_source

    # @pytest.mark.skip(reason='no need')
    def test_bad_auth_2(self):
        self.auth_page.auth('talamanov01@mail.ru', 'hgfjhagjdfsd')
        self.auth_page.auth_2('', '')
        assert ("Invalid login or password" or "Неверный логин или пароль") in self.driver.page_source


# @pytest.mark.skip(reason='no need')
@pytest.mark.UI
class TestCompany(BaseCase):
    def test_creation(self, auto_auth):
        self.driver = auto_auth
        self.company_page.create("Company is who")
        self.company_page.find(locators.CompanyLocators.CHECK, timeout= 10)
        self.company_page.clear()


@pytest.mark.UI
class TestSegment(BaseCase):
    # @pytest.mark.skip(reason='no need')
    def test_creation(self, auto_auth):
        self.driver = auto_auth
        self.segment_page.create("Super-puper-hyper-dooper section")
        self.segment_page.find(locators.SegmentLocators.SEGMENT_1)
        self.segment_page.delete("Super-puper-hyper-dooper section")

    # @pytest.mark.skip(reason='no need')
    def test_deletion(self, auto_auth):
        self.driver = auto_auth
        self.segment_page.create("Super-puper-puper-hyper-dooper section")
        self.segment_page.delete("Super-puper-puper-hyper-dooper section")
        with pytest.raises(TimeoutException):
            self.segment_page.find(locators.SegmentLocators.SEGMENT_2)
