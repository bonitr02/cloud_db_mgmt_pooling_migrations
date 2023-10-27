# Databases Part 4c Assignment: Cloud Database Management with Connection Pooling and Migrations

## 1. Connection Pooling Setup:

Azure setup
1. Sign into portal.azure.com 
2. Navigate to applications > Azure Database for MySQL flexible servers 
3. Ensure student resource group is chosen as the subscription for the application
4. Create instance and follow the provided instructions to ensure the lowest monthly payment possible:

    
        Azure Database for MySQL
        Deployment option: Flexible,
        Tier: Burstable
        Compute: B1S [$6.21 p/month] or B1MS [$12.41 p/month]


5. Under networking, ensure IP address 0.0.0.0 is included and public access is checked off
6. Under server parameters, change connect_timeout to 3 and max_connections to 20
7. Configured security settings to disable expectation of encryption.

GCP setup 
1. After logging into console.cloud.google, select the student resource group
2. Select SQL > MySQL from the sidebar menu
3. Create instance and follow the provided instructions to ensure the lowest monthly payment possible:
        
        
        DB-standard-1 (vCPU 1, RAM 3.75gb)
        10gb storage
        No backups [$9.37 month]


4. Under authorized networks, add the IP address of 0.0.0.0/0 


## 2a. Database Schema and Data:
-Database riannemigration1 created with tables patient_contact and procedure_hx
    - no errors found upon initial database and table creation

Initial schema with column headers only and no errors:
![Picture2](/az/images/FirstDatabaseSchema_Creation_noerrors.png "Text to show on mouseover") 

-Used faker and random to populate table with data
    - errors found:
        1. initially unable to update fake data to  "connection.execute(f"INSERT INTO  " string not being recognized. Troubleshooted by creating fake data tables and converting/uploading to sql schemas

Unable to Connect error:
![Picture7](/az/images/Unabletoconnect_MySQL.png "Text to show on mouseover")

Database schema:
![Picture5](/az/images/Table1_fakedata.png "Text to show on mouseover")
![Picture6](/az/images/Table2_fakedata.png "Text to show on mouseover")

## 2b. Using MySQL Workbench to Generate ERD:
        1. Reverse engineer schema error, resulting in only one table being loaded onto the schema. Databases both are populated with fake data.

Schema error
![Picture4](/az/images/SCHEMA_error.png "Text to show on mouseover")

Resulting schema
![Picture3](/az/images/Resulting_Schema.png "Text to show on mouseover")

## 3. SQLAlchemy and Flask Integration:
        1. Flask application not loading due to missing connection from mysql. Tested mysql connection which is still active.

## 4. Database Migrations with Alembic: