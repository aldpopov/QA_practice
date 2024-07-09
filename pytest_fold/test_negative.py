import pytest
import allure
from faker import Faker

from src.base_test_case.test_microservice import TestBase
from src.generators.builders import ProductBuilder

fake = Faker()
Faker.seed(451)


@allure.story('Testing with incorrect inputs and type violations')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize('product_model', [
    ProductBuilder().set_description(fake.text()).set_name(20)
                    .set_price(9999)
                    .set_quantity(fake.pyint(9999)).set_rating(fake.pyint(9999))
                    .get_product(),
    ProductBuilder().set_created_at(fake.text())
                    .set_product_id(fake.pyfloat(positive=False))
                    .get_product(),
    ])
class TestService(TestBase):
    """
    Two products with incorrect inputs, type violations, and large numbers to do a stress test.
    I (as a malicious user) tru to break the service (to stop its work)
    """
    @allure.feature('Post new product')
    @allure.description('Create new single product')
    def test_products_post_req(self, product_model, service_api):
        super().products_post_req(product_model, service_api)

    @allure.feature('Get product by id')
    @allure.description('Get single product by id')
    def test_products_product_id_get_req(self, product_model, service_api):
        super().products_product_id_get_req(product_model, service_api)

    @allure.feature('Update product by id')
    @allure.description('Update single product by id')
    def test_products_product_id_put_req(self, product_model, service_api):
        super().products_product_id_put_req(product_model, service_api)

    @allure.feature('Search for product')
    @allure.description('Search for product by description or name')
    def test_products_search_get_req(self, product_model, service_api):
        super().products_search_get_req(product_model, service_api)