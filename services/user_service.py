from datetime import datetime
import bcrypt
from repositories.user_repository import UserRepository

class UserService:

    @staticmethod
    def create_user(name, email, username, password, role):
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        user_data = {
            "name": name,
            "email": email,
            "username": username,
            "password": hashed,
            "role": role,
            "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        UserRepository.create_user(user_data)

    @staticmethod
    def get_user(username):
        return UserRepository.find_by_username(username)

    @staticmethod
    def get_all_users():
        return UserRepository.get_all()

    @staticmethod
    def update_user(user, name, email, role):
        updates = {
            "name": name or user.name,
            "email": email or user.email,
            "role": role or user.role,
            "modifiedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        UserRepository.update_user(user.username, updates)

    @staticmethod
    def delete_user(username):
        UserRepository.delete_user(username)

    @staticmethod
    def reset_password(user, current_password, new_password, new_password_again):
        if not user:
            return False, "Felhasználó nem található."

        #Jelenlegi jelszó ellenőrzés
        if not bcrypt.checkpw(current_password.encode(), user.password.encode()):
            return False, "Helytelen jelenlegi jelszó."

        # Új jelszavak egyezése
        if new_password != new_password_again:
            return False, "Az új jelszavak nem egyeznek."

        # Üres jelszó tiltás
        if not new_password.strip():
            return False, "Az új jelszó nem lehet üres."

        # ne lehessen ugyanaz mint a régi
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

        UserRepository.update_user(user.username, updates)
        return True, "Jelszó sikeresen módosítva!"
