# 2 вариант

import psycopg2

conn = psycopg2.connect(
    dbname="bd_test",
    user="davidkozahmetov",
    password="456759254",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS rooms (
    id SERIAL PRIMARY KEY,
    room_number VARCHAR(10),
    type VARCHAR(50),
    price NUMERIC
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id SERIAL PRIMARY KEY,
    room_id INTEGER,
    guest_name VARCHAR(100),
    check_in DATE,
    check_out DATE
)
""")

cur.execute("INSERT INTO rooms (room_number, type, price) VALUES ('101', 'Обычный', 3000), ('102', 'Двухместный', 5000), ('201', 'Люкс', 10000)")

conn.commit()
cur.close()
conn.close()
