from repository.user_repository import UserRepository
from model.user import User

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def update_user(self, user: User):
        self.user_repository.update_user(user)

    def delete_user(self, user_id: str):
        self.user_repository.delete_user(user_id)

    def get_history(self, user: User):
        return self.user_repository.get_history(user)

    def get_age(self, user: User, current_year: int):
        return self.user_repository.get_age(user, current_year)
