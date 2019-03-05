# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:51:40 2019

@author: Subham Rout
"""

from db import db

class ShoppingModel(db.Model):
    __tablename__ = 'shoppings'
    id = db.Column('id',db.Integer,primary_key=True)
    name = db.Column('name',db.String(80))
    price = db.Column('price',db.Float(precision=2))
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
  
    def json(self):
        return {'name':self.name,'price':self.price}
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_name(cls,name):
        item = cls.query.filter_by(name = name).first()
        return item
    
    def add_product(self):
        db.session.add(self)
        db.session.commit()
        
