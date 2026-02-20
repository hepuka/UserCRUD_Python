import bcrypt
from datetime import datetime
from services.base_service import BaseService


class UserService(BaseService):

    def __init__(self, repository):
        super().__init__(repository)

    def create_user(self, data):
        hashed = bcrypt.hashpw(
            data["password"].encode(),
            bcrypt.gensalt()
        ).decode()

        data["password"] = hashed
        data["createdAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.repository.create(data)

    def reset_password(self, user, current_password, new_password, new_password_again):

        if not user:
            return False, "Felhasználó nem található."

        if not bcrypt.checkpw(current_password.encode(), user.password.encode()):
            return False, "Helytelen jelenlegi jelszó."

        if new_password != new_password_again:
            return False, "Az új jelszavak nem egyeznek."

        if not new_password.strip():
            return False, "Az új jelszó nem lehet üres."

        if bcrypt.checkpw(new_password.encode(), user.password.encode()):
            return False, "Az új jelszó nem lehet azonos a régivel."

        new_hashed = bcrypt.hashpw(
            new_password.encode(),
            bcrypt.gensalt()
        ).decode()

        updates = {
            "password": new_hashed,
            "modifiedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.repository.update("username", user.username, updates)

        return True, "Jelszó sikeresen módosítva!"
