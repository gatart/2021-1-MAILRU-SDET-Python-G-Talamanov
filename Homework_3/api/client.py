import requests
import random
import string
from urllib.parse import urljoin


class ResponseStatusCodeException(Exception):
    pass


class FailedLoginError(Exception):
    pass


def random_title(length=10):
    letters = string.ascii_letters
    return ''.join(random.choices(letters, k=length))


class ApiClient:
    def __init__(self, user, password):
        self.base_url = 'https://target.my.com/'

        self.session = requests.Session()
        self.csrf = None

        self.user = user
        self.password = password
        self.login()
        self.set_csrf()

    def login(self):
        headers = {
            'Referer': self.base_url
        }
        data = {
            'email': self.user,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email'
        }

        res = self.session.request('POST', 'https://auth-ac.my.com/auth', headers=headers, data=data)
        if 'Invalid login or password' in res.text:
            raise FailedLoginError('Invalid login or password')

    def set_csrf(self):
        headers = self._request('GET', 'csrf/').headers
        self.csrf = headers['Set-Cookie'].split(';')[0].split('=')[-1]

    def seg_exist(self, id_):
        res = self._request('GET', 'api/v2/remarketing/segments.json?limit=500')
        return id_ in [x['id'] for x in res.json()['items']]

    def create_seg(self):
        title = random_title()
        res = self._request('POST', 'api/v2/remarketing/segments.json',
                            json={
                                "name": title,
                                "pass_condition": 1,
                                "relations": [{
                                    "object_type": "remarketing_player",
                                    "params": {"type": "positive", "left": 365, "right": 0}
                                }],
                                "logicType": "or"
                            },

                            headers={'X-CSRFToken': self.csrf})
        return res.json()['id']

    def delete_seg(self, id_):
        self._request('DELETE', f'api/v2/remarketing/segments/{id_}.json',
                      headers={'X-CSRFToken': self.csrf})

    def _request(self, method, location, accept_code=None, headers=None, params=None, data=None, json=None):
        if not accept_code:
            accept_code = range(200, 300)

        url = urljoin(self.base_url, location)

        res = self.session.request(method, url, headers=headers, params=params, data=data, json=json)

        if res.status_code not in accept_code:
            raise ResponseStatusCodeException(f'Response status code {res.status_code} not in  "{accept_code}"')

        return res
