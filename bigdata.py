#!/usr/bin/env python
# coding: utf-8

## Import the CSV File into the DataFrame.

import pandas as pd
empdata = pd.read_csv('C:\\Users\\XXXXX\\emp.csv', index_col=False, delimiter = ',')
empdata.head()

## Read file data in Jupyter Notenook

data = pd.read_csv('emp.csv')
df = pd.DataFrame(data)
print(df)

## Connect to the MySQL and create a Database

import os
import pymysql
import pandas as pd

host = os.getenv('MYSQL_HOST')
port = os.getenv('MYSQL_PORT')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
database = os.getenv('MYSQL_DATABASE')

conn = pymysql.connect(
    host="localhost",
    port=int(3306),
    user="root",
    passwd="",
    db="csv",
    charset='utf8mb4')

cursor = conn.cursor()
cursor.execute("select database();")
record = cursor.fetchone()
print("You're connected to database: ", record)
mydb.commit()
cursor.close()
print ("Done")


##  Create a table & Import the CSV data into the MySQL table with timestamp


import os
import pymysql
import pandas as pd
import datetime;

## Timestamp
ct = datetime.datetime.now()
print("current time:-", ct)

## Import CSV
data = pd.read_csv('emp.csv')
df = pd.DataFrame(data)

host = os.getenv('MYSQL_HOST')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
database = os.getenv('MYSQL_DATABASE')

conn = pymysql.connect(host="localhost",user="root",passwd="",db="csv",charset='utf8mb4')
cursor = conn.cursor()
cursor.execute("select database();")
record = cursor.fetchone()
print("You're connected to database: ", record)
cursor.execute('DROP TABLE IF EXISTS employee_data;')
cursor.execute("CREATE TABLE employee_data(first_name varchar(255),last_name varchar(255),company_name varchar(255),address varchar(255),city varchar(255),county varchar(255),state varchar(255),zip int,phone1 varchar(255),phone2 varchar(255),email varchar(255),web varchar(255))")
print("Table is created....") 

for i,row in data.iterrows():
    sql = "INSERT INTO csv.employee_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
conn.commit()

## timestamp
ct = datetime.datetime.now()
print("current time:-", ct) 
ts = ct.timestamp()
print("timestamp:-", ts)


## Query the Table

# Execute query
sql = "SELECT * FROM csv.employee_data"
cursor.execute(sql)
# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)
