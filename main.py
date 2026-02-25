from controllers.order_controller import OrderController
from controllers.product_controller import ProductController
from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository
from repositories.user_repository import UserRepository
from services.order_service import OrderService
from services.product_service import ProductService
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
        product_repository = ProductRepository()
        order_repository = OrderRepository()


        # Services
        user_service = UserService(user_repository)
        auth_service = AuthService(user_repository)
        product_service = ProductService(product_repository)
        order_service = OrderService(order_repository)

        # Controllers
        user_controller = UserController(user_service)
        auth_controller = AuthController(auth_service)
        product_controller = ProductController(product_service)
        order_controller = OrderController(order_service)

        # LOGIN
        login_view = LoginView(auth_controller)
        user = login_view.show()

        # MAIN MENU
        main_menu = MainMenu(user, user_controller, product_controller, order_controller)
        logout = main_menu.show()

        if logout:
            continue
        else:
            break

if __name__ == "__main__":
    main()
