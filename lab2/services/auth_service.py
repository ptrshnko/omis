from repository.user_repository import UserRepository
from model.user import User, Status

class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def login(self, user_id: str, password: str) -> Status:
        user = self.user_repository.get_user(user_id)
        if user and user.password == password:
            print(f"User {user.name} logged in successfully.")
            return user.status
        else:
            print("Invalid credentials.")
            return None

    def register(self, user: User) -> Status:
        existing_user = self.user_repository.get_user(user.user_id)
        if not existing_user:
            self.user_repository.create_user(user)
            print(f"User {user.name} registered successfully.")
            return user.status
        else:
            print("User already exists.")
            return None
