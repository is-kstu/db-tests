import psycopg2

class DataAccessor:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="pyqt",
            user="postgres",
            password="123456",
            host="localhost",
            port="5432"
        )
        self.conn.autocommit = True

    def get_tours(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, country FROM tours")
            return cur.fetchall()

    def get_clients_by_tour(self, tour_id):
        with self.conn.cursor() as cur:
            cur.execute("SELECT name, phone FROM clients WHERE tour_id = %s", (tour_id,))
            return cur.fetchall()

    def add_client(self, tour_id, name, phone):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO clients (tour_id, name, phone) VALUES (%s, %s, %s)",
                (tour_id, name, phone)
            )

    def delete_client(self, name):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM clients WHERE name = %s", (name,))
