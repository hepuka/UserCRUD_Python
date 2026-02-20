from views.login_view import LoginView
from views.main_menu import MainMenu

def main():
    while True:
        login_view = LoginView()
        user = login_view.show()

        menu = MainMenu(user)
        logout = menu.show()

        if not logout:
            break

if __name__ == "__main__":
    main()
