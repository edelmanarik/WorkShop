#!/usr/bin/env python
# coding: utf-8

# In[12]:


import sqlite3
conn = sqlite3.connect('L5DB') 
c = conn.cursor()
c.execute('''
          CREATE TABLE IF NOT EXISTS products
          ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTEGER)
          ''')
c.execute('''
          INSERT INTO products (product_id, product_name, price)
                VALUES
                (1,'Computer',800),
                (2,'Printer',200),
                (3,'Tablet',300),
                (4,'Desk',450),
                (5,'Chair',150),
                (6,'EBike',15000)
          ''')                     
conn.commit()


# In[13]:


import sqlite3
import pandas as pd

conn = sqlite3.connect('L5DB') 
sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM products
                               ''', conn)

df = pd.DataFrame(sql_query, columns = ['product_id', 'product_name', 'price'])
print (df)


# In[18]:


import sqlite3
import pandas as pd
conn = sqlite3.connect('L5DB') 
c = conn.cursor()
c.execute('''
          SELECT
          *
          FROM products
          ''')
df = pd.DataFrame(c.fetchall(), columns = ['product_id', 'product_name', 'price'])
max_price = df['price'].max()
print (f'max_price = {max_price}')
print()
print('All Data Base :')
print('===============')
print(df)

