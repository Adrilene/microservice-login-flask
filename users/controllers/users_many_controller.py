from flask import request
from users.services.users_service import (
  get_user_by_email,
  insert_user,
  insert_user_agent,
  get_user_by_user_agent,
  delete_user_agent
)
# from flask import Response, request
from users.models.users_model import User
from flask_jwt_extended import create_access_token
from flask_restful import Resource 
from users import api
import json
import requests
import random
import datetime


class SignupApiController(Resource):
    def post(self):
        body = request.get_json()
        user_id = insert_user(body)
        return {"id": user_id}, 200


class LoginApiController(Resource):
    def post(self):
        body = request.get_json()
        user = get_user_by_email(body['email']) 
        authorized = user.check_password(body['password'])
        insert_user_agent(user, request.headers.get('User-Agent'))

        if not authorized:
            return {'error': 'Email or password invalid'}, 401
        
        expires = datetime.timedelta(days=1)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {'token': access_token, '_id': str(user.id)}, 200
    
    def delete(self):
        user = get_user_by_user_agent(request.headers.get('User-Agent'))
        delete_user_agent(user)
        return 'OK', 200


class UserDataController(Resource):
    def get(self):
        user = get_user_by_user_agent(request.headers.get('User-Agent'))
        if user: 
            user = json.loads(user.to_json())
            return user, 200
        return {'msg': 'user not logged'}, 400


api.add_resource(SignupApiController, "/signup")
api.add_resource(LoginApiController, "/login")
api.add_resource(ProfileController, "/profile")
# api.add_resource(UserManyController, "/users")
# api.add_resource(UserManyVariedController, "/users_varied")
