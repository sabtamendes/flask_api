from src.repositories.user_repository import get_all_users, get_user_by_id, create_user, delete_user

def fetch_all_users():
    return get_all_users()

def fetch_user(user_id):
    return get_user_by_id(user_id)

def add_user(username, email):
    return create_user(username, email)

def remove_user(user_id):
    delete_user(user_id)
