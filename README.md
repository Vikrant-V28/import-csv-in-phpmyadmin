<div align="center">
  <img height="60" src="https://user-images.githubusercontent.com/85709371/155844936-1206011d-4a78-4277-936d-b1e0fc776161.png">
  <img height="60" src="https://user-images.githubusercontent.com/85709371/155845012-4b0b2841-61a3-434b-adac-918b9c683b95.png">
  <img height="60" src="https://user-images.githubusercontent.com/85709371/155844988-b88c879e-dade-408b-8842-a2b6aa2647a6.png">
</div>

# How to connect to mysql, create a table using python and import the csv file into mysql ?

## System requirements :
Install the pydrive python module as follows :

* pip install mysql-connector-python or pip install PyMySQL (phpMyAdmin)
* pip install pandas

The below codes can be run in Jupyter notebook , or any python console


### Step 1: Prepare the CSV File

To begin, prepare the CSV file that you'd like to import to MySQL. For example, I prepared a simple CSV file with the following data:

![Screenshot (138)](https://user-images.githubusercontent.com/85709371/146887468-78fff29a-4f94-45a9-b385-9015f373cbdf.png)

Note: the above employee csv data is taken from the below link <a href="https://www.briandunning.com/sample-data/">employee_data</a>

### Step 2: Import the CSV File into the DataFrame.
Next, import the CSV file into Python using the pandas library. Here is the code that I used to import the CSV file, and then create the DataFrame. You'll need to change the path name to reflect the location where the CSV file is stored on your computer

```python
import pandas as pd
empdata = pd.read_csv('C:\\Users\\XXXXX\\emp.csv', index_col=False, delimiter = ',')
empdata.head()
```
#### Output of the above code:

![Screenshot (139)](https://user-images.githubusercontent.com/85709371/146893846-aad5d2c4-62cc-41e1-8164-082c296a2e16.png)

Also you can read the data from CSV File by using

```python
data = pd.read_csv('emp.csv')
df = pd.DataFrame(data)
print(df)
```
#### Output of the above code:

![Screenshot (140)](https://user-images.githubusercontent.com/85709371/146894479-69c42b4f-56dc-4af9-89d6-a94f4d23abdc.png)

### Step 3 : Connect to the MySQL using Python and create a Database
Create a connection object to connect to MySQL.
```python
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
```
#### Output of the above code:

![Screenshot (141)](https://user-images.githubusercontent.com/85709371/146895770-405c598f-e98f-47a2-8b85-0db97dfd188d.png)

### Step 4 : Create a table and Import the CSV data into the MySQL table with Timestamp

```python
import os
import pymysql
import pandas as pd
import datetime;

# Timestamp
ct = datetime.datetime.now()
print("current time:-", ct)

# Import CSV
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
# timestamp
ct = datetime.datetime.now()
print("current time:-", ct) 
ts = ct.timestamp()
print("timestamp:-", ts)
```
#### Output of the above code:

![Screenshot (142)](https://user-images.githubusercontent.com/85709371/146897059-8d72b135-49d4-49a0-b012-3aa138f08e08.png)

#### Output from Database:

![Screenshot (137)](https://user-images.githubusercontent.com/85709371/146897154-f94fb37b-1cea-4065-a3b1-52c274fb04fd.png)

### Step 5 : Query the Table
Query the table to make sure that our inserted data has been saved correctly.


## Execute query
```python
sql = "SELECT * FROM csv.employee_data"
cursor.execute(sql)
# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)
```

#### Output of the Above code:

![Screenshot (144)](https://user-images.githubusercontent.com/85709371/146897800-1b9b2f3d-be91-40ee-a908-b40818256592.png)

## *Author Name*
[Vikrant](https://github.com/thevkrant)
