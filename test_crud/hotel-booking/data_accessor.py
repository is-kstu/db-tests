import psycopg2
from config import DB_CONFIG;

class DataAccessor:
    def __init__(self):
        self.conn = None;
        self.cursor = None;

    def connect(self):
        self.conn = psycopg2.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor()

    def execute_query(self, query):
        self.cursor.execute(query);
        self.conn.commit();
        self.cursor.close();

    def reservations_with_rooms(self):
        query_reservations = """
        SELECT * FROM reservations WHERE room_id != NULL;
        """

        return self.execute_query(query_reservations)

    def create_new_resetvation(self, room_id, guest_name, check_in, check_out):
        create_query = f"""
        INSERT INTO reservations(room_id, guest_name, check_in, check_out)
        VALUES({room_id}, {guest_name}, {check_in}, {check_out});
        """
        self.cursor.execute(self.conn, create_query)
        self.conn.commit();
        self.cursor.close();

if __name__ == "__main__":
    data_accessor = DataAccessor();
    data_accessor.connect()
    print(data_accessor.reservations_with_rooms())
