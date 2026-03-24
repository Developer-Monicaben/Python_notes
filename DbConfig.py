# pip install mysql-connector-python
import mysql.connector

# Establish the connection to MySQL without selecting a database first
conn = mysql.connector.connect(host="localhost", user="root", password="password")
cursor1 = conn.cursor()

# Create the database if it doesn't already exist
cursor1.execute("CREATE DATABASE IF NOT EXISTS my_database")

# Now, select the created database
conn.database = "my_database"

# Create a table (if it doesn't exist)
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30),
    age INT
);
"""
cursor1.execute(create_table_query)
cursor1.execute("SELECT * FROM users")
# Close the cursor and connection
cursor1.close()
conn.close()
