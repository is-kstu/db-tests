import sqlite3
def create_database():
    # Connect to SQLite database (will create if it doesn't exist)
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()
    
    # Create courses table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT
    )
    ''')
    
    # Create enrollments table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        courses_id INTEGER NOT NULL,
        student_name TEXT NOT NULL,
        enrollment_date TEXT NOT NULL,
        FOREIGN KEY (courses_id) REFERENCES courses (id)
    )
    ''')
    
    # Очистка данных перед заполнением
    cursor.execute("DELETE FROM enrollments")
    cursor.execute("DELETE FROM courses")
    
    # Insert some sample data
    # Sample courses
    sample_courses = [
        ('Python Programming', 'Introduction to Python programming language'),
        ('Database Design', 'Learn SQL and database normalization'),
        ('Web Development', 'HTML, CSS and JavaScript basics')
    ]
    
    cursor.executemany('INSERT INTO courses (title, description) VALUES (?, ?)', sample_courses)
    
    # Sample enrollments
    sample_enrollments = [
        (1, 'Иван Иванов', '2025-04-10'),
        (1, 'Мария Петрова', '2025-04-11'),
        (2, 'Алексей Сидоров', '2025-04-12'),
        (2, 'Елена Смирнова', '2025-04-13'),
        (3, 'Дмитрий Козлов', '2025-04-14')
    ]
    
    cursor.executemany('INSERT INTO enrollments (courses_id, student_name, enrollment_date) VALUES (?, ?, ?)', 
                      sample_enrollments)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print("Database created successfully with sample data!")

if __name__ == "__main__":
    create_database()