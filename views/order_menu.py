from views.base_menu import BaseMenu

class OrderMenu(BaseMenu):

    def __init__(self, logged_user, user_controller, product_controller):
        super().__init__(logged_user, user_controller, product_controller)

    def show(self):
        menu = {
            "1": ("Rendelések listázása", self.get_orders),
            "2": ("Visszalépés a főmenübe", self.back_to_prev_menu),
            "0": ("Kilépés", self.exit_app)
        }
        return self.run(menu, "RENDELÉSEK MENÜ")

    def get_orders(self):
        print("Rendelések listázása...")