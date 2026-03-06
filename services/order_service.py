from datetime import datetime
from services.base_service import BaseService
from bson import ObjectId

class OrderService(BaseService):

    def __init__(self, repository):
        super().__init__(repository)

    def create_order(self, data):
        data["createdAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.repository.create(data)


    def add_products_to_order(self, object_id, new_products, total_to_add):
        if not isinstance(object_id, ObjectId):
            object_id = ObjectId(object_id)

        updates = {
            "$push": {"products": {"$each": new_products}},
            "$inc": {"total": int(total_to_add)},
            "$set": {"modifiedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        }

        result = self.repository.collection.update_one(
            {"_id": object_id},
            updates
        )

        return result.modified_count > 0