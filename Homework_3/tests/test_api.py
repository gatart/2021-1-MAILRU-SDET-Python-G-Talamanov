import pytest


@pytest.mark.API
class TestApi:
    @pytest.fixture(scope='function', autouse=True)
    def auth(self, api_client):
        self.client = api_client

    def test_create(self, api_client):
        id_ = self.client.create_seg()
        assert self.client.seg_exist(id_)
        self.client.delete_seg(id_)

    def test_deletion(self, api_client):
        id_ = self.client.create_seg()
        self.client.delete_seg(id_)
        assert not self.client.seg_exist(id_)
