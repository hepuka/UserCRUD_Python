from controllers.auth_controller import AuthController

class LoginView:

    def show(self):
        while True:
            print("\n------ BEJELENTKEZÉS ------")

            username = input("Felhasználónév: ")
            password = input("Jelszó: ")

            success, user, message = AuthController.login(username, password)

            if success:
                print(message)
                return user

            print(message)
