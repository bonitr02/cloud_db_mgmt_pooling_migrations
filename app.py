#pip install sqlalchemy alembic mysql-connector-python pymysql
#pip install python-dotenv
#pip install pymysql
#pip install mysql
#pip install mysql-connector-python
import os
from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import random
import faker
from faker import Faker
from dotenv import load_dotenv
from pandas import read_sql
from flask import Flask, render_template
import pandas as pd
from sqlite3 import connect

load_dotenv('.env')  # Load environment variables from .env file

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)

def get_tables(engine):
    """Get list of tables."""
    inspector = inspect(engine)
    return inspector.get_table_names()

def execute_query_to_dataframe(query: str, engine):
    """Execute SQL query and return result as a DataFrame."""
    return read_sql(query, engine)

# Example usage
tables = get_tables(db_engine)
print("Tables in the database:", tables)

sql_query = "SELECT * FROM patient_contact"  # Modify as per your table
df = execute_query_to_dataframe(sql_query, db_engine)
#print(df)

sql_query2 = "SELECT * FROM procedure_hx"  # Modify as per your table
df2 = execute_query_to_dataframe(sql_query2, db_engine)
#rint(df2)

# Flask App 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

sqldb1 = df.to_html('mysqldata.html')
sqldb2 = df2.to_html('mysqldata2.html')

@app.route('/mysqldata')
def mysqldata(sqldata=df):
    return render_template('mysqldata.html', sqldata=df)

@app.route('/mysqldata2')
def mysqldata2(sqldata=df2):
    return render_template('mysqldata2.html', sqldata=df2)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )