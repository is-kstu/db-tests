import sys
import psycopg2
from PyQt6.QtWidgets import QApplication, QMessageBox

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="my_db",      # Имя базы данных
            user="postgres",     # Имя пользователя (исправлено)
            password="1111",     # Пароль
            host="localhost",    # Адрес сервера
            port=5433            # Порт PostgreSQL (проверь)
        )
        print("✅ Подключение к БД успешно!")
        return conn
    except psycopg2.Error as e:
        QMessageBox.critical(None, "Ошибка подключения", f"Ошибка: {e}")
        print(f"❌ Ошибка подключения к БД: {e}")
        return None

def execute_query():
    conn = connect_to_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM employees")  # Пример запроса
            rows = cur.fetchall()
            for row in rows:
                print(row[0], row[1])  # Вывод данных
            cur.close()
            conn.close()
        except psycopg2.Error as e:
            print(f"❌ Ошибка выполнения запроса: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    execute_query()
    sys.exit(app.exec())
