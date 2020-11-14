import sqlite3
connection = sqlite3.connect("employee_detials.db")
print("Database opened successfully")
cursor = connection.cursor()
#delete
#cursor.execute('''DROP TABLE Employee_Info;''')
connection.execute("create table Employee_Info (id INTEGER PRIMARY KEY AUTOINCREMENT , name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, gender TEXT NOT NULL, contact TEXT UNIQUE NOT NULL, dob TEXT NOT NULL, year TEXT NOT NULL, salary TEXT NOT NULL, dept TEXT NOT NULL, address TEXT NOT NULL)")
print("Table created successfully")
connection.close()   
