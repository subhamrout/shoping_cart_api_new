# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:22:48 2019

@author: Subham Rout
"""

import sqlite3

connection = sqlite3.connect('data.db')
cursor =  connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS shoppings (id INTEGER PRIMARY KEY,name text,price real)"

cursor.execute(create_table)

query = [('bata shoe',39.45),('classmate copy',12.45),('dettole handwash',10.43),('one plus 5t',100.67),('hp laptop',250.56),
         ('cracking the coding interview book',33.45),('watter bottle',26.780),('blackberry shirt',45.67),('rolex watch',450.00),
         ('school bag',60.67),
         ('5 star chocolate',5.67)]


insert = "INSERT INTO shoppings VALUES (NULL,?,?)"


cursor.executemany(insert,query)

select_query = "SELECT * FROM shoppings"

for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()
 
    
    