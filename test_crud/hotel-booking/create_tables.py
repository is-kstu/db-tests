import psycopg2

from config import DB_CONFIG;

def create_connection(): return psycopg2.connect(**DB_CONFIG)

def execute_query(conn, query):
    cursor = conn.cursor();
    cursor.execute(query);
    conn.commit();
    cursor.close();

def create_tables(conn):
    create_rooms_query = """
        CREATE TABLE IF NOT EXISTS  rooms (
            id SERIAL PRIMARY KEY,
            number INTEGER,
            type VARCHAR(255),
            price_per_night INTEGER
        );
        """
    execute_query(conn, create_rooms_query)

    create_reservations_query = """
        CREATE TABLE IF NOT EXISTS reservations (
            id SERIAL PRIMARY KEY,
            room_id INTEGER,
            guest_name VARCHAR(255),
            check_in DATE,
            check_out DATE
        );
        """
    execute_query(conn, create_reservations_query)


if __name__ == "__main__":
    conn = create_connection()
    create_tables(conn)
