from views.login_view import LoginView
from views.main_menu import MainMenu

def main():
    login_view = LoginView()
    user = login_view.show()

    menu = MainMenu(user)
    menu.show()

if __name__ == "__main__":
    main()
