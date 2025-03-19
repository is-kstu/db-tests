from PyQt6 import QtWidgets
from data_accessor import DataAccessor

class InsertModal(QtWidgets.QDialog):
    def __init__(self, current_tab):
        super().__init__()
        if current_tab == 0:
            self.__init_ui_for_departments()
            self.setWindowTitle('new department')
        elif current_tab == 1:
            self.setWindowTitle('new employee')
            self.__init_ui_for_employees()

    def __init_ui_for_departments(self):
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.name_edit = QtWidgets.QLineEdit()
        self.vertical_layout.addWidget(self.name_edit)
        self.insert_button = QtWidgets.QPushButton()
        self.insert_button.setText('add')
        self.insert_button.clicked.connect(self.add_new_department)
        self.vertical_layout.addWidget(self.insert_button)
        self.setLayout(self.vertical_layout)

    def __init_ui_for_employees(self):
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.name_edit = QtWidgets.QLineEdit()
        self.vertical_layout.addWidget(self.name_edit)
        self.departments_dropdown = QtWidgets.QComboBox()
        self.vertical_layout.addWidget(self.departments_dropdown)
        self.get_all_departments()
        self.salary_edit = QtWidgets.QLineEdit()
        self.vertical_layout.addWidget(self.salary_edit)
        self.insert_button = QtWidgets.QPushButton()
        self.insert_button.setText('add')
        self.insert_button.clicked.connect(self.add_new_employee)
        self.vertical_layout.addWidget(self.insert_button)
        self.setLayout(self.vertical_layout)

    def add_new_employee(self):
        employee_name = self.name_edit.text()
        department = self.departments_dropdown.currentText()
        salary = self.salary_edit.text()
        data_accessor = DataAccessor()
        data_accessor.add_new_employee(employee_name, department, salary)
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Информация")
        msg.setText("employee has been added!")
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)

        msg.exec()  # Отображение окна

    def add_new_department(self):
        department_name = self.name_edit.text()
        data_accessor = DataAccessor()
        data_accessor.add_new_department(department_name)
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Информация")
        msg.setText("department has been added!")
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)

        msg.exec()  # Отображение окна

    def get_all_departments(self):
        data_accessor = DataAccessor()
        departments = data_accessor.select_all_departments()
        for department in departments:
            self.departments_dropdown.addItem(department[1])