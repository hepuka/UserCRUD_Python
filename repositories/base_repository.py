from abc import ABC
from config.database import db

class BaseRepository(ABC):

    def __init__(self, collection_name: str, model_class):
        self.collection = db[collection_name]
        self.model_class = model_class

    def get_all(self):
        documents = self.collection.find({}, {"_id": 0})
        return [self.model_class(doc) for doc in documents]

    def find_by_field(self, field: str, value):
        data = self.collection.find_one({field: value}, {"_id": 0})
        return self.model_class(data) if data else None

    def create(self, data: dict):
        self.collection.insert_one(data)

    def update(self, field: str, value, updates: dict):
        result = self.collection.update_one(
            {field: value},
            {"$set": updates}
        )

    def delete(self, field: str, value):
        self.collection.delete_one({field: value})
