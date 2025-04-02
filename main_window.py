# ВАРИАНТ 9

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QTableWidget, QLineEdit

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Заказы клиентов')
		self.setFixedSize(QSize(800, 600))
		
		self.title = QLabel('Список заказов')
		self.table1 = QLabel('Стол 1')
		self.table2 = QLabel('Стол 2')
		self.table3 = QLabel('Стол 3')
		self.table_1 = QTableWidget()
		self.table_2 = QTableWidget()
		self.table_3 = QTableWidget()
		self.add_button = QPushButton('+')
		self.delete_button = QPushButton('-')
		self.new_order = QLineEdit()

		self.main_layout = QVBoxLayout()
		self.h1_layout = QHBoxLayout()
		self.h2_layout = QHBoxLayout()
		self.h3_layout = QHBoxLayout()
		self.h4_layout = QHBoxLayout()
		self.h5_layout = QHBoxLayout()

		self.main_layout.addLayout(self.h1_layout)
		self.main_layout.addLayout(self.h2_layout)
		self.main_layout.addLayout(self.h3_layout)
		self.main_layout.addLayout(self.h4_layout)
		self.main_layout.addLayout(self.h5_layout)

		self.h1_layout.addWidget(self.title)

		self.h2_layout.addWidget(self.table1)
		self.h2_layout.addWidget(self.table2)
		self.h2_layout.addWidget(self.table3)

		self.h3_layout.addWidget(self.table_1)
		self.h3_layout.addWidget(self.table_2)
		self.h3_layout.addWidget(self.table_3)

		self.h4_layout.addWidget(self.add_button)
		self.h4_layout.addWidget(self.delete_button)

		self.h5_layout.addWidget(self.new_order)
	
		self.setLayout(self.main_layout)
		

		
		


app = QApplication([])
window = MainWindow()
window.show()
app.exec()