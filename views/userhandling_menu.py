from views.base_menu import BaseMenu

class UserHandlingMenu(BaseMenu):

    role_map = {
        "u": "user",
        "a": "admin",
    }

    field_labels = {
        "name": "Név",
        "email": "Email",
        "role": "Szerepkör",
        "username": "Felhasználónév",
        "createdAt": "Létrehozva",
        "modifiedAt": "Módosítva"
    }

    def show(self):
        menu = {
            "1": ("Felhasználók listázása", self.get_users),
            "2": ("Felhasználó keresése", self.get_user),
            "3": ("Új felhasználó hozzáadása", self.add_user),
            "4": ("Felhasználó módosítása", self.edit_user),
            "5": ("Felhasználó törlése", self.delete_user),
            "6": ("Visszalépés a főmenübe", self.back_to_prev_menu),
            "0": ("Kilépés", self.exit_app)
        }

        return self.run(menu, "TERMÉKMENÜ")

    def add_user(self):
        name = input("Név: ")
        print("Szerepkörtök:")
        print("(U) User")
        print("(A) Admin")
        role_input = input("Válassz szerepkört: ").strip().lower()
        role = self.role_map.get(role_input)
        email = input("Email: ")
        username = input("Felhasználónév: ")
        password = input("Jelszó: ")

        self.user_controller.create({
            "name": name,
            "email": email,
            "username": username,
            "password": password,
            "role": role
        })

        print("Felhasználó létrehozva!")

    def get_user(self):
        search_value = input("Add meg a felhasználónevet vagy email címet: ").strip()

        if "@" in search_value:
            user = self.user_controller.get_by_email(search_value)
        else:
            user = self.user_controller.get_user(search_value)

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
        users = self.user_controller.get_all()

        if not users:
            print("\nNincs rögzített felhasználó!")
            return

        print("\nREGISZTRÁLT FELHASZNÁLÓK")

        display_fields = users[0].get_display_fields()
        hidden_fields = users[0].get_hidden_fields()

        keys = [
            key for key in vars(users[0]).keys()
            if key not in hidden_fields
        ]

        width = 20

        header = " | ".join(
            display_fields.get(key, key).ljust(width)
            for key in keys
        )
        print(header)
        print("-" * len(header))

        for user in users:
            row = " | ".join(
                str(getattr(user, key, "-") or "-").ljust(width)
                for key in keys
            )
            print(row)

    def edit_user(self):
        username = input("Add meg a felhasználónevet: ")
        user = self.user_controller.get_user(username)

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

        self.user_controller.update_user(user, name, email, role)
        print("A felhasználó adatai sikeresen módosítva!")

    def delete_user(self):
        username = input("Add meg a törlendő felhasználó felhasználónevét: ")
        tmp = input("Biztosan törölni szeretnéd a felhasználót? (I) Igen (N) Mégsem: ").lower()

        if tmp == "i":
            self.user_controller.delete("username", username)
            print("Felhasználó sikeresen törölve")
            return
        else:
            print("Felhasználó törlése megszakítva.")
            return