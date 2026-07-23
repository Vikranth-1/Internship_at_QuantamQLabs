import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sample.db')

def insert_student():
    print("\n--- Insert Student ---")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    email = input("Enter Email: ")
    course = input("Enter Course: ")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO students (name, age, email, course) VALUES (?, ?, ?, ?)",
            (name, age, email, course)
        )
        conn.commit()
        print("Student added successfully!")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

def display_all():
    print("\n--- All Students ---")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Email: {row[3]} | Course: {row[4]}")
    conn.close()

def search_student():
    print("\n--- Search Student ---")
    name = input("Enter name to search: ")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", (f"%{name}%",))
    for row in cursor.fetchall():
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Email: {row[3]} | Course: {row[4]}")
    conn.close()

def update_student():
    print("\n--- Update Student ---")
    student_id = int(input("Enter Student ID to update: "))
    new_course = input("Enter new Course: ")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET course = ? WHERE id = ?", (new_course, student_id))
    conn.commit()
    conn.close()
    print("Student updated successfully!")

def delete_student():
    print("\n--- Delete Student ---")
    student_id = int(input("Enter Student ID to delete: "))

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    print("Student deleted successfully!")


conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,
age INTEGER,email TEXT UNIQUE,course TEXT)""")
conn.commit()
conn.close()

insert_student()
insert_student()
display_all()
search_student()
update_student()
delete_student()