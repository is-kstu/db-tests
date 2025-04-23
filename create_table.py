import psycopg2

class Data:
    def connect_to_db(self):
        try:
            connection = psycopg2.connect(
                database='pyqt',
                user='postgres',
                password='korileka55',
                host='localhost',
                port='5432'
            )
            cursor = connection.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS courses (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(100),
                    description TEXT
                );
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS enrollments (
                    id SERIAL PRIMARY KEY,
                    course_id INT,
                    student_name VARCHAR(100),
                    enrollment_date VARCHAR(50),
                    FOREIGN KEY (course_id) REFERENCES courses(id)
                );
            ''')

            cursor.execute('''
                INSERT INTO COURSES (title)
		VALUES ('математика'), ('программирование');
            ''')
            

            connection.commit()
            cursor.close()
            connection.close()
            print('Запрос успешно выполнен')

        except Exception as e:
            print(f'Ошибка подключения к БД: {e}')

create_table = Data()
create_table.connect_to_db()