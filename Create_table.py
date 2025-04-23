import psycopg2

class PostgresDB:
    def __init__(self, host, port, dbname, user, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            print("Успешное подключение к базе данных.")
        except Exception as e:
            print("Ошибка при подключении:", e)

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Exception as e:
            print("Ошибка при выполнении запроса:", e)
            return None

    def execute_non_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            print("Запрос выполнен успешно.")
        except Exception as e:
            print("Ошибка при выполнении запроса:", e)
            self.connection.rollback()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Соединение закрыто.")


if __name__ == "__main__":
    db = PostgresDB(
        host="localhost",
        port=5432,
        dbname="pyqt",
        user="postgres",
        password="123456"
    )
    db.connect()

    create_table_sql = """
    	CREATE TABLE tours (
    	id INTEGER PRIMARY KEY,
    	country TEXT,
    	price REAL,
    	duration INTEGER
	);

	CREATE TABLE clients (
   	id INTEGER PRIMARY KEY,
    	tour_id INTEGER,
   	name TEXT,
    	phone TEXT,
    	FOREIGN KEY(tour_id) REFERENCES tours(id)
	);

    """

    db.execute_non_query(create_table_sql)

    db.close()
