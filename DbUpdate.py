# UPDATE `user` SET `name` = 'fooboo' WHERE `user`.`id` = 2;

import mysql.connector

host="localhost"
user="root"
password="password"
dbname="Pydb"

conn = mysql.connector.connect(host=host,user=user,password=password,database=dbname)


cursor=conn.cursor()
NewValue=str(input("Enter the updated value :"))
OldValue=str(input("Enter the old value :"))

query="update user1 set name=%s where name=%s ;"
val=(NewValue,OldValue)
cursor.execute(query,val)
conn.commit()
print("Update data successfully")
