#pip install sqlalchemy alembic mysql-connector-python pymysql
#pip install python-dotenv
#pip install pymysql
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
def create_rows_faker(engine, num_MRN=50, num_procedures=50):
    with engine.connect() as connection:
        for _ in range(num_MRN):
            first_name:fake.first_name()
            last_name:fake.last_name()
            patient_number:fake.license_plate()
            query = connection.execute(text(f"INSERT INTO patient_contact (first_name, last_name, patient_number) VALUES ('{first_name}', '{last_name}', '{patient_number}')")

        # #Fetch patient mrn (db schema updated to autoincrement for MRN=primary key)
        #     mrn_ids = [row[0] for row in connection.execute(text("SELECT mrn FROM patient_contact")).fetchall()]

        #     diagnosis = ['E11.9', 'S06.0X1A', 'G44.311', 'M54.2', 'M99.01']

        # for _ in range(num_procedures):
        #     visit_id = random.randint(10000,99999)
        #     mrn = random.choice(mrn_ids)
        #     diagnosis_code = random.choice(diagnosis)
        #     physician_name = fake.name()
        #     query2 = connection.execute(text(f"INSERT INTO procedure_hx (visit_id, mrn, diagnosis_code, physician_name) VALUES ('{visit_id}', '{mrn}', '{diagnosis_code}', '{physician_name})"))
        #     connection.commit()


#test data insertion
#pd.read_sql("SELECT * FROM patient_contact LIMIT 5;", engine)

#if __name__ == "__main__":
#    create_rows_faker(engine)
#    print("Fake data insertion complete!")
