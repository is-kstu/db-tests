import sqlite3

def show_products_by_category(category_id):
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, price FROM products WHERE category_id = ?", (category_id,))
    products = cursor.fetchall()
    conn.close()
    return products

def add_product(name, price, category_id):
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)", (name, price, category_id))
    conn.commit()
    conn.close()
    print("Товар добавлен.")

def delete_product(product_name):
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE name = ?", (product_name,))
    conn.commit()
    conn.close()
    print("Товар удалён.")

# Пример использования
print(show_products_by_category(1))  # Покажет товары из категории Electronics
add_product("Tablet", 600.00, 1)
delete_product("Novel")
