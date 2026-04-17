import mysql.connector

conn = mysql.connector.connect(
    host="localhost",     # ✅ only host
    port=3306,            # ✅ port separately
    user="root",
    password="Srivarsha@1234",
    database="d12"
)

print("Connected successfully!")