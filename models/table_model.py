
class Table:

    def __init__(self, data: dict):
        self.number = data.get("number")
        self.status = data.get("status")
        self.createdAt = data.get("createdAt")

    def to_dict(self):
        return {
            "number": self.number,
            "status": self.status,
            "createdAt": self.createdAt
        }