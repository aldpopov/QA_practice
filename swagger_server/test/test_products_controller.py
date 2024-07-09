# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.models_product import ModelsProduct  # noqa: E501
from swagger_server.models.models_products_list import ModelsProductsList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProductsController(BaseTestCase):
    """ProductsController integration test stubs"""

    def test_products_post(self):
        """Test case for products_post

        Create new product
        """
        response = self.client.open(
            '/products',
            method='POST',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_product_id_get(self):
        """Test case for products_product_id_get

        Get product by id
        """
        response = self.client.open(
            '/products/{product_id}'.format(product_id='product_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_product_id_put(self):
        """Test case for products_product_id_put

        Update single product
        """
        response = self.client.open(
            '/products/{product_id}'.format(product_id='product_id_example'),
            method='PUT',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_search_get(self):
        """Test case for products_search_get

        Search product
        """
        query_string = [('search', 'search_example'),
                        ('page', 'page_example'),
                        ('size', 'size_example')]
        response = self.client.open(
            '/products/search',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
