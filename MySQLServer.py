import mysql.connector
from mysql.connector import Error

# Database configuration (update with your MySQL credentials)
DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = "Rockitwell@30"
DB_NAME = "alx_book_store"

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    
    if connection.is_connected():
        cursor = connection.cursor()
        
        # Create database if not exists
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store")
        print(f"Database '{DB_NAME}' created successfully!")
        
except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")

finally:
    # Close the connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")