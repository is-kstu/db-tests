import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton, QTableWidget, QTableWidgetItem
import psycopg2

class StudentGradesApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Учёт студентов и их оценок")
        self.setGeometry(100, 100, 600, 400)
        
        self.layout = QVBoxLayout()
        
        self.student_combo = QComboBox()
        self.layout.addWidget(self.student_combo)
        
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Предмет", "Оценка"])
        self.layout.addWidget(self.table)
        
        self.add_button = QPushButton("Добавить оценку")
        self.delete_button = QPushButton("Удалить оценку")
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.delete_button)
        
        self.setLayout(self.layout)
        
        self.create_tables()
        self.load_students()
        self.student_combo.currentIndexChanged.connect(self.load_grades)
    
    def connect_db(self):
        return psycopg2.connect(
            dbname="StudentsGrades",
            user="postgres",
            password="123456",
            host="localhost",
            port="5432"
        )
    
    def create_tables(self):
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO students (id, name, group_name)
	VALUES
	(1, 'Max','Programmist');

	INSERT INTO grades (student_id, subject, grade)
	VALUES
	(1, 'yughijo', 2);
        """)
        
        conn.commit()
        conn.close()
    
    def load_students(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM students")
        students = cursor.fetchall()
        conn.close()
        
        self.student_combo.clear()
        for student in students:
            self.student_combo.addItem(student[1], student[0])
    
    def load_grades(self):
        student_id = self.student_combo.currentData()
        if student_id is None:
            return
        
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, subject, grade FROM grades WHERE student_id = %s", (student_id,))
        grades = cursor.fetchall()
        conn.close()
        
        self.table.setRowCount(len(grades))
        for row, grade in enumerate(grades):
            self.table.setItem(row, 0, QTableWidgetItem(str(grade[0])))
            self.table.setItem(row, 1, QTableWidgetItem(grade[1]))
            self.table.setItem(row, 2, QTableWidgetItem(str(grade[2])))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentGradesApp()
    window.show()
    sys.exit(app.exec())