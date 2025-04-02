import psycopg2

class CreateTable():
	def __init__(self):
		self.connection = psycopg2.connect (database = 'hotel_db', username = 'postgres', password = '305012')
		self.cursor = sefl.connection.cursor()
	def createTable(self):
		self.execute(
'''
create table rooms(id serial, number int, type varchar(50), price_per_night int);
create table reservations (id serial, room_id int, guest_name varchar(50), check_in date, check_out date, foreign key room_id references rooms(id));
'''
)
