
from services.base_service import BaseService

class ProductService(BaseService):

    def __init__(self, repository):
        super().__init__(repository)

    def find_by_name_contains(self, keyword):
        return self.repository.find_by_name_contains(keyword)