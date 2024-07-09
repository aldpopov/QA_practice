import pytest
import requests
from src.generators.builders import ProductBuilder

class ApiClient:
    def __init__(self, base_address, headers):
        self.base_address = base_address
        self.headers = headers

    def post(self, path="/", params=None, data=None, json=None):
        url = f"{self.base_address}{path}"
        return requests.post(url=url, params=params, data=data, json=json, headers=self.headers, verify=False)

    def get(self, path="/", params=None):
        url = f"{self.base_address}{path}"
        return requests.get(url=url, params=params, headers=self.headers, verify=False)

    def put(self, path="/",params=None):
        url = f"{self.base_address}{path}"
        return requests.put(url=url, params=params, headers=self.headers, verify=False)


@pytest.fixture
def service_api():
    return ApiClient(base_address="https://localhost:5007/api/v1/", headers={'Content-Type': 'application/json'})


@pytest.fixture
def test_product():
    return ProductBuilder().set_description('ball').set_name('media').set_price(691029.526710028).set_quantity(10).set_rating(10).get_product()
