from faker import Faker
from swagger_server.models.models_product import ModelsProduct
from swagger_server.models.models_products_list import ModelsProductsList

fake = Faker()
Faker.seed(451)


class ProductBuilder:

    def __init__(self):
        self.product = ModelsProduct()

    def set_description(self, description):
        self.product.description = description
        return self

    def set_name(self, name):
        self.product.name = name
        return self

    def set_price(self, price):
        self.product.price = price
        return self

    def set_quantity(self, quantity):
        self.product.quantity = quantity
        return self

    def set_rating(self, rating):
        self.product.rating = rating
        return self

    def set_category_id(self, category_id):
        self.product.category_id = category_id
        return self

    def set_created_at(self, created_at):
        self.product.created_at = created_at
        return self

    def set_image_url(self, image_url):
        self.product.image_url = image_url
        return self

    def set_photos(self, photos):
        self.product.photos = photos
        return self

    def set_product_id(self, product_id):
        self.product.product_id = product_id
        return self

    def set_updated_at(self, updated_at):
        self.product.updated_at = updated_at
        return self

    def new_correct_product(self):
        self.set_description(fake.sentence())
        self.set_name(fake.word())
        self.set_price(fake.pyfloat(positive=True))
        self.set_quantity(fake.pyint(min_value=0))
        self.set_rating(fake.pyint(min_value=0, max_value=10))
        return self

    def get_product(self):
        return self.product

class ProductListBuilder:
    def __init__(self):
        self.product_list = ModelsProductsList()

    def set_has_more(self, has_more):
        self.product_list.has_more = has_more
        return self

    def set_page(self, page):
        self.product_list.page = page
        return self

    def set_products(self, products):
        self.product_list.products = products
        return self

    def set_size(self, size):
        self.product_list.size = size
        return self

    def set_total_count(self, total_count):
        self.product_list.total_count = total_count
        return self

    def set_total_pages(self, total_pages):
        self.product_list.total_pages = total_pages
        return self

    def get_product_list(self):
        return self.product_list
