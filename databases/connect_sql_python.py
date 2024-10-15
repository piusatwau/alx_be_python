# Connecting to an SQL Database

import mysql.connector

mydb = mysql.connector.connect(
    
    host="localhost",
    user="root",
    password="72527",
    database="Employees"   
    
)

print(mydb.get_server_info())