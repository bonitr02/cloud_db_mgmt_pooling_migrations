#pip install python-dotenv
#pip install pymysql
# pip install sqlalchemy alembic mysql-connector-python
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

load_dotenv('.env')

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patient_contact'
#Added autoincrement
    mrn = Column(Integer, primary_key=True, autoincrement=True) #randint
    first_name = Column(String(50), nullable=False) #faker
    last_name = Column(String(50), nullable=False) #faker
    patient_number = Column(String(15)) #faker

    records = relationship('Procedure_History', back_populates='patient')

class Procedure_History(Base):
    __tablename__ = 'procedure_hx'

    visit_id = Column(Integer, primary_key=True) #randint
    mrn = Column(Integer, ForeignKey('patient_contact.mrn'), nullable=False) #randint
    diagnosis_code = Column(String(100), nullable=False) # randint
    physician_name = Column(String(200), nullable=False) #faker name

    patient = relationship('Patient', back_populates='records')


### Part 2 - initial sqlalchemy-engine to connect to db:

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

## Test connection

inspector = inspect(db_engine)
inspector.get_table_names()

### Part 3 - create the tables using sqlalchemy models, with no raw SQL required:

Base.metadata.create_all(db_engine)
