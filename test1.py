import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine
import faker 
import numpy as np
from dotenv import load_dotenv
from pandas import read_sql
import random
from faker import Faker
import os

load_dotenv('.env')

fake = Faker()

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connect to the database
connectionString = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'

# Test connection
engine = create_engine(connectionString)
connection = engine.connect()

# Try and read tables data from the database
tables = pd.read_sql("SHOW TABLES", connection)

# Try and query patient_contact table
patient_contact = pd.read_sql("SELECT * FROM patient_contact", connection)

mrn_ids = []
for _ in range(100):
    mrn_ids.append(random.randint(1000000, 9999999))
print (mrn_ids)

mrn_id = pd.DataFrame(mrn_ids, columns=['mrn'])

# Try and insert in dummy data with first_name, last_name, patient_number
dummyData_df = pd.DataFrame(
    {
        'mrn' : [6085168,7078057],
        'first_name': ['John', 'Jane'],
        'last_name': ['Doe', 'Doe'],
        'patient_number': ['1234567890', '0987654321']
    }
)
print(dummyData_df)

# Send dummy data to patient_contact table
dummyData_df.to_sql('patient_contact', con=connection, if_exists='append', index=False)

## try and read patient_contact table again
patient_contact = pd.read_sql("SELECT * FROM patient_contact", connection)


## ------- Real data --------
## now create larger fake df using faker 
fake_df = pd.DataFrame(
    {
        'first_name': [fake.first_name() for _ in range(100)],
        'last_name': [fake.last_name() for _ in range(100)],
        'patient_number': [fake.random_number(digits=10) for _ in range(100)]
    }
)

#insert mrn into fake_df
patient_df = pd.concat([mrn_id, fake_df], axis=1)

## send fake df to patient_contact table
patient_df.to_sql('patient_contact', con=connection, if_exists='append', index=False)

## read patient_contact table again
patient_contact = pd.read_sql("SELECT * FROM patient_contact", connection)
print(patient_contact)

#test data insertion
pd.read_sql("SELECT * FROM patient_contact LIMIT 5;", engine)

# ----------- procedure-hx table ------- #

# Try and query procedure_hx table
procedure_history = pd.read_sql("SELECT * FROM procedure_hx", connection)

# Try and insert in dummy data with 
dummyData_df2 = pd.DataFrame(
    {
        'visit_id': ['123234133', '1234235'],
        'mrn' : [1004919,1017481],
        'diagnosis_code': ['Dx21', 'Dx23'],
        'physician_name': ['Charles Dorn', 'Matthew Pratt']
    }
)
print(dummyData_df2)

# Send dummy data to procedure_hx table
dummyData_df2.to_sql('procedure_hx', con=connection, if_exists='append', index=False)

## try and read table again
procedure_history = pd.read_sql("SELECT * FROM procedure_hx", connection)

#fake diagnosis data
diagnosis = ['E11.9', 'S06.0X1A', 'G44.311', 'M54.2', 'M99.01']

## now create larger fake df using faker 
fake_df2 = pd.DataFrame(
    {
        'visit_id': [fake.random_number(digits=5) for _ in range(100)],
        'diagnosis_code': [random.choice(diagnosis) for _ in range(100)],
        'physician_name': [fake.name() for _ in range(100)]
    }
)

#insert mrn into fake_df2
procedure_df = pd.concat([mrn_id, fake_df2], axis=1)

## send fake df to procedure_hx table
procedure_df.to_sql('procedure_hx', con=connection, if_exists='append', index=False)

## read patient_contact table again
procedure_history = pd.read_sql("SELECT * FROM procedure_hx", connection)
print(procedure_history)

#test data insertion
pd.read_sql("SELECT * FROM procedure_hx LIMIT 5;", engine)

connection.close()