# from PyQt6.QtCore import Qt, QSize
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QTableWidget, QLineEdit, QTableWidgetItem
# from data_accessor import DataAccessor

# class MainWindow(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.setWindowTitle('Онлайн-курсы и слушатели')
# 		self.setFixedSize(QSize(800, 600))
		
# 		self.title = QLabel('Список курсов и слушателей')
# 		self.course_label = QLabel('Курсы')
# 		self.student_label = QLabel('Слушатели')
# 		self.courses_table = QTableWidget()
# 		self.students_table = QTableWidget()
# 		self.add_button = QPushButton('Добавить студента')
# 		self.delete_button = QPushButton('Удалить')
# 		self.input_field = QLineEdit()

# 		self.main_layout = QVBoxLayout()
# 		self.h1_layout = QHBoxLayout()
# 		self.h2_layout = QHBoxLayout()
# 		self.h3_layout = QHBoxLayout()
# 		self.h4_layout = QHBoxLayout()

# 		self.main_layout.addLayout(self.h1_layout)
# 		self.main_layout.addLayout(self.h2_layout)
# 		self.main_layout.addLayout(self.h3_layout)
# 		self.main_layout.addLayout(self.h4_layout)

# 		self.h1_layout.addWidget(self.title)

# 		self.h2_layout.addWidget(self.course_label)
# 		self.h2_layout.addWidget(self.student_label)

# 		self.h3_layout.addWidget(self.courses_table)
# 		self.h3_layout.addWidget(self.students_table)

# 		self.h4_layout.addWidget(self.add_button)
# 		self.h4_layout.addWidget(self.delete_button)
# 		self.h4_layout.addWidget(self.input_field)
	
# 		self.setLayout(self.main_layout)

# 		self.add_button.clicked.connect(self.add_student)
# 		self.delete_button.clicked.connect(self.delete_student)
# 		self.courses_table.cellClicked.connect(self.load_students)

# 		self.load_courses()

# 		self.table_1.keyPressEvent = self.KeyPressed

# 	def load_courses(self):
# 		accessor = DataAccessor()
# 		self.courses = accessor.get_all_courses()
# 		self.courses_table.setRowCount(len(self.courses))
# 		self.courses_table.setColumnCount(2)
# 		self.courses_table.setHorizontalHeaderLabels(['ID', 'Название'])
# 		for row, course in enumerate(self.courses):
# 			self.courses_table.setItem(row, 0, QTableWidgetItem(str(course[0])))
# 			self.courses_table.setItem(row, 1, QTableWidgetItem(course[1]))
# 		self.courses_table.cellDoubleClicked.connect(self.KeyPressed)


# 	def load_students(self):
# 		course_id = self.get_selected_course_id()
# 		if course_id:
# 			accessor = DataAccessor()
# 			students = accessor.show_students_on_course(course_id)
# 			self.students_table.setRowCount(len(students))
# 			self.students_table.setColumnCount(2)
# 			self.students_table.setHorizontalHeaderLabels(['Имя', 'Дата'])
# 			for row, student in enumerate(students):
# 				self.students_table.setItem(row, 0, QTableWidgetItem(student[0]))
# 				self.students_table.setItem(row, 1, QTableWidgetItem(student[1]))

# 	def add_student(self):
# 		course_id = self.get_selected_course_id()
# 		student_name = self.input_field.text()
# 		enrollment_date = '2025-04-23'
# 		if course_id and student_name:
# 			accessor = DataAccessor()
# 			accessor.add_student(course_id, student_name, enrollment_date)
# 			self.load_students()

# 	def delete_student(self):
# 		student_name = self.input_field.text()
# 		if student_name:
# 			accessor = DataAccessor()
# 			accessor.delete_student(student_name)
# 			self.load_students()

