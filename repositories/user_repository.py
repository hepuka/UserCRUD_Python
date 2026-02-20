from config.database import users_collection
from models.user_model import User

class UserRepository:

    @staticmethod
    def get_all():
        users = users_collection.find({}, {"_id": 0})
        return [User(u) for u in users]

    @staticmethod
    def find_by_username(username: str):
        data = users_collection.find_one({"username": username}, {"_id": 0})
        return User(data) if data else None

    @staticmethod
    def create_user(user_data: dict):
        users_collection.insert_one(user_data)

    @staticmethod
    def update_user(username: str, updates: dict):
        users_collection.update_one(
            {"username": username},
            {"$set": updates}
        )

    @staticmethod
    def delete_user(username: str):
        users_collection.delete_one({"username": username})