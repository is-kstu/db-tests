import psycopg2
class Data:
    def connect_to_db(self):
        try:
            connection = psycopg2.connect(database = 'postgres',
						      user = 'postgres',
						      password = 'korileka55',
						      host = 'localhost',
						      port = '5432')
            connection.commit()
            cursor = connection.cursor()
	
            cursor.execute('''CREATE TABLE tables (
				id SERIAL PRIMARY KEY,
				table_number INT,
				capacity INT);
				
				CREATE TABLE orders (
				    id SERIAL PRIMARY KEY,
				    table_id INT,
				    order_time VARCHAR(50),
				    total_price INT,
				   FOREIGN KEY (table_id) REFERENCES tables(id));''')
	
            cursor.close()
            connection.close()
            print('Запрос успешно выполнен')
        except Exception as e:
            print(f'Ошибка подключения к БД: {e}')

create_table = Data()
create_table.connect_to_db()

