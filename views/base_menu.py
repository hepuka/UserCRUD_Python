import sys

class BaseMenu:

    def __init__(self, user_controller):
        self.user_controller = user_controller

    def run(self, menu: dict, title: str):
        while True:
            print(f"\n----- {title.upper()} -----")

            for key, (desc, _) in menu.items():
                print(f"({key}) {desc}")

            print("------------------------------")

            choice = input("Választott menüpont: ")
            action = menu.get(choice)

            if action:
                result = action[1]()

                if result is True:
                    return True

                if result is False:
                    import sys
                    sys.exit(0)

            else:
                print("Érvénytelen menüpont!")

    def logout(self):
        print("Sikeres kijelentkezés.")
        return True

    def reset_password(self):
        username = input("Add meg a felhasználónevet: ")
        user = self.user_controller.get_user(username)

        if not user:
            print("Felhasználó nem található!")
            return

        current_password = input("Add meg a jelenlegi jelszavad: ")
        new_password = input("Add meg az új jelszavad: ")
        new_password_again = input("Add meg ismét az új jelszavad: ")

        success, message = self.user_controller.reset_password(user, current_password, new_password, new_password_again)
        print(message)

    def back_to_prev_menu(self):
        print("Visszalépés az előző menübe...")
        return True

    @staticmethod
    def exit_app():
        print("Kilépés...")
        sys.exit(0)