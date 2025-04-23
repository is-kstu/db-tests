import psycopg2

from env import DB_PARAMS

def create_tables():
    conn = None
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()

        print("Удаление старых таблиц (если существуют)...")
        cur.execute("DROP TABLE IF EXISTS repairs;")
        cur.execute("DROP TABLE IF EXISTS masters;")

        print("Создание таблицы 'masters'...")
        cur.execute("""
            CREATE TABLE masters (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                specialty VARCHAR(100)
            )
        """)

        print("Создание таблицы 'repairs'...")
        cur.execute("""
            CREATE TABLE repairs (
                id SERIAL PRIMARY KEY,
                master_id INTEGER,
                item VARCHAR(255) NOT NULL,
                issue TEXT,
                status VARCHAR(50) DEFAULT 'Новый',
                FOREIGN KEY (master_id) REFERENCES masters (id) ON DELETE SET NULL
            )
        """)

        print("Добавление тестовых мастеров...")
        masters_data = [
            ('Сергей Сергей', 'Электро'),
            ('Анна Анна', 'Быт техника'),
            ('Виктор Виктор', 'Комп')
        ]
        cur.executemany("INSERT INTO masters (name, specialty) VALUES (%s, %s)", masters_data)
        conn.commit()

        cur.execute("SELECT id FROM masters ORDER BY id")
        master_ids = [row[0] for row in cur.fetchall()]

        if master_ids:
            print("Добавление тестовых заказов...")
            repairs_data = [
                (master_ids[0], 'Телефон', 'Не включается', 'В работе'),
                (master_ids[1], 'Bosch', 'БАМБАМБИМ', 'Новый'),
                (master_ids[0], 'Пваншет', 'Разбит экран', 'ОПОПОПО'),
                (master_ids[2], 'Ноут', '200C', 'Новый'),
                (None, 'Кофеварка', 'Протекает', 'Новый')
            ]
            cur.executemany("INSERT INTO repairs (master_id, item, issue, status) VALUES (%s, %s, %s, %s)", repairs_data)

        conn.commit()
        print("Таблицы созданы")
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка PostgreSQL: {error}")
        if conn: conn.rollback()
    finally:
        if conn is not None:
            conn.close()
            print("Соединение закрыто.")

if __name__ == '__main__':
    create_tables()
    print("\nУСПЕХ")

