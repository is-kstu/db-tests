import psycopg2

def create_tables():
	conn = psycopg2.connect (database = 'manage_repair_db', user = 'postgres', password = '305012')
	cursor = conn.cursor()
	cursor.execute('''
		create table if not exists devices (id serial primary key, name varchar (60), serial_number int);
		create table if not exists repairs (id serial primary key, device_id int references devices (id), problem_description text, status varchar (50), date_recived timestamp default current_timestamp); 
			''')
	conn.commit()
	cursor.close()
	conn.close()