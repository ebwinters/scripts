import sqlite3

conn = sqlite3.connect('data.db')

c = conn.cursor()

# c.execute('create table ex1(name varchar(10), price integer)')

c.execute("insert into ex1 values('Ethan', 20)")
conn.commit()