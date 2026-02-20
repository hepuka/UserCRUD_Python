from repositories.user_repository import UserRepository
from services.user_service import UserService
from services.auth_service import AuthService
from controllers.user_controller import UserController
from controllers.auth_controller import AuthController
from views.login_view import LoginView
from views.main_menu import MainMenu

def main():
    while True:
        # Repository
        user_repository = UserRepository()

        # Services
        user_service = UserService(user_repository)
        auth_service = AuthService(user_repository)

        # Controllers
        user_controller = UserController(user_service)
        auth_controller = AuthController(auth_service)

        # LOGIN
        login_view = LoginView(auth_controller)
        user = login_view.show()

        # MAIN MENU
        main_menu = MainMenu(user, user_controller)
        logout = main_menu.show()

        if logout:
            continue
        else:
            break

if __name__ == "__main__":
    main()
