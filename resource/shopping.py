# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:11:27 2019

@author: Subham Rout
"""

from models.shopping import ShoppingModel
from flask_restful import Resource


class Shopping_List(Resource):
    
    def get(self):
        return {"items": [item.json() for item in ShoppingModel.find_all()]}
    