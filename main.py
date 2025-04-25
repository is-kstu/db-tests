import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, 
                             QListWidget, QTableWidget, QTableWidgetItem, 
                             QPushButton, QLabel, QInputDialog, QMessageBox)
# Импортируем функции из вашего модуля
import data_accessor as da

class CourseEnrollmentApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('Course Enrollment System')
        self.setGeometry(300, 300, 800, 500)
        
        # Main layout
        main_layout = QVBoxLayout()
        
        # Top layout with courses list and enrollments table
        top_layout = QHBoxLayout()
        
        # Left side - Courses list
        courses_label = QLabel("Courses:")
        self.courses_list = QListWidget()
        self.courses_list.setMinimumWidth(300)
        
        left_layout = QVBoxLayout()
        left_layout.addWidget(courses_label)
        left_layout.addWidget(self.courses_list)
        
        top_layout.addLayout(left_layout)
        
        # Right side - Enrollments table
        enrollments_label = QLabel("Enrolled Students:")
        self.enrollments_table = QTableWidget()
        self.enrollments_table.setColumnCount(3)
        self.enrollments_table.setHorizontalHeaderLabels(['ID', 'Student Name', 'Enrollment Date'])
        self.enrollments_table.setMinimumWidth(400)
        
        right_layout = QVBoxLayout()
        right_layout.addWidget(enrollments_label)
        right_layout.addWidget(self.enrollments_table)
        
        top_layout.addLayout(right_layout)
        
        # Bottom layout with buttons
        bottom_layout = QHBoxLayout()
        
        self.add_student_btn = QPushButton('Add Student')
        self.delete_student_btn = QPushButton('Delete Student')
        
        bottom_layout.addWidget(self.add_student_btn)
        bottom_layout.addWidget(self.delete_student_btn)
        
        # Add layouts to main layout
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)
        
        self.setLayout(main_layout)
        
        # Connect signals
        self.courses_list.itemClicked.connect(self.on_course_selected)
        self.add_student_btn.clicked.connect(self.add_student)
        self.delete_student_btn.clicked.connect(self.delete_student)
        
        # Load initial data
        self.load_courses()
        
    def load_courses(self):
        courses = da.get_courses()
        self.courses_list.clear()
        for course in courses:
            self.courses_list.addItem(f"{course[0]}: {course[1]}")
    
    def on_course_selected(self, item):
        # Get selected course ID
        course_id = int(item.text().split(':')[0])
        self.current_course_id = course_id
        
        # Update enrollments table
        self.load_enrollments(course_id)
    
    def load_enrollments(self, course_id):
        enrollments = da.get_students(course_id)
        
        self.enrollments_table.setRowCount(len(enrollments))
        
        for row, enrollment in enumerate(enrollments):
            self.enrollments_table.setItem(row, 0, QTableWidgetItem(str(enrollment[0])))
            self.enrollments_table.setItem(row, 1, QTableWidgetItem(enrollment[1]))
            self.enrollments_table.setItem(row, 2, QTableWidgetItem(enrollment[2]))
    
    def add_student(self):
        if not hasattr(self, 'current_course_id'):
            QMessageBox.warning(self, "Warning", "Please select a course first")
            return
            
        student_name, ok = QInputDialog.getText(self, "Add Student", "Enter student name:")
        
        if ok and student_name:
            da.add_student(self.current_course_id, student_name)
            self.load_enrollments(self.current_course_id)
    
    def delete_student(self):
        selected_items = self.enrollments_table.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "Please select a student to delete")
            return
            
        row = selected_items[0].row()
        enrollment_id = int(self.enrollments_table.item(row, 0).text())
        
        confirm = QMessageBox.question(self, "Confirm Deletion", 
                                      "Are you sure you want to delete this enrollment?",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            da.delete_enrollment(enrollment_id)
            self.load_enrollments(self.current_course_id)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CourseEnrollmentApp()
    window.show()
    sys.exit(app.exec())