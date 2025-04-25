import psycopg2

class DataAccessor():
	def __init__(self):
		return None	
	def connect(self):
		conn = psycopg2.connect(database = 'manage_repair_db', user = 'postgres', password = '305012')
		return conn

	def get_all_devices(self):
		self.conn = self.connect()
		self.cursor = self.conn.cursor()
		self.cursor.execute('''
				select id, name, serial_number from devices;
				''')
		devices = self.cursor.fetchall()
		self.conn.commit()
		self.cursor.close()
		self.conn.close()
		return devices


	def get_all_repairs(self, device_id):
		self.conn = self.connect()
		self.cursor = self.conn.cursor()
		self.cursor.execute('''
				select id, device_id, problem_description, status, date_recived from repairs where device_id = %s;
				''',(device_id,))
		repairs = self.cursor.fetchall()
		self.conn.commit()
		self.cursor.close()
		self.conn.close()
		return repairs


	def add_repair(self, device_id, problem_description, status):
		self.conn = self.connect()
		self.cursor = self.conn.cursor()
		self.cursor.execute('''
				insert into repairs (device_id, problem_description, status) values (%s, %s, %s)
				''', (device_id, problem_description, status))
		self.conn.commit()
		self.cursor.close()
		self.conn.close()


	def change_status(self, repair_id, new_status):
		self.conn = self.connect()
		self.cursor = self.conn.cursor()
		self.cursor.execute ('''update repairs set status = %s where id = %s''', (new_status, repair_id))
		self.conn.commit()
		self.cursor.close()
		self.conn.close()

	


	
		
