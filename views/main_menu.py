from controllers.user_controller import UserController
from views.base_menu import BaseMenu

class MainMenu(BaseMenu):

    def __init__(self, user):
        self.logged_user = user

        print(f"Bejelentkezve: {user.name} ({user.role})\n")

    def show(self):

        if self.logged_user.role == "admin":
            menu = self.admin_menu()
        else:
            menu = self.user_menu()

        self.run(menu, "FŐMENÜ")
        return True

    def admin_menu(self):
        return {
            "1": ("Új felhasználó hozzáadása", self.add_user),
            "2": ("Felhasználók listázása", self.get_users),
            "3": ("Felhasználó keresése", self.get_user),
            "4": ("Felhasználó módosítása", self.edit_user),
            "5": ("Felhasználó törlése", self.delete_user),
            "6": ("Jelszómódosítás", self.reset_password),
            "7": ("Logout", self.logout),
            "0": ("Kilépés", self.exit_app)
        }

    def user_menu(self):
        return {
            "1": ("Saját adatok megtekintése", self.my_profile),
            "2": ("Saját adatok módosítása", self.edit_my_profile),
            "3": ("Jelszómódosítás", self.reset_password),
            "4": ("Logout", self.logout),
            "0": ("Kilépés", self.exit_app)
        }


    def add_user(self):
        name = input("Név: ")
        email = input("Email: ")
        username = input("Felhasználónév: ")
        password = input("Jelszó: ")
        tmp = input("Szerepkör: (1)user (2)admin:")
        role = "user" if tmp == "1" else "admin"

        UserController.create_user({
            "name": name,
            "email": email,
            "username": username,
            "password": password,
            "role": role
        })

        print("Felhasználó létrehozva!")

    def get_user(self):
        username = input("Add meg a felhasználónevet: ")
        user = UserController.get_user(username)

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
        users = UserController.get_all_users()

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
        user = UserController.get_user(username)

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

        UserController.update_user(user, name, email, role)
        print("A felhasználó adatai sikeresen módosítva!")

    def delete_user(self):
        username = input("Add meg a törlendő felhasználó felhasználónevét: ")
        tmp = input("Biztosan törölni szeretnéd a felhasználót? (I) Igen (N) Mégsem: ").lower()

        if tmp == "i":
            UserController.delete_user(username)
            print("Felhasználó sikeresen törölve")
            return True
        else:
            print("Felhasználó törlése megszakítva.")
            return False

    def reset_password(self):
        username = input("Add meg a felhasználónevet: ")
        user = UserController.get_user(username)

        if not user:
            print("Felhasználó nem található!")
            return

        current_password = input("Add meg a jelenlegi jelszavad: ")
        new_password = input("Add meg az új jelszavad: ")
        new_password_again = input("Add meg ismét az új jelszavad: ")

        success, message = UserController.reset_password(user, current_password, new_password, new_password_again)
        print(message)

    def logout(self):
        print("Sikeres kijelentkezés.")
        return

    def my_profile(self):
        user = self.logged_user

        print("\n--- Saját adatok ---")
        print(f"Név: {user.name}")
        print(f"Email: {user.email}")
        print(f"Felhasználónév: {user.username}")
        print(f"Szerepkör: {user.role}")
        print(f"Profil létrehozva: {user.createdAt}")
        print(f"Profil módosítva: {user.modifiedAt}")


    def edit_my_profile(self):
        user = self.logged_user

        name = input(f"Név [{user.name}]: ").strip()
        email = input(f"Email [{user.email}]: ").strip()

        UserController.update_user(
            user,
            name or user.name,
            email or user.email,
            user.role
        )

        print("Adatok frissítve!")
