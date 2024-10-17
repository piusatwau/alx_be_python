# Connecting to an SQL Database

import mysql.connector

mydb = mysql.connector.connect(
    
    host="localhost",
    user="root",
    password="72527",
    database="Employees"   
    
)

# print(mydb.get_server_info())

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

all_databases = mycursor.fetchall()

for database in all_databases:
    print(database)

mycursor.execute("USE sql_inventory")


# print(all_databases)
