# 6 var
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QComboBox
)
from dataAccessor import DataAccessor

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.data_accessor = DataAccessor()
        self.init_ui()

    def init_ui(self):                      
        self.setWindowTitle("Cars")
        self.layout = QVBoxLayout(self)
        self.h_layout = QHBoxLayout()
            
        self.cars = data_accessor.getCars()
        
        self.table = QTableWidget(5, cars.length)
        
        # ИМЯ
        self.input_field1 = QLineEdit(self)
        self.layout.addWidget(self.input_field1)
        # birth_date
        self.input_field2 = QLineEdit(self)
        self.layout.addWidget(self.input_field2)
        # brand
        self.input_field3 = QLineEdit(self)
        self.layout.addWidget(self.input_field3)
        #model
        self.input_field4 = QLineEdit(self)
        self.layout.addWidget(self.input_field4)
        #year
        self.input_field5 = QLineEdit(self)
        self.layout.addWidget(self.input_field5)
        #id
        self.input_field6 = QLineEdit(self)
        self.layout.addWidget(self.input_field6)


        self.button1 = QPushButton("Add", self)
        self.button1.clicked.connect(self.add_car)
        self.h_layout.addWidget(self.button2)

        self.button2 = QPushButton("Delete", self)
        self.button2.clicked.connect(self.delete_car)
        self.h_layout.addWidget(self.button3)

        self.layout.addLayout(self.h_layout)

        self.combo_box = QComboBox(self)
        self.layout.addWidget(self.combo_box)

    def add_car(self):
        name = self.input_field1.text()
        birth_date = self.input_field2.text()
        brand = self.input_field3.text()
        model = self.input_field4.text()
        year = self.input_field5.text()

        self.data_accessor.addCar(name, birth_date, brand, model, year)
        print(f"Added car: {model}")

    def delete_car(self):
        id = self.input_field6.text()
        self.data_accessor.deleteCar

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
