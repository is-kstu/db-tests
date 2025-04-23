import psycopg2;

DB_PARAMS = {
"dbname": "library_db",
"user": "postgres",
"password": "1234",
"port": "5433",
}

conn = psycopg2.connect(**DB_PARAMS)
cursor = conn.cursor()

cursor.execute ("""
Create table if not exists devices(
id serial primary key,
name varchar(50) not null,
serial_number varchar(100) 
)

""")

cursor.execute ("""
Create table if not exists repairs(
id serial primary key,
device_id integer not null,
problem_description varchar(100) not null,
status boolean,
date_received timestamp
)

""")

conn.commit()