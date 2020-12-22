from users.models.users_model import User
from flask_bcrypt import generate_password_hash, check_password_hash
from users.models.users_model import User

def insert_user(body):
    user = User(**body)
    user.hash_password()
    user.save()
    return str(user.id)

def get_user_by_email(email):
    return User.objects.get(email=email)

def insert_user_agent(user, user_agent):
    user.update(set__user_agent=user_agent)

def get_user_by_user_agent(user_agent):
    return User.objects.get(user_agent=user_agent)

def delete_user_agent(user):
    user.update(set__user_agent='')