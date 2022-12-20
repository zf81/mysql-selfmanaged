#import packages
from sqlalchemy import create_engine
import pandas as pd
import pymysql

#Connecting to mysql
MYSQL_HOSTNAME  
MYSQL_USER 
MYSQL_PASSWORD 
MYSQL_DATABASE 


connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
connection_string 

db = create_engine(connection_string)

query = 'select * from db3.table1;'
query

df = pd.read_sql(query, con=db)

#Inserting a new table to database
real_df = pd.read_csv('/Users/fizzahzaidi/Documents/development/python_projects/mysql-selfmanaged/ACPs_Lung_cancer.csv')

real_df.to_sql('new_table', con=db, if_exists='replace')