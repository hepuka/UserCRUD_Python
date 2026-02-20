import sys

class BaseMenu:

    def run(self, menu: dict, title: str):
        while True:
            print(f"\n----- {title.upper()} -----")
            print(f"Bejelentkezve: {self.logged_user.username} ({self.logged_user.role})\n")

            for key, (desc, _) in menu.items():
                print(f"({key}) {desc}")

            print("------------------------------")

            choice = input("Választott menüpont: ")
            action = menu.get(choice)

            if action:
                result = action[1]()

                if choice in ["7", "4"]:  # logout opciók
                    return
            else:
                print("Érvénytelen menüpont!")

    @staticmethod
    def exit_app():
        print("Kilépés...")
        sys.exit(0)