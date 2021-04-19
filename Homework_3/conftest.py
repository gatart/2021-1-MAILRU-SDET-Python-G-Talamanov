import pytest
from api.client import ApiClient


@pytest.mark.api
@pytest.fixture(scope='function')
def api_client():
    user = 'talamanov01@mail.ru'
    password = 'qwerty123456'

    return ApiClient(user, password)
