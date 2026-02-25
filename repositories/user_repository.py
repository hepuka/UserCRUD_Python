from repositories.base_repository import BaseRepository
from models.user_model import User

class UserRepository(BaseRepository):

    def __init__(self):
        super().__init__("users", User)

    def find_by_username(self, username):
        data = self.collection.find_one({"username": username})
        if not data:
            return None
        return User(data)
