from model.database import Database
from model.user import User


class UserRepository:
    def __init__(self):
        self.database = Database()

    def create_user(self, user: User):
        self.database.save(user.user_id, user)

    def update_user(self, user: User):
        if self.database.get(user.user_id):
            self.database.save(user.user_id, user)
        else:
            print("User not found")

    def delete_user(self, user_id: str):
        self.database.delete(user_id)

    def get_user(self, user_id: str):
        return self.database.get(user_id)

    def get_history(self, user: User):
        # Заглушка для получения истории пользователя
        return f"History for user {user.name}"

    def get_age(self, user: User, current_year: int):
        return user.get_age(current_year)
