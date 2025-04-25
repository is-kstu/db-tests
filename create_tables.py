import psycopg2


conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="ghost0596",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS masters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    specialty VARCHAR(100)
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS repairs (
    id SERIAL PRIMARY KEY,
    master_id INTEGER REFERENCES masters(id),
    item VARCHAR(100),
    issue TEXT,
    status VARCHAR(50)
);
""")

cur.execute("SELECT COUNT(*) FROM masters")
master_count = cur.fetchone()[0]

if master_count == 0:
    cur.execute("INSERT INTO masters (name, specialty) VALUES (%s, %s)", ('Иванов Иван', 'Электроника'))
    cur.execute("INSERT INTO masters (name, specialty) VALUES (%s, %s)", ('Петров Пётр', 'Механика'))

cur.execute("SELECT id FROM masters WHERE name = 'Иванов Иван'")
ivanov_id = cur.fetchone()[0]

cur.execute("SELECT id FROM masters WHERE name = 'Петров Пётр'")
petrov_id = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM repairs")
repair_count = cur.fetchone()[0]

if repair_count == 0:
    cur.execute("""
        INSERT INTO repairs (master_id, item, issue, status)
        VALUES
        (%s, 'Телефон', 'Не включается', 'Принят'),
        (%s, 'Ноутбук', 'Сломан экран', 'В работе'),
        (%s, 'Пылесос', 'Не всасывает', 'Готов')
    """, (ivanov_id, ivanov_id, petrov_id))

conn.commit()
cur.close()
conn.close()

print("Таблицы созданы.")
