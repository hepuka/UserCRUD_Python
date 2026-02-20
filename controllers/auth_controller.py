from services.auth_service import AuthService

class AuthController:

    @staticmethod
    def login(username: str, password: str):
        return AuthService.login(username, password)
