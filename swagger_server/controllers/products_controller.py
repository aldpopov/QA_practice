import connexion
import six

from swagger_server.models.models_product import ModelsProduct  # noqa: E501
from swagger_server.models.models_products_list import ModelsProductsList  # noqa: E501
from swagger_server import util


def products_post():  # noqa: E501
    """Create new product

    Create new single product # noqa: E501


    :rtype: ModelsProduct
    """
    return 'do some magic!'


def products_product_id_get(product_id):  # noqa: E501
    """Get product by id

    Get single product by id # noqa: E501

    :param product_id: product id
    :type product_id: str

    :rtype: ModelsProduct
    """
    return 'do some magic!'


def products_product_id_put(product_id):  # noqa: E501
    """Update single product

    Update single product by id # noqa: E501

    :param product_id: product id
    :type product_id: str

    :rtype: ModelsProduct
    """
    return 'do some magic!'


def products_search_get(search=None, page=None, size=None):  # noqa: E501
    """Search product

    Search product by name or description # noqa: E501

    :param search: search text
    :type search: str
    :param page: page number
    :type page: str
    :param size: number of elements
    :type size: str

    :rtype: ModelsProductsList
    """
    return 'do some magic!'
