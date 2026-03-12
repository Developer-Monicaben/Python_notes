# DELETE FROM `user` WHERE `user`.`id` = 3


import mysql.connector

host="localhost"
user="root"
password="*30Pm28*"
dbname="Pydb"

conn = mysql.connector.connect(host=host,user=user,password=password,database=dbname)

name=str(input("Enter delete userName: "))

cursor=conn.cursor()
query="DELETE FROM user1 WHERE user1.name = %s"
val=(name,)
cursor.execute(query,val)
conn.commit()
print("delete data successfully")