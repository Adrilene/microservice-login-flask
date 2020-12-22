from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "db": "users",
    "host": "mongodb+srv://adrilene:arq2201@cluster0.a3msk.mongodb.net/test?authSource=admin&replicaSet=atlas-2nqljv-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
}
db = MongoEngine(app)
api = Api(app)
CORS(app)
bcrypt = Bcrypt(app)
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)


from .models import users_model
from .services import users_service
from .controllers import users_many_controller
