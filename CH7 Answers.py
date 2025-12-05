#Problem 1
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade REAL
)
""")

students = [
    (1, "Ali", 85.5),
    (2, "Sara", 92.0),
    (3, "Mohamed", 78.3)
]

cursor.executemany("INSERT OR REPLACE INTO students VALUES (?, ?, ?)", students)

conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

#Problem 2
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

name = input("Enter name: ")
grade = float(input("Enter grade:"))

cursor.execute("select * from students")
rows = cursor.fetchall()

id = rows[-1][0] + 1

cursor.execute("INSERT OR REPLACE INTO students VALUES(? , ? , ?)" , (id , name , grade))

conn.commit()

cursor.execute("select * from students")
rows = cursor.fetchall()

print("--- Updated Records ---")
for row in rows:
    print(row)

conn.close()

#Problem 3
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

try:
    cursor.execute("BEGIN")

    print("Started Transaction...")

    cursor.execute("INSERT OR REPLACE INTO students VALUES(4 , 'Ahmed' , 80.1)")
    cursor.execute("INSERT OR REPLACE INTO students VALUES(5 , 'Khaled' , 84.14)")
    cursor.execute("INSERT OR REPLACE INTO students VALUES(6 , 'Mark' , 95.7)")

    x = 1 / 0

    conn.commit()
except Exception as e:
    print("Error Happened..")
    conn.rollback()
    print("Rollback Excuted...")

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()


#Problem 4
import sqlite3

class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author

connection = sqlite3.connect("books.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT
)
""")

books = [
    Book(1, "The Alchemist", "Paulo Coelho"),
    Book(2, "Atomic Habits", "James Clear")
]

book_tuples = [(b.id, b.title, b.author) for b in books]

cursor.executemany("INSERT OR REPLACE INTO books VALUES(?, ?, ?)", book_tuples)

connection.commit()

cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close()