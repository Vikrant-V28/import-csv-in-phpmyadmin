# connection to mysql using python
# create a table
# import the csv file into mysql

# System requirements :
Install the pydrive python module as follows :
pip install mysql-connector-python or pip install PyMySQL (phpMyAdmin)
pip install pandas

The below codes can be run in Jupyter notebook , or any python console


# Step 1: Prepare the CSV File
To begin, prepare the CSV file that you'd like to import to MySQL. For example, I prepared a simple CSV file with the following data:
![Screenshot (138)](https://user-images.githubusercontent.com/85709371/146887468-78fff29a-4f94-45a9-b385-9015f373cbdf.png)
Note: the above employee csv data is taken from the below link <a href="https://www.briandunning.com/sample-data/">employee_data</a>

# Step 2: Import the CSV File into the DataFrame.
Next, import the CSV file into Python using the pandas library. Here is the code that I used to import the CSV file, and then create the DataFrame. You'll need to change the path name to reflect the location where the CSV file is stored on your computer

<blockquote style=color:'red'>
import pandas as pd
empdata = pd.read_csv('C:\\Users\\XXXXX\\emp.csv', index_col=False, delimiter = ',')
empdata.head()
</blockquote>

Output of the above code:
![Screenshot (139)](https://user-images.githubusercontent.com/85709371/146893846-aad5d2c4-62cc-41e1-8164-082c296a2e16.png)

Also you can read the data from CSV File by using

<blockquote style=color:'red'>
data = pd.read_csv('emp.csv')
df = pd.DataFrame(data)
print(df)
</blockquote>
![Screenshot (140)](https://user-images.githubusercontent.com/85709371/146894479-69c42b4f-56dc-4af9-89d6-a94f4d23abdc.png)

# Step 3 : Connect to the MySQL using Python and create a Database
Create a connection object to connect to MySQL.
<blockquote style=color:'red'>
import pandas as pd
empdata = pd.read_csv('C:\\Users\\XXXXX\\emp.csv', index_col=False, delimiter = ',')
empdata.head()
</blockquote>
