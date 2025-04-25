import psycopg2

class DataAccessor:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="conrol2",
            user="postgres",
            password="305012",
            host="localhost",  
            port="5432"       
        )
        self.cursor = self.conn.cursor()

    def add_new_screen(self, movie_id, date_time, hall_number):
        query = "INSERT INTO screenings (movie_id, date_time, hall_number) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (movie_id, date_time, hall_number))
        self.conn.commit()

    def delete_screen(self, screen_id):
        query = "DELETE FROM screenings WHERE id = %s"
        self.cursor.execute(query, (screen_id,))
        self.conn.commit()

def get_screen(self, movie_id):
    query = "SELECT id, movie_id, date_time, hall FROM screenings WHERE movie_id = %s"
    self.cursor.execute(query, (movie_id,))
    return self.cursor.fetchall()


    def __del__(self):
        self.cursor.close()
        self.conn.close()












