import sqlite3

conn = sqlite3.connect('database/database.db')
c = conn.cursor()
c.execute("CREATE TABLE students (UID text,student_name text, attendance text)")
print("A new Database is Created")
conn.commit()
conn.close()