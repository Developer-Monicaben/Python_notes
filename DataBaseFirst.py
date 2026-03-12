# pip install mysql-connector-python  -->need to download!

import mysql.connector

# Establish a connection to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="*30Pm28*"  # Replace with your MySQL password
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a new database named 'mydatabase'
cursor.execute("CREATE DATABASE mydatabase")

# Select the 'mydatabase' to use
cursor.execute("USE mydatabase")

# Define the SQL query to create a table
create_table_query = """
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    sex CHAR(1),
    income FLOAT
)
"""

# Execute the query to create the table
cursor.execute(create_table_query)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
print("Database and table created successfully.")
