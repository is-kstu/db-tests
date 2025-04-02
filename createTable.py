import psycopg2

class CreateTable:
    def __init__(self):
        self.connection = psycopg2.connect(
            user="postgres",
            password="rgb123qq",
            host="localhost",
            port="5432",
            database="test_1"
        )
        self.cursor = self.connection.cursor()

    def create(self):
        sqlLine1 = """
        CREATE TABLE owners(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            birth_date DATE
        );
        """

        sqlLine2 = """
        CREATE TABLE cars(
            id SERIAL PRIMARY KEY,
            owner_id INT REFERENCES owners(id),
            brand VARCHAR(50),
            year INT,
            model VARCHAR(50)
        );
        """

        self.cursor.execute(sqlLine1)
        self.cursor.execute(sqlLine2)
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

create_table = CreateTable()
create_table.create()
