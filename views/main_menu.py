from views.admin_menu import AdminMenu
from views.base_menu import BaseMenu
from views.user_menu import UserMenu


class MainMenu(BaseMenu):

    def __init__(self, user, user_controller):
        super().__init__(user_controller)
        self.logged_user = user
        self.user_controller = user_controller

        print(f"Bejelentkezve: {user.name} ({user.role})\n")

    def show(self):

        if self.logged_user.role == "admin":
            menu = AdminMenu(self.logged_user, self.user_controller)
        else:
            menu = UserMenu(self.logged_user, self.user_controller)

        return menu.show()





