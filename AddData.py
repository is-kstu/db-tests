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