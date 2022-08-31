import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:progress@localhost:5432/employee", pool_recycle = 1)
db_engine = engine.connect()

with open('employee.csv', 'r') as file:
    data_df = pd.read_csv(file)
    data_df.to_sql('employee_data', con=engine, schema='public', if_exists = 'append')

engine.execute("SELECT * FROM employee_data").fetchall()

db_engine.close()
