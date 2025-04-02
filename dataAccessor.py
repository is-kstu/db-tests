import psycopg2

class DataAccessor:
    def __init__(self):
        self.connection = psycopg2.connect(
            user="postgres",
            password="rgb123qq",
            host="localhost",
            port="5432",
            database="test_1"
        )
        self.cursor = self.connection.cursor()

    def getCars(self, id):
        try:
            self.cursor.execute("SELECT * FROM cars WHERE id = %s", (id,))
            return self.cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print(error)
        finally:
            if hasattr(self, 'cursor') and self.cursor:
                self.cursor.close()
            if hasattr(self, 'connection') and self.connection:
                self.connection.close()

    def addCars(self, name, birth_date, brand, model, year):
        try:
            self.cursor.execute(
                "INSERT INTO owners (name, birth_date) VALUES (%s, %s)",
            (name, birth_date)
            )
            self.cursor.execute(
                "INSERT INTO cars (brand, model, year) VALUES (%s, %s, %s )",
                (brand, model, year)
            )
            self.connection.commit()
            return True
        except (Exception, psycopg2.Error) as error:
            print(error)
            return False
        finally:
            if hasattr(self, 'cursor') and self.cursor:
                self.cursor.close()
            if hasattr(self, 'connection') and self.connection:
                self.connection.close()
                
     def deleteCars(self, id):
        try:
            self.cursor.execute("SELECT * FROM cars WHERE id = %s", (id,))
            return self.cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print(error)
        finally:
            if hasattr(self, 'cursor') and self.cursor:
                self.cursor.close()
            if hasattr(self, 'connection') and self.connection:
                self.connection.close()
