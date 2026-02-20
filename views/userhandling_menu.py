from views.base_menu import BaseMenu

class UserHandlingMenu(BaseMenu):

    def show(self):
        menu = {
            "1": ("Új felhasználó hozzáadása", self.add_user),
            "2": ("Felhasználók listázása", self.get_users),
            "3": ("Felhasználó keresése", self.get_user),
            "4": ("Felhasználó módosítása", self.edit_user),
            "5": ("Felhasználó törlése", self.delete_user),
            "6": ("Visszalépés a főmenübe", self.back_to_prev_menu),
            "0": ("Kilépés", self.exit_app)
        }

        return self.run(menu, "TERMÉKMENÜ")

    def add_user(self):
        name = input("Név: ")
        email = input("Email: ")
        username = input("Felhasználónév: ")
        password = input("Jelszó: ")
        tmp = input("Szerepkör: (1)user (2)admin:")
        role = "user" if tmp == "1" else "admin"

        self.user_controller.create({
            "name": name,
            "email": email,
            "username": username,
            "password": password,
            "role": role
        })

        print("Felhasználó létrehozva!")

    def get_user(self):
        username = input("Add meg a felhasználónevet: ")
        user = self.user_controller.get_user(username)

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