# 8 вариант

import psycopg2

DB_PARAMS = {
    "dbname": "bd_test",
    "user": "davidkozahmetov",
    "password": "456759254",
    "host": "localhost",
    "port": "5432"
}

def get_students():
    conn = psycopg2.connect(**DB_PARAMS)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM students;")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return students

def get_grades(student_id):
    conn = psycopg2.connect(**DB_PARAMS)
    cursor = conn.cursor()
    cursor.execute("SELECT id, subject, grade FROM grades WHERE student_id = %s;", (student_id,))
    grades = cursor.fetchall()
    cursor.close()
    conn.close()
    return grades

def add_grade(student_id, subject, grade):
    conn = psycopg2.connect(**DB_PARAMS)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO grades (student_id, subject, grade) VALUES (%s, %s, %s);", (student_id, subject, grade))
    conn.commit()
    cursor.close()
    conn.close()

