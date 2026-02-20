import bcrypt
from repositories.user_repository import UserRepository

class AuthService:

    @staticmethod
    def login(username: str, password: str):
        user = UserRepository.find_by_username(username)

        if not user:
            return False, None, "Hibás felhasználónév vagy jelszó."

        if not bcrypt.checkpw(password.encode(), user.password.encode()):
            return False, None, "Hibás felhasználónév vagy jelszó."

        return True, user, "Sikeres bejelentkezés."
