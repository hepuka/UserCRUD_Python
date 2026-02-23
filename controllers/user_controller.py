from controllers.base_controller import BaseController


class UserController(BaseController):

    def __init__(self, service):
        super().__init__(service)

    def get_user(self, username):
        return self.service.get_by_field("username", username)

    def get_by_email(self, email):
        return self.service.get_by_field("email", email)

    def update_user(self, user, name, email, role):
        updates = {
            "name": name or user.name,
            "email": email or user.email,
            "role": role or user.role
        }
        self.service.update("username", user.username, updates)
        return self.get_user(updates["username"])

    def reset_password(self, user, current_password, new_password, new_password_again):
        return self.service.reset_password(user, current_password, new_password, new_password_again)
