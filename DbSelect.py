import mysql.connector
host="localhost"
user="root"
password="password"
database="Pydb"

conn=mysql.connector.connect(host=host,user=user,password=password,database=database)
cursor=conn.cursor()
query="Select * from user1;"
cursor.execute(query)
result=cursor.fetchall()

for data in result :
    print(data)
