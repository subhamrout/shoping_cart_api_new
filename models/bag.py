# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:29:34 2019

@author: Subham Rout
"""

from db import db
import sqlite3

class BagModel(db.Model):
    __tablename__ = 'bags'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    quantity = db.Column(db.Integer)
    
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def json(self):
        return {'name':self.name,'price':self.price,'quantity':self.quantity}
    
    @classmethod
    def delete_all(cls):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM bags"
        cursor.execute(query)
        connection.commit()
        connection.close()
        
        
        
    
    