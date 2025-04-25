import sqlite3
from datetime import datetime

DB = 'courses.db'

def get_courses():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id, title FROM courses")
    result = c.fetchall()
    conn.close()
    return result

def get_students(course_id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id, student_name, enrollment_date FROM enrollments WHERE courses_id = ?", (course_id,))
    result = c.fetchall()
    conn.close()
    return result

def add_student(course_id, name):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO enrollments (courses_id, student_name, enrollment_date) VALUES (?, ?, ?)",
              (course_id, name, datetime.now().strftime('%Y-%m-%d')))
    conn.commit()
    conn.close()

def delete_enrollment(enrollment_id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM enrollments WHERE id = ?", (enrollment_id,))
    conn.commit()
    conn.close()