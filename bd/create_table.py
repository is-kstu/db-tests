# 8 вариант

import psycopg2

DB_PARAMS = {
    "dbname": "bd_test",
    "user": "davidkozahmetov",
    "password": "456759254",
    "host": "localhost",
    "port": "5432"
}
conn = psycopg2.connect(**DB_PARAMS)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    group_name VARCHAR(50) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS grades (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id) ON DELETE CASCADE,
    subject VARCHAR(100) NOT NULL,
    grade INTEGER CHECK (grade BETWEEN 1 AND 5)
);
""")

cursor.execute("INSERT INTO students (name, group_name) VALUES ('Иван Иванов', 'Группа 1'), ('Мария Петрова', 'Группа 2') ON CONFLICT DO NOTHING;")

cursor.execute("INSERT INTO grades (student_id, subject, grade) VALUES (1, 'Математика', 4), (1, 'Физика', 5), (2, 'Литература', 3) ON CONFLICT DO NOTHING;")

conn.commit()
cursor.close()
conn.close()


