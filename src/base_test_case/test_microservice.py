import allure
from flask import json


class TestBase:

    @staticmethod
    def products_post_req(product_model, service_api):
        with allure.step('1. Create model of a single product'):
            product = product_model
        with allure.step('2. Post the product created during the previous step'):
            response = service_api.post('products', data=json.dumps(dict(product)))
        with allure.step('3. Check if status code of the response is equal to 201'):
            assert response.status_code == 201

    @staticmethod
    def products_product_id_get_req(product_model, service_api):
        with allure.step('1. Pick id of a single product'):
            product_id = product_model.product_id
        with allure.step('2. Get the product by id picked during the previous step'):
            response = service_api.get(f'products/{product_id}')
        with allure.step('3. Check if status code of the response is equal to 200'):
            assert response.status_code == 200

    @staticmethod
    def products_product_id_put_req(product_model, service_api):
        with allure.step('1. Pick id of a single product'):
            product_id = product_model.product_id
        with allure.step('2. Put the product by id picked during the previous step'):
            response = service_api.put(f'products/{product_id}')
        with allure.step('3. Check if status code of the response is equal to 200'):
            assert response.status_code == 200

    @staticmethod
    def products_search_get_req(product_model, service_api):
        with allure.step('1. Pick parameters for search of a single product'):
            params = {
                'search': product_model.description,
                'name': product_model.name,
                'rating': product_model.rating
            }
        with allure.step('2. Get the product with these parameters: {}'.format(params)):
            response = service_api.get('products/search', params=params)
        with allure.step('3. Check if status code of the response is equal to 200'):
            assert response.status_code == 200
