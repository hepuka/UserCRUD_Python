from abc import ABC
from datetime import datetime

class BaseService(ABC):

    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_field(self, field, value):
        return self.repository.find_by_field(field, value)

    def create(self, data: dict):
        data["createdAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.repository.create(data)

    def update(self, field, value, updates: dict):
        updates["modifiedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.repository.update(field, value, updates)

    def delete(self, field, value):
        self.repository.delete(field, value)

    def get_many_by_field(self, field: str, value):
        return self.repository.find_many_by_field(field, value)
