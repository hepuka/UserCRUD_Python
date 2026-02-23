from controllers.base_controller import BaseController

class ProductController(BaseController):

    def __init__(self, service):
        super().__init__(service)

    def get_product(self, name):
        return self.service.get_by_field("name", name)

    def update_product(self, product, name, price, packaging):
        updates = {
            "name": name or product.name,
            "price": price or product.price,
            "packaging": packaging or product.packaging
        }

        self.service.update("name", product.name, updates)
        return self.get_product(updates["name"])

    def search_products(self, keyword):
        return self.service.find_by_name_contains(keyword)

    def get_by_category(self, category):
        return self.service.get_many_by_field("category", category)
