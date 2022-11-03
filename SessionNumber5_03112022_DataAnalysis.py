#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Useful imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# הצגת כל המידע הגרפי בתוך חוברת העבודה בה אנחנו עובדים
get_ipython().run_line_magic('matplotlib', 'inline')
#seaborn - טעינת מאגר מידע לבדיקות מתוך עולם ה
# ניטרול הודעות שגיאה 
import warnings
warnings.filterwarnings("ignore")


# File to download
# https://raw.githubusercontent.com/edelmanarik/DataVisualFri/main/northwindDataBase.xlsx

# In[ ]:


DataTest_P=pd.read_excel('https://raw.githubusercontent.com/edelmanarik/DataVisualFri/main/northwindDataBase.xlsx',sheet_name='Products')
DataTest_S=pd.read_excel('https://raw.githubusercontent.com/edelmanarik/DataVisualFri/main/northwindDataBase.xlsx',sheet_name='Suppliers')
DataTest_OD=pd.read_excel('https://raw.githubusercontent.com/edelmanarik/DataVisualFri/main/northwindDataBase.xlsx',sheet_name='OrderDetails')


# In[ ]:


DataTest_S.head()


# In[ ]:


SupandPro=DataTest_S.merge(DataTest_P, left_on='supplierID', right_on='supplierID')
SupandPro=SupandPro[['companyName','productID','productName','unitPrice']]
SupandPro.groupby('companyName').count()['productName']


# In[ ]:


for i in SupandPro['companyName'].unique():
    C1=SupandPro['companyName']==i
#     print(i)
    SupandPro.loc[C1].to_csv(i + '.csv')


# In[ ]:


# SQL : EDELMANARIKOFFI\SQLEXPRESS
# https://www.hedaro.com/blog/pandas-sql.html


# In[ ]:


import pandas as pd
import pyodbc
import sys


# In[39]:


# parameters
DB = {'servername': 'EDELMANARIKOFFI\SQLEXPRESS','database': 'NorthWind'}
# create the connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + DB['servername'] + ';DATABASE=' + DB['database'] + ';Trusted_Connection=yes')
# query db
sql = """
SELECT E.LastName + ' ' + E.FirstName as FullName,
       dateDiff(Year,E.birthdate,getdate()) as Age
FROM Employees as E 
"""
df = pd.read_sql(sql, conn)
df


# In[41]:


# Exam 2:
sql = """
SELECT E.LastName + ' ' + E.FirstName as FullName,
       Sum(O.freight) as SumfFreight
FROM Employees as E inner join orders as O 
on E.employeeid=o.employeeid
group by E.LastName + ' ' + E.FirstName
"""
df = pd.read_sql(sql, conn)
df.head()


# In[37]:


df.info()


# In[ ]:


df2 = pd.DataFrame({'key':['a','a','b'],
                    'val':[435,7,6],
                    'Mark':[90,67,45]
                   })
df2


# In[ ]:


from sqlalchemy import create_engine
# parameters
DB = {'servername': 'EDELMANARIKOFFI\SQLEXPRESS','database': 'NorthWind','driver': 'driver=SQL Server Native Client 11.0'}
# create the connection
engine = create_engine('mssql+pyodbc://' + DB['servername'] + '/' + DB['database'] + "?" + DB['driver'])
# add table to sql server
df2.to_sql('test', index=False, con=engine)
print('Worked!')


# In[ ]:




