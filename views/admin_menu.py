from views.base_menu import BaseMenu
from views.product_menu import ProductView
from views.userhandling_menu import UserHandlingMenu


class AdminMenu(BaseMenu):

    def __init__(self, user,user_controller, product_controller):
        super().__init__(user_controller, product_controller)
        self.logged_user = user

    def show(self):
        menu = {
            "1": ("Felhasználókezelő menü", self.navigate_to_userhandling_menu),
            "2": ("Termékmenü", self.navigate_to_product_menu),
            "3": ("Rendelések", self.orders),
            "4": ("Üzleti összesítő", self.get_business_details),
            "5": ("Jelszómódosítás", self.reset_password),
            "6": ("Logout", self.logout),
            "0": ("Kilépés", self.exit_app)
        }

        self.run(menu, "ADMIN MENÜ")
        return True

    def navigate_to_product_menu(self):
        product_view = ProductView(self.user_controller, self.product_controller)
        product_view.show()


    def navigate_to_userhandling_menu(self):
        userhandling_view = UserHandlingMenu(self.user_controller, self.product_controller)
        userhandling_view.show()

    def orders(self):
        pass

    def get_business_details(self):
        products = self.product_controller.get_all()
        orders = None
        income = None

        # Értékek előkészítése
        values = {
            "Összes megrendelés": f"{orders or 0} darab",
            "Összes bevétel": f"{income or 0} Ft",
            "Termékek száma": f"{len(products)} darab"
        }

        print("\nÜZLETI ÖSSZESÍTŐ")

        column_widths = {}

        for key, value in values.items():
            column_widths[key] = max(len(key), len(value)) + 4

        header = " | ".join(
            key.ljust(column_widths[key])
            for key in values.keys()
        )
        print(header)
        print("-" * len(header))

        row = " | ".join(
            value.ljust(column_widths[key])
            for key, value in values.items()
        )
        print(row)
