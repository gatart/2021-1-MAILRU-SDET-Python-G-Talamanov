import requests
import pytest

import settings
from mock.flask_mock import SURNAME_DATA

url = f'http://{settings.APP_HOST}:{settings.APP_PORT}'


class TestApp:
    @pytest.mark.app
    def test_add_get_user(self):
        resp = requests.post(f'{url}/add_user', json={'name': 'Ilya'})
        user_id_from_add = resp.json()['user_id']

        resp = requests.get(f'{url}/get_user/Ilya')
        user_id_from_get = resp.json()['user_id']

        assert user_id_from_add == user_id_from_get

    @pytest.mark.app
    def test_add_existent_user(self):
        requests.post(f'{url}/add_user', json={'name': 'Ilya1'})
        resp = requests.post(f'{url}/add_user', json={'name': 'Ilya1'})
        assert resp.status_code == 400

    @pytest.mark.app
    def test_has_not_surname(self):
        requests.post(f'{url}/add_user', json={'name': 'Sveta'})

        resp = requests.get(f'{url}/get_user/Sveta')
        assert resp.json()['surname'] == None

        print(resp.json())


class TestMock:
    @pytest.mark.get
    def test_has_surname(self):
        SURNAME_DATA['Olya'] = 'Zaitceva'

        requests.post(f'{url}/add_user', json={'name': 'Olya'})

        resp = requests.get(f'{url}/get_user/Olya')
        assert resp.json()['surname'] == 'Zaitceva'

        print(resp.json())

    @pytest.mark.get
    def test_get_non_existent_user(self):
        resp = requests.get(f'{url}/get_user/dnsfndksfnkjsdnfjkdsjkfnsd')
        assert resp.status_code == 404

    # ----------------------------------------My code-----------------------------------------------------------------
    @pytest.mark.put
    def test_put_update(self):
        SURNAME_DATA['George'] = 'Talamanov'
        requests.post(f'{url}/add_user', json={'name': 'George'})

        resp = requests.put(f'{url}/update_user/George', json={'surname': 'Kalashnikov'})
        assert resp.status_code == 200

        resp = requests.get(f'{url}/get_user/George')
        assert resp.json()['surname'] == 'Kalashnikov'

    @pytest.mark.put
    def test_put_create(self):
        resp = requests.put(f'{url}/update_user/John', json={'surname': 'Talamanov'})
        assert resp.status_code == 201

        resp = requests.get(f'{url}/get_user/John')
        assert resp.json()['surname'] == 'Talamanov'

    @pytest.mark.delete
    def test_del_good(self):
        SURNAME_DATA['Alina'] = 'Novikova'
        requests.post(f'{url}/add_user', json={'name': 'Alina'})

        resp = requests.delete(f'{url}/delete_surname/Alina')
        assert resp.status_code == 200
        resp = requests.get(f'{url}/get_user/Alina')
        assert resp.json()['surname'] == None

    @pytest.mark.delete
    def test_del_no_surname(self):
        requests.post(f'{url}/add_user', json={'name': 'Anna'})

        resp = requests.delete(f'{url}/delete_surname/Anna')
        assert resp.status_code == 422

    @pytest.mark.delete
    def test_del_bad(self):
        resp = requests.delete(f'{url}/delete_surname/Mike')
        assert resp.status_code == 404
