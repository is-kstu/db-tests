# 8 вариант

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit
import sys
from data_accessor import get_students, get_grades, add_grade

class GradeManager(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.student_select = QComboBox()
        self.LoadStudents()  
        self.student_select.currentIndexChanged.connect(self.LoadGrade)
        layout.addWidget(self.student_select)

        self.grade_table = QTableWidget()
        self.grade_table.setColumnCount(3)  
        self.grade_table.setHorizontalHeaderLabels(["ID", "Предмет", "Оценка"])
        layout.addWidget(self.grade_table)

        self.subject_input = QLineEdit()
        self.subject_input.setPlaceholderText("Предмет")
        layout.addWidget(self.subject_input)

        self.grade_input = QLineEdit()
        self.grade_input.setPlaceholderText("Оценка")
        layout.addWidget(self.grade_input)

        self.add_button = QPushButton("Добавить оценку")
        self.add_button.clicked.connect(self.PushGrade)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def LoadStudents(self):
        self.student_select.clear()  
        students = get_students()  
        for student in students:
            self.student_select.addItem(student[1], student[0])  

    def LoadGrade(self):
        student_id = self.student_select.currentData()  
        self.grade_table.setRowCount(0)  
        grades = get_grades(student_id)  
        for grade in grades:
            row = self.grade_table.rowCount()  
            self.grade_table.insertRow(row)  
            self.grade_table.setItem(row, 0, QTableWidgetItem(str(grade[0])))  
            self.grade_table.setItem(row, 1, QTableWidgetItem(grade[1]))  
            self.grade_table.setItem(row, 2, QTableWidgetItem(str(grade[2])))  

    def PushGrade(self):
        student_id = self.student_select.currentData()  
        subject = self.subject_input.text()  
        grade = self.grade_input.text()  
        add_grade(student_id, subject, int(grade))  
        self.LoadGrade()  

if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = GradeManager()  
    window.show()  
    sys.exit(app.exec())  
