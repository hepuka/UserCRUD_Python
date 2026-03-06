from repositories.base_repository import BaseRepository
from models.order_model import Order
from bson import ObjectId

class OrderRepository(BaseRepository):

    def __init__(self):
        super().__init__("orders", Order)

    def update_order_status(self, order_id: ObjectId, new_status: str):
        result = self.collection.update_one(
            {"_id": order_id},
            {"$set": {"status": new_status, "modifiedAt": __import__('datetime').datetime.now().strftime("%Y-%m-%d %H:%M:%S")}}
        )
        return result.modified_count > 0

