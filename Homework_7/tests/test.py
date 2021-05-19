import requests
import pytest

import settings
from mock.flask_mock import SURNAME_DATA

url = f'http://{settings.APP_HOST}:{settings.APP_PORT}'


@pytest.mark.skip
def test_add_get_user():
    resp = requests.post(f'{url}/add_user', json={'name': 'Ilya'})#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
    user_id_from_add = resp.json()['user_id']

    resp = requests.get(f'{url}/get_user/Ilya')#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    user_id_from_get = resp.json()['user_id']

    assert user_id_from_add == user_id_from_get


@pytest.mark.skip
def test_add_existent_user():
    requests.post(f'{url}/add_user', json={'name': 'Ilya1'})#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    resp = requests.post(f'{url}/add_user', json={'name': 'Ilya1'})
    assert resp.status_code == 400


@pytest.mark.skip
def test_has_not_surname():
    requests.post(f'{url}/add_user', json={'name': 'Sveta'})#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    resp = requests.get(f'{url}/get_user/Sveta')#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    assert resp.json()['surname'] == None

    print(resp.json())


@pytest.mark.skip
def test_by_socket():#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    requests.post(f'{url}/add_user', json={'name': 'Egor'})#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    import socket
    import json

    host = settings.APP_HOST
    port = int(settings.APP_PORT)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.settimeout(0.1)

    client.connect((host, port))

    params = '/get_user/Egor'
    request = f'GET {params} HTTP/1.1\r\nHost:{host}\r\n\r\n'

    client.send(request.encode())

    total_data = []

    while True:
        data = client.recv(4096)
        if data:
            total_data.append(data.decode())
        else:
            client.close()
            break

    data = ''.join(total_data).splitlines()

    print(data)

    assert json.loads(data[-1])['age'] > 0


class TestMock:
    @pytest.mark.skip
    def test_has_surname(self):
        SURNAME_DATA['Olya'] = 'Zaitceva'

        requests.post(f'{url}/add_user', json={'name': 'Olya'})#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        resp = requests.get(f'{url}/get_user/Olya')#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        assert resp.json()['surname'] == 'Zaitceva'

        print(resp.json())

    @pytest.mark.skip
    def test_get_non_existent_user(self):
        resp = requests.get(f'{url}/get_user/dnsfndksfnkjsdnfjkdsjkfnsd')  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        assert resp.status_code == 404

    # ----------------------------------------My code-----------------------------------------------------------------

    def test_put_update(self):
        SURNAME_DATA['George'] = 'Talamanov'
        requests.post(f'{url}/add_user', json={'name': 'George'})

        resp = requests.put(f'{url}/update_user/George', json={'surname': 'Kalashnikov'})
        assert resp.status_code == 200

        resp = requests.get(f'{url}/get_user/George')
        assert resp.json()['surname'] == 'Kalashnikov'

    def test_put_create(self):
        resp = requests.put(f'{url}/update_user/John', json={'surname': 'Talamanov'})
        assert resp.status_code == 201

        resp = requests.get(f'{url}/get_user/John')
        assert resp.json()['surname'] == 'Talamanov'

    @pytest.mark.skip
    def test_del_surname_good(self):
        SURNAME_DATA['Alina'] = 'Novikova'
        requests.post(f'{url}/add_user', json={'name': 'Alina'})

        resp = requests.delete(f'{url}/del_surname/Alina')
        assert resp.status_code == 200
        resp = requests.get(f'{url}/get_user/Alina')
        assert resp.json()['surname'] == None

    @pytest.mark.skip
    def test_del_surname_bad(self):
        resp = requests.delete(f'{url}/del_surname/Mike')
        assert resp.status_code == 404 # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Ne videt etot url
