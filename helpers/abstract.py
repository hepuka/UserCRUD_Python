
class AbstractRepository:
    def __init__(self, collection):
        self.collection = collection

    def get_all(self, classname):
        data = self.collection.find({}, {"_id": 0})
        return [classname(obj) for obj in data]


    def find_by_property(self,prop: str, value:str, classname):
        data = self.collection.find_one({prop: value}, {"_id": 0})
        return classname(data) if data else None

    def create_item(self, data: dict):
        self.collection.insert_one(data)

    def update_item(self,prop: str, value:str, updates: dict):
        self.collection.update_one(
            {prop: value},
            {"$set": updates}
        )

    def delete_user(self,prop: str, value:str,):
        self.collection.delete_one({prop: value})