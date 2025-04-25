import psycopg2

class DataCreate:
    def connect_to_db(self):
        try:
            connection = psycopg2.connect(
                user='postgres',
                password='postgres',
                port='5432',
                host='localhost',
                database='postgres'
            )
            cursor = connection.cursor()

            create_table = '''
            CREATE TABLE IF NOT EXISTS categories(
                ID SERIAL PRIMARY KEY,
                name VARCHAR(50)
            );
            
            CREATE TABLE IF NOT EXISTS products(
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price NUMERIC(10,2),
                category_id INTEGER REFERENCES categories(id)
            );
            '''
            cursor.execute(create_table)

            
            insert_categories = '''
            INSERT INTO categories (name) VALUES 
            ('Электроника'), 
            ('Одежда'), 
            ('Книги')
            ON CONFLICT DO NOTHING;
            '''
            cursor.execute(insert_categories)

            insert_products = '''
            INSERT INTO products (name, price, category_id) VALUES
            ('Смартфон', 30000.00, 1),
            ('Футболка', 1500.00, 2),
            ('Роман', 500.00, 3)
            ON CONFLICT DO NOTHING;
            '''
            cursor.execute(insert_products)

            connection.commit()
            cursor.close()
            connection.close()

            print('Таблицы успешно созданы и заполнены')
        except Exception as e:
            print(f'Ошибка подключения к БД: {e}')


table = DataCreate()
table.connect_to_db()