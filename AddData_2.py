<<<<<<< HEAD
# Variant 11

import os 
import psycopg2
from dotenv import load_dotenv

load_dotenv(override=True)

user = "postgres"
password ="305012"	
dbname = "conrol2"
host = "localhost"

connection = psycopg2.connect(user="postgres", password="305012", database="conrol2")
cursor = connection.cursor()

def create_table(cursor):
	cursor.execute('''

create table movies(id serial primary key,
title varchar(50),
genre varchar(50),
duration varchar(50));

create table screenings( id serial primary key,
movie_id int references movies(id),
date_time timestamp,
hall_number int );

insert into movies(title, genre, duration)
values
('aboba','zzz','123'),
('zup','xxx','210'),
('loxn','ipuo','100'),
('pop','popinor','1243');


insert into screenings(movie_id, date_time,hall_number)
values
('1','2025.03.15 06:12:00','1'),
('2','2025.03.15 06:12:00','2'),
('3','2025.03.15 06:12:00','3'),
('4','2025.03.15 06:12:00','4'),
('1','2025.03.16 06:12:00','2'),
('2','2025.03.16 06:12:00','3'),
('3','2025.03.16 06:12:00','1');
''')

	connection.commit()
	cursor.close()
	connection.close()

if __name__ == "__main__":
	create_table(cursor)





=======
// Вариант 6

import psycopg2

class AddData:
	def connect_to_db(self):
		try:
			database = psycopg2.connect(
				database="bd_courses_2", 
				user = "postgres",
				password="305012",
				port = "5432",
				host="localhost"
			)
			cursor = database.cursor()

			cursor.execute(""" 
create table owners(id serial primary key, name varchar(50), birht_date varchar(50));

crate table cars( id serial primary key, owner_id is not null, foreign key(id) references owners(id), brand varchar(50), model varchar(50), year int);

insert into owners(name varchar(50), birht_date varchar(50))
values
('Ura','12.10.2005'),
('Ivan','15.09.2005'),
('David','12.01.2006');

insert into cars(owner_id, brand, model, year)
values
(1,'bmv','e3',1998),
(2,'merc','benz',2015),
(3,'audi','a3',2014);
""")

			database.commit()
			cursor.close()
			database/close()

			print("Данные успешно сохранены")

		except Exception as e:
			print(f"Ощибка подключения к БД:{e}")

addData=AddData()
addData.connect_to_db()
>>>>>>> 68be27f36bb2289b992076191fea6eaae0544012
