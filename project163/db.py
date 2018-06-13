import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
cursor = c.execute("SELECT * from question")

for row in cursor:
    print(row[0], row[1], row[2])
