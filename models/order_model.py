from bson import ObjectId

class Order:

    def __init__(self, data: dict):
        self._id = ObjectId(data.get("_id")) if data.get("_id") else None
        self.user_id = data.get("user_id")
        self.table_number = data.get("table_number")
        self.products = data.get("products", [])
        self.total = data.get("total")
        self.status = data.get("status")
        self.createdAt = data.get("createdAt")
        self.modifiedAt = data.get("modifiedAt")

    def get_id(self):
            return self._id

    def __str__(self):
        return f"Order(id={self._id}, table={self.table_number}, total={self.total}, status={self.status}, products={len(self.products)})"

    def to_dict(self):
        return {
            "_id": self._id,
            "user_id": self.user_id,
            "table_number": self.table_number,
            "products": self.products,
            "total": self.total,
            "status": self.status,
            "createdAt": self.createdAt,
            "modifiedAt": self.modifiedAt
        }