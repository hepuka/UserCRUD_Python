from views.base_menu import BaseMenu

class AdminMenu(BaseMenu):

    def __init__(self, logged_user, user_controller, product_controller):
        super().__init__(logged_user, user_controller, product_controller)
        self.logged_user = logged_user

    def show(self):
        menu = {
            "1": ("Felhasználókezelő menü", self.navigate_to_userhandling_menu),
            "2": ("Termék menü", self.navigate_to_product_menu),
            "3": ("Rendelések menü", self.navigate_to_order_menu),
            "4": ("Üzleti összesítő", self.get_business_details),
            "5": ("Jelszómódosítás", self.reset_password),
            "6": ("Kijelentkezés", self.logout),
            "0": ("Kilépés", self.exit_app)
        }

        self.run(menu, "ADMIN MENÜ")
        return True

    def orders(self):
        pass

    def get_business_details(self):
        products = self.product_controller.get_all()

        orders = 0
        income = 0

        stats = {
            "Összes megrendelés": f"{orders} db",
            "Összes bevétel": f"{income} Ft",
            "Termékek száma": f"{len(products)} db"
        }

        print("\n" + "=" * 82)
        print("BUSINESS DASHBOARD".center(82))
        print("=" * 82)

        GREEN = "\033[92m"
        RED = "\033[91m"
        RESET = "\033[0m"

        if income > 0:
            stats["Összes bevétel"] = GREEN + stats["Összes bevétel"] + RESET
        else:
            stats["Összes bevétel"] = RED + stats["Összes bevétel"] + RESET

        col_width = max(
            max(len(key) for key in stats.keys()),
            max(len(str(value)) for value in stats.values())
        ) + 6

        total_width = col_width * len(stats) + (len(stats) - 1) * 3

        print("+" + "-" * (total_width + 2) + "+")

        header = " | ".join(key.center(col_width) for key in stats.keys())
        print("| " + header + " |")

        print("+" + "-" * (total_width + 2) + "+")

        row = " | ".join(str(value).rjust(col_width) for value in stats.values())
        print("| " + row + " |")

        print("+" + "-" * (total_width + 2) + "+")

        print("\nTOP 5 TERMÉK (példa-order_qty berakni a termékekhez):")
        top_products = products[:5]

        if not top_products:
            print("Nincs termék adat.")
        else:
            for i, product in enumerate(top_products, 1):
                print(f"{i}. {product.name.capitalize()}")


