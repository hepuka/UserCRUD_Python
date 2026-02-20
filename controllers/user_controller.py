from controllers.base_controller import BaseController


class UserController(BaseController):

    def __init__(self, service):
        super().__init__(service)

    def create(self, data):
        self.service.create(data)

    def get_user(self, username):
        return self.service.get_by_field("username", username)

    def update_user(self, user, name, email, role):
        updates = {
            "name": name or user.name,
            "email": email or user.email,
            "role": role or user.role
        }
        self.service.update("username", user.username, updates)

        updated_user = self.get_user(user.username)
        return updated_user

    def reset_password(self, user, current_password, new_password, new_password_again):
        return self.service.reset_password(user, current_password, new_password, new_password_again)
