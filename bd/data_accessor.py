# 2 вариант

import psycopg2

class HotelDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="bd_test",
            user="davidkozahmetov",
            password="456759254",
            host="localhost",
            port="5432"
        )

    def get_rooms(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, room_number FROM rooms")
        result = cur.fetchall()
        cur.close()
        return result

    def get_bookings_by_room(self, room_id):
        cur = self.conn.cursor()
        cur.execute("SELECT guest_name, check_in, check_out FROM bookings WHERE room_id = %s", (room_id,))
        result = cur.fetchall()
        cur.close()
        return result

    def add_booking(self, room_id, guest_name, check_in, check_out):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO bookings (room_id, guest_name, check_in, check_out) VALUES (%s, %s, %s, %s)",
                    (room_id, guest_name, check_in, check_out))
        self.conn.commit()
        cur.close()
