import os
from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey, text, insert
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import random
import faker
from faker import Faker
from dotenv import load_dotenv
from pandas import read_sql
import pandas as pd
import sqlite3

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
engine = create_engine(conn_string, echo=False)

# Create a Faker instance
fake = Faker()

# Create fake data for patient_contact table
range_ofnumbers = range(50)

def create_rows_faker(engine, num_MRN=range_ofnumbers):
    with engine.connect() as connection:
        for x in num_MRN:
            print(x)
            first_name = fake.first_name()
            print(first_name)
            last_name = fake.last_name()
            patient_number = fake.license_plate()
            query = (f"INSERT INTO patient_contact (first_name, last_name, patient_number) VALUES ('{first_name}', '{last_name}', '{patient_number}');")
            print(query)
            connection.execute(text(query))

create_rows_faker(engine)

#test data insertion
pd.read_sql("SELECT * FROM patient_contact LIMIT 5;", engine)