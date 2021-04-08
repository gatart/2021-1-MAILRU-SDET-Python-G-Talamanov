import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.auth_page import AuthPage
from ui.pages.profile_page import ProfPage


@pytest.mark.UI
class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request: FixtureRequest):
        self.driver = driver

        self.auth_page: AuthPage = request.getfixturevalue('auth_page')
        self.prof_page: ProfPage = request.getfixturevalue('prof_page')
