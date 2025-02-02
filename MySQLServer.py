import mysql.connector
from mysql.connector import Error

# Database configuration details
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Kirigo@99',
    'db_name': 'alx_book_store'
}

# Connect to the MySQL database
try:
    connection = mysql.connector.connect(**db_config)
    
    if connection.is_connected():
        cursor = connection.cursor()
        
        # Create the database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_config['db_name']}")
        print(f"Database {db_config['db_name']} created successfully.")
        
except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")
    
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")