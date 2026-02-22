from repositories.base_repository import BaseRepository
from models.product_model import Product

class ProductRepository(BaseRepository):

    def __init__(self):
        super().__init__("products", Product)

    def find_by_name(self, name):
        return self.find_by_field("name", name)

    def find_by_name_contains(self, keyword):
        results = self.collection.find(
            {"name": {"$regex": keyword, "$options": "i"}},  # i = case insensitive
            {"_id": 0}
        )
        return [self.model_class(doc) for doc in results]