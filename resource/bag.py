# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:05:40 2019

@author: Subham Rout
"""

from flask_restful import Resource
from flask_jwt import jwt_required
from models.bag import BagModel
from models.shopping import ShoppingModel
import global_var

class Bag(Resource):
    @jwt_required()
    def get(self,name):
        item = BagModel.find_by_name(name)
        
        if item:
            return item.json()
        else:
            return {"Message":"No item of this name is present in the bag"}
    
    @jwt_required()
    def post(self,name):
        item = ShoppingModel.find_by_name(name)
        if item:
            temp_item = BagModel.find_by_name(name)
            if temp_item:
                bag = BagModel(item.name,item.price,temp_item.quantity +1)
                bag.save_to_db()
            else:
                bag = BagModel(item.name,item.price,1)
                bag.save_to_db()
            global_var.total += item.price    
            return {"Message": "item added sucessfully"}    
        else:
            return {"Message":"There is no item of the current name exist"}
        
    @jwt_required()   
    def delete(self,name):
        item = BagModel.find_by_name(name)
        if item:
            try:
                global_var.total -= item.price
                item.delete_from_db()
                
            except:
                return {"Message":"Error occured while removing item from the bag"}
            
        else:
            return {"Message":"No item of this name exist in the bag"}
        
        return {"Message": "Item removed from the bag"}

class Bag_List(Resource):
    def get(self):
        return {"items": [item.json() for item in BagModel.find_all()],'total':global_var.total}
    
    
class Bag_Bill(Resource):
    @jwt_required()
    def get(self):
        items = BagModel.find_all()
        BagModel.delete_all()
        tot = global_var.total
        global_var.total = 0
        return {"Bill": [item.json() for item in items],'total':tot}        
    
    
        
        
        
        
        
        
        
        