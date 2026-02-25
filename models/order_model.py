
class Order:

    def __init__(self, data: dict):
        self.user_id = data.get("user_id")
        self.products = data.get("products", [])
        self.total = data.get("total")
        self.status = data.get("status")
        self.createdAt = data.get("createdAt")

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "products": self.products,
            "total": self.total,
            "status": self.status,
            "createdAt": self.createdAt
        }