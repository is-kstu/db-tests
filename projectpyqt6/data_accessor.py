import psycopg2

class DataAccessor:
    def __init__(self):
        self.connection = psycopg2.connect(
            database="Uniony",
                user="postgres",
                password="123456",
                port="5432",
                host="localhost"
        )
        self.cursor = self.connection.cursor()
        
    def add_new_user(self, name, departament_id, salary):
        self.cursor.execute('''
            INSERT INTO employees(name, departament_id, salary)
            VALUES
                ('%s', %s, %s)
                            
        '''%(name, departament_id,salary))
        self.connection.commit()
        self.connection.close()
    
    def add_new_department(self, name):
        self.cursor.execute('''
            INSERT INTO departaments(name)
            VALUES
                ('%s')
                            
        '''%(name))
        self.connection.commit()
        self.connection.close()

    def add_new_employee(self, name, department, salary):
            self.cursor.execute('''
                INSERT INTO employees(name, departament_id, salary)
                VALUES
                    ('%s', (Select id FROm departaments WHERE name = '%s'), %s)
                                
            '''%(name, department, salary))
            self.connection.commit()
            self.connection.close()

    def select_all_departments(self):
        self.cursor.execute('''
            Select * FROM departaments;
        ''')
        departments = self.cursor.fetchall()
        self.connection.close()
        return departments
