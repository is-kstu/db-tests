import psycopg2
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout, QTableWidget
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt, QSize
from PyQt6 import QtWidgets
import sys
from insert_modal import InsertModal

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setFixedSize(QSize(600, 400))
        self.mainLayout = QtWidgets.QHBoxLayout()
        self.current_tab = 0

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout2 = QtWidgets.QVBoxLayout()

        text_request = QtWidgets.QLabel("Запросы")
        request_button1 = QPushButton("Первый запрос")
        request_button2 = QPushButton("Второй запрос")
        request_button3 = QPushButton("Третий запрос")
        self.verticalLayout.addWidget(text_request)
        self.verticalLayout.addWidget(request_button1)
        self.verticalLayout.addWidget(request_button2)
        self.verticalLayout.addWidget(request_button3)

        self.horizontalLayoutButtons = QtWidgets.QHBoxLayout()

        self.tabWidget = QtWidgets.QTabWidget()

        self.table1 = QTableWidget(self)
        self.table2 = QTableWidget(self)
        self.table3 = QTableWidget(self)

        # self.table1.setColumnCount(3)     #Set three columns
        # self.table1.setRowCount(1)

        self.tabWidget.addTab(self.table1, "dep")
        self.tabWidget.addTab(self.table2, "emp")
        self.tabWidget.addTab(self.table3, "proj")

        self.tabWidget.currentChanged.connect(self.on_tab_changed)

        self.addButton = QPushButton("+")
        self.refreshButton = QPushButton("*")

        self.horizontalLayoutButtons.addWidget(self.addButton)
        self.horizontalLayoutButtons.addWidget(self.refreshButton)

        self.addButton.clicked.connect(self.new_employee)

        self.setLayout(self.mainLayout)
        self.mainLayout.addLayout(self.verticalLayout)
        self.mainLayout.addLayout(self.verticalLayout2)
        self.verticalLayout2.addWidget(self.tabWidget)
        self.verticalLayout2.addLayout(self.horizontalLayoutButtons)
        
    def new_employee(self):
        insert_modal = InsertModal(self.current_tab)
        insert_modal.exec()

    def on_tab_changed(self, tab_index):
        self.current_tab = tab_index
        print(self.current_tab, tab_index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
