from users import db
from flask_bcrypt import generate_password_hash, check_password_hash


class User(db.Document):
    meta = {"collection": "users"}
    name = db.StringField(required=True)
    lastname = db.StringField(required=True)
    email = db.StringField(required=True)
    password = db.StringField(required=True)
    cpf = db.StringField(required=True)
    cellphone = db.StringField(required=True)
    address = db.StringField(required=True)
    number = db.IntField(required=True)
    city = db.StringField(required=True)
    state = db.StringField(required=True)
    user_agent = db.StringField(required=False)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)