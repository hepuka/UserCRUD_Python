from views.base_menu import BaseMenu
from bson import ObjectId

class OrderMenu(BaseMenu):

    def __init__(self, logged_user, user_controller, product_controller, order_controller):
        super().__init__(logged_user, user_controller, product_controller, order_controller)
        self.logged_user = logged_user
        self.user_controller = user_controller
        self.product_controller = product_controller
        self.order_controller = order_controller

    status_map = {
        "n": "Nyitott",
        "f": "Fizetve",
    }

    def show(self):
        menu = {
            "1": ("Új rendelés felvétele", self.create_order),
            "2": ("Rendelések listázása", self.get_orders),
            "3": ("Visszalépés a főmenübe", self.back_to_prev_menu),
            "0": ("Kilépés", self.exit_app)
        }
        return self.run(menu, "RENDELÉSEK MENÜ")

    def get_orders(self):
        print("\nRendelés állapota:")
        print("(N) Nyitott")
        print("(F) Fizetve")
        print("(Enter) Összes")

        status_input = input("Melyik rendelési állapotot szeretnéd megjeleníteni? ").strip().lower()

        if status_input == "":
            orders = self.order_controller.get_all()
        elif status_input in self.status_map:
            orders = self.order_controller.get_by_status(self.status_map[status_input])
        else:
            print("Érvénytelen státusz!")
            return

        if not orders:
            print("\nNincs rögzített rendelés!")
            return

        # Fejléc
        print("\nRÖGZÍTETT RENDELÉSEK")
        header = (
            f"{'Rendelés ideje'.ljust(20)} | "
            f"{'Rendelés módosítva'.ljust(20)} | "
            f"{'Asztalszám'.ljust(12)} | "
            f"{'Rendelés állapota'.ljust(12)} | "
            f"{'Végösszeg'.ljust(10)} | "
            f"{'Felszolgáló ID'.ljust(24)} | "
            f"Rendelés részletei"
        )
        print(header)
        print("-" * 130)

        for order in orders:

            if hasattr(order, 'products') and order.products:
                products_str = ", ".join(
                    f"{p.get('name', '').capitalize()} x{p.get('quantity', 0)} "
                    f"(Ár: {p.get('unit_price', 0)} Ft, Összesen: {p.get('total_price', 0)} Ft)"
                    for p in order.products
                )
            else:
                products_str = "-"

            print(
                f"{(order.createdAt or '').ljust(20)} | "
                f"{(order.modifiedAt or '-').ljust(20)} | "
                f"{(order.table_number or '').ljust(12)} | "
                f"{(order.status or '').ljust(12)} | "
                f"{(str(order.total) or '0').ljust(10)} | "
                f"{(str(order.user_id) if order.user_id else '').ljust(24)} | "
                f"{products_str}"
            )

    def create_order(self):
        if not isinstance(self.logged_user._id, ObjectId):
            self.logged_user._id = ObjectId(self.logged_user._id)

        order_data = {
            "user_id": self.logged_user._id,
            "table_number": input("Asztalszám: "),
            "products": [],
            "total": 0,
            "status": "nyitott",
        }

        self.order_controller.create(order_data)
