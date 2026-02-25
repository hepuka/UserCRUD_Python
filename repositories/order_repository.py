from repositories.base_repository import BaseRepository
from models.order_model import Order

class OrderRepository(BaseRepository):

    def __init__(self):
        super().__init__("orders", Order)

