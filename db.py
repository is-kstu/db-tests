import psycopg2

def get_connection():
    return psycopg2.connect(
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432',
        database='postgres'
    )

def get_categories():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name FROM categories")
            return cur.fetchall()

def get_products_by_category(category_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, name, price FROM products WHERE category_id = %s",
                (category_id,))
            return cur.fetchall()

def add_product(name, price, category_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO products (name, price, category_id) VALUES (%s, %s, %s)",
                (name, price, category_id))
            conn.commit()

def delete_product(product_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM products WHERE id = %s", (product_id,))
            conn.commit()