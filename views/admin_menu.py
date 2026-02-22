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
            "3": ("Jelszómódosítás", self.reset_password),
            "4": ("Logout", self.logout),
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
