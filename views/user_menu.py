from views.base_menu import BaseMenu
from controllers.user_controller import UserController

class UserMenu(BaseMenu):

    def __init__(self, user, user_controller):
        super().__init__(user_controller)
        self.logged_user = user
        self.user_controller = user_controller

    def show(self):
        menu = {
            "1": ("Saját adatok megtekintése", self.my_profile),
            "2": ("Saját adatok módosítása", self.edit_my_profile),
            "3": ("Jelszómódosítás", self.reset_password),
            "4": ("Logout", self.logout),
            "0": ("Kilépés", self.exit_app)
        }

        self.run(menu, "FELHASZNÁLÓ MENÜ")
        return True

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

        self.logged_user = self.user_controller.update_user(
            user,
            name or user.name,
            email or user.email,
            user.role
        )

        print("Adatok frissítve!")