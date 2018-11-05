import pandas as pd
from sqlalchemy import engine

engine = engine.create_engine('mysql+pymysql://root:123@localhost:3306/psl')
sql = 'select * from stu'

df = pd.read_sql_query(sql, engine)
df['datetime_str'] = df['datetime_str'].map(str)
print(df['datetime_str'])
# df['datetime_str'] = df['datetime_str'].str.strip()
print(df['datetime_str'])
df['datetime_str'] = pd.to_datetime(df['datetime_str'])

df.to_sql('stu1', engine)
print(df)