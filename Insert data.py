import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Iphone12345",
    database="emp"

)

run = db.cursor()

run.execute("INSERT INTO student (name, age, department) VALUES (%s, %s, %s)", ("John Doe", 22, "Computer Science"))
db.commit()

print("Data inserted successfully.")