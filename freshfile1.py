import mysql.connector

host="localhost"
user="root"
password="*30Pm28*"
databasename="IPL"

use=mysql.connector.connect(host=host,user=user,password=password,database=databasename)

oldname=input("Enter the player's old name:")
newname=input("Enter the new name:")
# # age=int(input("Enter the player's age:"))
# state=input("Enter the palyer's state:")

cursor=use.cursor()
query="update teams set name=%s where teams.name=%s;"
val=(newname,oldname)
cursor.execute(query,val)
use.commit()
print("data updated successfully")





