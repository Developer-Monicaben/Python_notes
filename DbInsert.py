# pip install mysql-connector-python
import mysql.connector

host1="localhost"
user1="root"
password="password"
dbname="Pydb"

conn = mysql.connector.connect(host=host1,user=user1,password=password,database=dbname)

name=str(input("Enter Name: "))
email=str(input("Enter Email: "))
passwd=str(input("Enter Password: "))
address=str(input("Enter Addess: "))

cursor=conn.cursor()
query="INSERT INTO user1 (name,email,password,address) VALUES (%s,%s,%s,%s);"
val=(name,email,passwd,address)
cursor.execute(query,val)
conn.commit()
print("Insert data successfully")
