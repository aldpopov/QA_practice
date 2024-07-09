import pytest
import allure
from faker import Faker

from src.base_test_case.test_microservice import TestBase
from src.generators.builders import ProductBuilder

fake = Faker()
Faker.seed(451)


@allure.story('Testing with semi-correct inputs')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize('product_model', [
    ProductBuilder().set_description('deus')
                    .set_name('exhr')
                    .set_price(691029.526710028)
                    .set_quantity(10).set_rating(10)
                    .get_product(),
    ProductBuilder().new_correct_product()
                    .get_product(),
    ProductBuilder().set_description(fake.pyint())
                    .set_name(fake.pyfloat())
                    .set_price(fake.word())
                    .set_quantity(fake.sentence())
                    .set_rating(fake.random_letter())
                    .get_product(),
    ProductBuilder().set_description('Four')
                    .set_name('lE')
                    .set_product_id('tr')
                    .get_product()
    ])
class TestService(TestBase):
    """
    Two products with correct input and two with type violations to check if the service can handle ordinary operations.
    I (as a user) post new product, check it, update it and try to find it using different methods (to track it).
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
