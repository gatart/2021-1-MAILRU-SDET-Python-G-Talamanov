import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.auth_page import AuthPage


@pytest.mark.ui
class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request: FixtureRequest):
        self.driver = driver

        self.auth_page: AuthPage = request.getfixturevalue('auth_page')
