import pandas as pd
import numpy as np 
import sqlalchemy
import pymysql

df = pd.read_excel('pandas/test.xlsx', sheet_name=0, header=0)
print (df)
engine = sqlalchemy.create_engine('mysql+pymysql://root:123@localhost:3306/mysql?charset=utf8')
df.to_sql(df,engine,if_exists='append')






