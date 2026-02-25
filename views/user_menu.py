from views.base_menu import BaseMenu

class UserMenu(BaseMenu):

    def __init__(self, logged_user,  user_controller, product_controller, order_controller):
        super().__init__(logged_user,user_controller, product_controller, order_controller)
        self.logged_user = logged_user
        self.user_controller = user_controller
        self.product_controller = product_controller
        self.order_controller = order_controller

    def show(self):
        menu = {
            "1": ("Felhasználókezeló menü", self.navigate_to_userhandling_menu),
            "2": ("Termék menü", self.navigate_to_product_menu),
            "3": ("Rendelések menü", self.navigate_to_order_menu),
            "4": ("Kijelentkezés", self.logout),
            "0": ("Kilépés", self.exit_app)
        }

        self.run(menu, "FELHASZNÁLÓ MENÜ")
        return True

