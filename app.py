# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:54:51 2019

@author: Subham Rout
"""

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from resource.user import UserRegister
from resource.bag import Bag,Bag_List,Bag_Bill
from resource.shopping import Shopping_List
import global_var

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
app.secret_key = "SuBhAm$RoUt"

jwt = JWT(app,authenticate,identity)

global_var.init()
api.add_resource(Bag,'/bag/<string:name>')
api.add_resource(Bag_List,'/bags')
api.add_resource(UserRegister,'/Register')
api.add_resource(Bag_Bill,'/getbill')
api.add_resource(Shopping_List,'/ship_list')



if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug = True)
    
