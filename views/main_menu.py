from views.admin_menu import AdminMenu
from views.base_menu import BaseMenu
from views.user_menu import UserMenu


class MainMenu(BaseMenu):

    def __init__(self, logged_user, user_controller, product_controller, order_controller):
        super().__init__(logged_user, user_controller, product_controller, order_controller)
        self.logged_user = logged_user
        self.user_controller = user_controller
        self.product_controller = product_controller
        self.order_controller = order_controller

        print(f"Bejelentkezve: {logged_user.name} ({logged_user.role})\n")

    def show(self):

        if self.logged_user.role == "admin":
            menu = AdminMenu(self.logged_user, self.user_controller, self.product_controller)
        else:
            menu = UserMenu(self.logged_user, self.user_controller, self.product_controller, self.order_controller)

        return menu.show()

