class LoginView:

    def __init__(self, auth_controller):
        self.auth_controller = auth_controller

    def show(self):
        while True:
            print("\n------ BEJELENTKEZÉS ------")

            username = "felszolgalo1" #input("Felhasználónév: ")
            password = "12345" #input("Jelszó: ")

            success, user, message = self.auth_controller.login(username, password)

            if success:
                print(message)
                return user

            print(message)
