from services.user_service import UserService


class UserController:

    @staticmethod
    def create_user(data):
        UserService.create_user(**data)

    @staticmethod
    def get_user(username):
        return UserService.get_user(username)

    @staticmethod
    def get_all_users():
        return UserService.get_all_users()

    @staticmethod
    def update_user(user, name, email, role):
        UserService.update_user(user, name, email, role)

    @staticmethod
    def delete_user(username):
        UserService.delete_user(username)

    @staticmethod
    def reset_password(user, current_password, new_password, new_password_again):
        return UserService.reset_password(user, current_password, new_password, new_password_again)
