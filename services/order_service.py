from datetime import datetime
from services.base_service import BaseService


class OrderService(BaseService):

    def __init__(self, repository):
        super().__init__(repository)

    def create_order(self, data):
        data["createdAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.repository.create(data)