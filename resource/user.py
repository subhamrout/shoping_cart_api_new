# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:44:17 2019

@author: Subham Rout
"""

from flask_restful import Resource,reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',type=str,
                                   required = True,help = "This field cannot left blank")
    parser.add_argument('password',type=str,
                                   required = True,help = "This field cannot left blank")

    def post(self):
        data =  UserRegister.parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user:
            return {"Message":"The user already registered"}
        
        user = UserModel(**data)
        user.save_to_db()
        
        return {"Message":"User Registration sucessful"}
    