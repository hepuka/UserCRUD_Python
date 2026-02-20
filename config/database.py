from pymongo import MongoClient, errors
import certifi

class Database:
    _client = None
    _db = None

    @classmethod
    def connect(cls):
        if cls._client:
            return cls._db

        MONGO_URI = (
            "mongodb+srv://kavezo:rkPLxRSJSpcSjeap@cluster0.q7veg.mongodb.net/"
            "bank_app?retryWrites=true&w=majority&appName=bank_app"
        )

        try:
            cls._client = MongoClient(
                MONGO_URI,
                tls=True,
                tlsCAFile=certifi.where(),
                serverSelectionTimeoutMS=5000
            )

            cls._client.server_info()
            cls._db = cls._client["CRUD_Python"]

            print("\n--- Kapcsolat az adatbázissal létrejött ---")

            return cls._db

        except errors.ServerSelectionTimeoutError as e:
            raise RuntimeError(
                "Nem sikerült csatlakozni a MongoDB Atlas-hoz. "
            ) from e

db = Database.connect()

users_collection = db["users"]
