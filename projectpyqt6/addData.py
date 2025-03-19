import psycopg2
class AddData:
     
     def connect_to_db(self):
        try:
            database = psycopg2.connect(
                database="Uniony",
                user="postgres",
                password="123456",
                port="5432",
                host="localhost"
            )
            cursor = database.cursor()

            cursor.execute(""" 
                INSERT INTO departaments (name)
                VALUES
                        ('HR'),
                        ('IT'),
                        ('Markering');
                INSERT INTO employees (name, departament_id, salary)
                VALUES
                           ('Alice', )

            """)

            database.commit()
            cursor.close()
            database.close()
            
            print("Данные успешно изменены")
        except Exception as e:
            print(f"Ошибка подключения к БД: {e}")

addData = AddData()
addData.connect_to_db()
