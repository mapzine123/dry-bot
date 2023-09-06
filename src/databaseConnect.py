import os
import mysql.connector

DB_USER = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_DATABASE = os.environ.get('DB_DATABASE')

config = {
    'user': DB_USER,
    'password': DB_PASSWORD,
    'host': DB_HOST,
    'port': DB_PORT,
    'database': DB_DATABASE
}

conn = mysql.connector.connect(**config)

cursor = conn.cursor()

cursor.execute("SELECT admin_no FROM admin")
rows = cursor.fetchall()

for row in rows:
    print(row[0])


conn.close()
