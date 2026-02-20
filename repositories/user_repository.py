from repositories.base_repository import BaseRepository
from models.user_model import User

class UserRepository(BaseRepository):

    def __init__(self):
        super().__init__("users", User)

    def find_by_username(self, username):
        return self.find_by_field("username", username)
