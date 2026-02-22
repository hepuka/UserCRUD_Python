class User:

    display_fields = {
        "name": "Név",
        "email": "Email",
        "role": "Szerepkör",
        "username": "Felhasználónév",
        "createdAt": "Létrehozva",
        "modifiedAt": "Módosítva"
    }

    hidden_fields = ["_id", "password"]

    def __init__(self, data: dict):
        self.name = data.get("name")
        self.email = data.get("email")
        self.username = data.get("username")
        self.password = data.get("password")
        self.role = data.get("role")
        self.createdAt = data.get("createdAt")
        self.modifiedAt = data.get("modifiedAt")

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "role": self.role,
            "createdAt": self.createdAt,
            "modifiedAt": self.modifiedAt
        }

    @classmethod
    def get_display_fields(cls):
        return cls.display_fields

    @classmethod
    def get_hidden_fields(cls):
        return cls.hidden_fields
