import psycopg2

class DataAccessor:
    def __init__(self):
        self.connection = psycopg2.connect(
            database="pyqt",
            user="postgres",
            password="korileka55",
            port="5432",
            host="localhost"
        )
        self.cursor = self.connection.cursor()
        
    def show_students_on_course(self, course_id):
        self.cursor.execute('''
            SELECT student_name, enrollment_date FROM enrollments
            WHERE course_id = %s
        ''' % course_id)
        result = self.cursor.fetchall()
        self.connection.close()
        return result

    def add_student(self, course_id, student_name, enrollment_date):
        self.cursor.execute('''
            INSERT INTO enrollments(course_id, student_name, enrollment_date)
            VALUES (%s, '%s', '%s')
        ''' % (course_id, student_name, enrollment_date))
        self.connection.commit()
        self.connection.close()

    def delete_student(self, student_name):
        self.cursor.execute('''
            DELETE FROM enrollments
            WHERE student_name = '%s'
        ''' % student_name)
        self.connection.commit()
        self.connection.close()

    def get_all_courses(self):
        self.cursor.execute('''
            SELECT id, title FROM courses
        ''')
        result = self.cursor.fetchall()
        self.connection.close()
        return result

    def rename_course(self, course_id, new_title):
        self.cursor.execute('''
            UPDATE courses SET title = %s WHERE id = %s
        ''', (new_title, course_id))
        self.connection.commit()
        self.connection.close()


