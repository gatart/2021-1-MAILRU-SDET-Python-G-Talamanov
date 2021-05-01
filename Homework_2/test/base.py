import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.auth_page import AuthPage
from ui.pages.company_page import CompanyPage
from ui.pages.segment_page import SegmentPage


@pytest.mark.UI
class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request: FixtureRequest):
        self.driver = driver

        self.auth_page: AuthPage = request.getfixturevalue('auth_page')
        self.company_page: CompanyPage = request.getfixturevalue('company_page')
        self.segment_page: SegmentPage = request.getfixturevalue('segment_page')
