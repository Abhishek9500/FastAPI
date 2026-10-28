from fastapi import FastAPI,Request
import sqlite3

app = FastAPI()

# connect to database
conn = sqlite3.connect("users.db")

# create a cursor
cursor = conn.cursor()

# create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
""")

# Insert Data
cursor.execute(
    "INSERT INTO users (name, age) VALUES (?, ?)",
    ("Abhishek", 21)
)

# save changes
conn.commit()

# fetch data
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# close connection
conn.close()
