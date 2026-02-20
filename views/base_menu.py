import sys

class BaseMenu:

    def run(self, menu: dict, title: str):
        while True:
            print(f"\n----- {title.upper()} -----")

            for key, (desc, _) in menu.items():
                print(f"({key}) {desc}")

            print("------------------------------")

            choice = input("Választott menüpont: ")
            action = menu.get(choice)

            if action:
                action[1]()
            else:
                print("Érvénytelen menüpont!")

    @staticmethod
    def exit_app():
        print("Kilépés...")
        sys.exit(0)