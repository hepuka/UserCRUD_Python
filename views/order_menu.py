from views.base_menu import BaseMenu
from bson import ObjectId

class OrderMenu(BaseMenu):

    def __init__(self, logged_user, user_controller, product_controller, order_controller):
        super().__init__(logged_user, user_controller, product_controller, order_controller)
        self.logged_user = logged_user
        self.user_controller = user_controller
        self.product_controller = product_controller
        self.order_controller = order_controller

    def show(self):
        menu = {
            "1": ("Új rendelés felvétele", self.create_order),
            "2": ("Rendelések listázása", self.get_orders),
            "3": ("Visszalépés a főmenübe", self.back_to_prev_menu),
            "0": ("Kilépés", self.exit_app)
        }
        return self.run(menu, "RENDELÉSEK MENÜ")

    def get_orders(self):
        print("Rendelések listázása...")

    def create_order(self):
        if not isinstance(self.logged_user._id, ObjectId):
            self.logged_user._id = ObjectId(self.logged_user._id)

        order_data = {
            "user_id": self.logged_user._id,
            "table_number": input("Asztalszám: "),
            "products": [],
            "total": 0,
            "status": "pending",
        }

        self.order_controller.create(order_data)
