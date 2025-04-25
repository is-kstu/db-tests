import sqlite3

# Создание базы данных
conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

# Удаление таблиц если они уже есть
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS categories")

# Создание таблиц
cursor.execute("""
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)
)
""")

# Вставка данных
categories = [("Electronics",), ("Books",), ("Clothing",)]
cursor.executemany("INSERT INTO categories (name) VALUES (?)", categories)

products = [
    ("Phone", 1200.00, 1),
    ("Laptop", 2500.00, 1),
    ("Novel", 15.99, 2),
    ("T-shirt", 9.99, 3)
]
cursor.executemany("INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)", products)

conn.commit()
conn.close()
print("База данных создана и заполнена.")
