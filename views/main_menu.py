from datetime import datetime
from repositories.user_repository import UserRepository
from views.base_menu import BaseMenu
import bcrypt

class MainMenu(BaseMenu):

    def show(self):
        menu = {
            "1": ("Új felhasználó hozzáadása", self.add_user),
            "2": ("Felhasználók listázása", self.get_users),
            "3": ("Felhasználó keresése", self.get_user),
            "4": ("Felhasználó adatainak módosítása", self.edit_user),
            "5": ("Felhasználó törlése", self.delete_user),
            "6": ("Jelszómódosítás", self.reset_password),
            "0": ("Kilépés", self.exit_app)
        }

        self.run(menu, "FŐMENÜ")

    def add_user(self):
        name = input("Név: ")
        email = input("Email: ")
        username = input("Felhasználónév: ")
        password = input("Jelszó: ")
        tmp = input("Szerepkör: (1)user (2)admin:")
        role = "user" if tmp == "1" else "admin"
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
        print(f"Felhasználó sikeresen létrehozva. Név: {user_data['name']} ")

    def get_user(self):
        username = input("Add meg a felhasználónevet: ")
        user = UserRepository.find_by_username(username)

        if not user:
            print("Felhasználó nem található!")
            return

        print("\n--- Felhasználó adatai ---")
        print(f"Név: {user.name}")
        print(f"Email: {user.email}")
        print(f"Szerepkör: {user.role}")
        print(f"Felhasználónév: {user.username}")
        print(f"Létrehozva: {user.createdAt}")
        print(f"Módosítva: {user.modifiedAt or '-'}")

    def get_users(self):
        users = UserRepository.get_all()

        if not users:
            print("\nNincs rögzített felhasználó!")
            return

        print("\nREGISZTRÁLT FELHASZNÁLÓK")
        print(
            f"{'Név'.ljust(20)} | "
            f"{'Email'.ljust(20)} | "
            f"{'Szerepkör'.ljust(10)} | "
            f"{'Felhasználónév'.ljust(20)} | "
            f"{'Létrehozva'.ljust(20)} | "
            f"{'Módosítva'.ljust(20)}"
        )

        for u in users:
            print(
                f"{(u.name or '').ljust(20)} | "
                f"{(u.email or '').ljust(20)} | "
                f"{(u.role or '').ljust(10)} | "
                f"{(u.username or '').ljust(20)} | "
                f"{(u.createdAt or '').ljust(20)} | "
                f"{(u.modifiedAt or '-').ljust(20)}"
            )

    def edit_user(self):
        username = input("Add meg a felhasználónevet: ")
        user = UserRepository.find_by_username(username)

        if not user:
            print("Felhasználó nem található!")
            return

        print("\n--- Felhasználó adatainak módosítása ---")
        print("(Enter = a megadott adat változatlan marad)\n")

        name = input(f"Név [{user.name}]: ").strip()
        email = input(f"Email [{user.email}]: ").strip()
        role_tmp = input(f"Szerepkör: (1)user (2)admin [{user.role}]: ").strip()
        role = user.role

        if role_tmp == "1":
            role = "user"
        elif role_tmp == "2":
            role = "admin"

        updates = {}
        if name:
            updates["name"] = name
        if email:
            updates["email"] = email
        if role:
            updates["role"] = role

        updates["username"] = user.username
        updates["createdAt"] = user.createdAt
        updates["modifiedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        UserRepository.update_user(user.username, updates)
        print("A felhasználó adatai sikeresen módosítva!")

    def delete_user(self):
        username = input("Add meg a törlendő felhasználó felhasználónevét: ")
        user = UserRepository.find_by_username(username)

        if not user:
            print("Nincs ilyen regisztrált felhasználó.")
            return False

        tmp = input("Biztosan törölni szeretnéd a felhasználót? (I) Igen (N) Mégsem: ").lower()
        if tmp == "i":
            UserRepository.delete_user(username)
            print("Felhasználó sikeresen törölve")
            return True
        else:
            print("Felhasználó törlése megszakítva.")
            return False

    def reset_password(self):
        user_tmp = input("Add meg a felhasználónevet: ")
        user = UserRepository.find_by_username(user_tmp)

        if not user:
            print("Felhasználó nem található!")
            return

        current_password = input("Add meg a jelenlegi jelszavad: ")

        if not bcrypt.checkpw(current_password.encode(), user.password.encode()):
            print("Helytelen jelszó!")
            return

        new_password = input("Add meg az új jelszavad: ")
        new_password_again = input("Add meg az újra az új jelszavad: ")

        if new_password != new_password_again:
            print("A megadott jelszavak nem egyeznek!")
            return

        new_hashed_password = bcrypt.hashpw(
            new_password.encode(),
            bcrypt.gensalt()
        ).decode()

        updates = {
            "password": new_hashed_password,
            "modifiedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        UserRepository.update_user(user.username, updates)
        print("A felhasználó jelszava sikeresen módosítva!")