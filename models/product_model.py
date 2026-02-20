class Product:
    def __init__(self, data: dict):
        self.name = data.get("name")
        self.price = data.get("price")
        self.packaging = data.get("packaging")
        self.category = data.get("category")
        self.createdAt = data.get("createdAt")
        self.modifiedAt = data.get("modifiedAt")

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "packaging": self.packaging,
            "category": self.category,
            "createdAt": self.createdAt,
            "modifiedAt": self.modifiedAt
        }
