import bcrypt


class AuthService:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def login(self, username, password):

        user = self.user_repository.find_by_username(username)

        if not user:
            return False, None, "Hibás felhasználónév vagy jelszó."

        if not bcrypt.checkpw(password.encode(), user.password.encode()):
            return False, None, "Hibás felhasználónév vagy jelszó."

        return True, user, "Sikeres bejelentkezés."
