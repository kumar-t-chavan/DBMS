import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Iphone12345",
    database="emp"
)

run = db.cursor()

run.execute("CREATE TABLE IF NOT EXISTS student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, department VARCHAR(255))")

print("Table created successfully.")