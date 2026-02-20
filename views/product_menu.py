from views.base_menu import BaseMenu

class ProductView(BaseMenu):

    def show(self):
        menu = {
            "1": ("Új termékregisztráció", self.add_product),
            "2": ("Termék keresése", self.search_product),
            "3": ("Termék adatainak módosítása", self.edit_product),
            "4": ("Visszalépés a főmenübe", self.back_to_prev_menu),
            "0": ("Kilépés", self.exit_app)
        }

        return self.run(menu, "TERMÉKMENÜ")

    def add_product(self):
        print("Új termék regisztrálva (demo).")

    def search_product(self):
        print("Termék keresése (demo).")

    def edit_product(self):
        print("Termék adatainak módosítása (demo).")

