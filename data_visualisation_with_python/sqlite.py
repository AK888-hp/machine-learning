import sqlite3


conn=sqlite3.connect('test.db')
cursor=conn.cursor()
# cursor.execute("CREATE TABLE employees (id INTEGER PRIMARY KEY, NAME TEXT,AGE INTEGER,DEPTARTMENT TEXT)")
# conn.commit()
# cursor. execute("INSERT INTO employees VALUES (?,?,?,?)", (1, 'John Doe', 30, 'IT'))
# conn.commit()
data=[(2, 'Jane Smith', 28, 'HR'), (3, 'Alice Johnson', 32, 'IT'), (4, 'Bob Brown', 25,"Manager"),(5,"Smitha",30,"Teacher")]
cursor.executemany("INSERT INTO employees VALUES (?,?,?,?)",data)
conn.commit()
print("Data inserted successfully")
cursor.execute("SELECT * FROM employees")
rows=cursor.fetchall()
for row in rows:
    print(row)