# 	def get_selected_course_id(self):
# 		selected = self.courses_table.currentRow()
# 		if selected != -1:
# 			item = self.courses_table.item(selected, 0)
# 			if item:
# 				return int(item.text())

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QTableWidget, QLineEdit, QTableWidgetItem
from data_accessor import DataAccessor

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Онлайн-курсы и слушатели')
        self.setFixedSize(QSize(800, 600))

        self.title = QLabel('Список курсов и слушателей')
        self.course_label = QLabel('Курсы')
        self.student_label = QLabel('Слушатели')
        self.courses_table = QTableWidget()
        self.students_table = QTableWidget()
        self.add_button = QPushButton('Добавить студента')
        self.delete_button = QPushButton('Удалить')
        self.input_field = QLineEdit()

        self.main_layout = QVBoxLayout()
        self.h1_layout = QHBoxLayout()
        self.h2_layout = QHBoxLayout()
        self.h3_layout = QHBoxLayout()
        self.h4_layout = QHBoxLayout()

        self.main_layout.addLayout(self.h1_layout)
        self.main_layout.addLayout(self.h2_layout)
        self.main_layout.addLayout(self.h3_layout)
        self.main_layout.addLayout(self.h4_layout)

        self.h1_layout.addWidget(self.title)
        self.h2_layout.addWidget(self.course_label)
        self.h2_layout.addWidget(self.student_label)
        self.h3_layout.addWidget(self.courses_table)
        self.h3_layout.addWidget(self.students_table)
        self.h4_layout.addWidget(self.add_button)
        self.h4_layout.addWidget(self.delete_button)
        self.h4_layout.addWidget(self.input_field)

        self.setLayout(self.main_layout)

        self.add_button.clicked.connect(self.add_student)
        self.delete_button.clicked.connect(self.delete_student)
        self.courses_table.cellClicked.connect(self.load_students)

        self.load_courses()

        self.courses_table.keyPressEvent = self.KeyPressed

    def load_courses(self):
        accessor = DataAccessor()
        self.courses = accessor.get_all_courses()
        self.courses_table.setRowCount(len(self.courses))
        self.courses_table.setColumnCount(2)
        self.courses_table.setHorizontalHeaderLabels(['ID', 'Название'])
        for row, course in enumerate(self.courses):
            self.courses_table.setItem(row, 0, QTableWidgetItem(str(course[0])))
            item = QTableWidgetItem(course[1])
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)
            self.courses_table.setItem(row, 1, item)
        
        self.courses_table.itemChanged.connect(self.KeyPressed)

    def load_students(self):
        course_id = self.get_selected_course_id()
        if course_id:
            accessor = DataAccessor()
            students = accessor.show_students_on_course(course_id)
            self.students_table.setRowCount(len(students))
            self.students_table.setColumnCount(2)
            self.students_table.setHorizontalHeaderLabels(['Имя', 'Дата'])
            for row, student in enumerate(students):
                self.students_table.setItem(row, 0, QTableWidgetItem(student[0]))
                self.students_table.setItem(row, 1, QTableWidgetItem(student[1]))

    def add_student(self):
        course_id = self.get_selected_course_id()
        student_name = self.input_field.text()
        enrollment_date = '2025-04-23'
        if course_id and student_name:
            accessor = DataAccessor()
            accessor.add_student(course_id, student_name, enrollment_date)
            self.load_students()

    def delete_student(self):
        student_name = self.input_field.text()
        if student_name:
            accessor = DataAccessor()
            accessor.delete_student(student_name)
            self.load_students()

    def get_selected_course_id(self):
        selected = self.courses_table.currentRow()
        if selected != -1:
            item = self.courses_table.item(selected, 0)
            if item:
                return int(item.text())

    def KeyPressed(self, event):
        row = event.row()
        col = event.column()
        if col == 1:  # Колонка с названием курса
            course_id = int(self.courses_table.item(row, 0).text())
            new_title = self.courses_table.item(row, 1).text()
            db = DataAccessor()
            db.rename_course(course_id, new_title)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()


	


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
