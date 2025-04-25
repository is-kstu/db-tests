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





