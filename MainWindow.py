from PyQt6.QtWidgets import (
    QVBoxLayout, QWidget, QApplication, QLineEdit,
    QFormLayout, QPushButton, QTableWidget, QTableWidgetItem
)
import sys
import psycopg2
from DataAccessor import DataAccessor  # Убедись, что файл DataAccessor.py существует

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Управление кинотеатром")
        self.setGeometry(100, 100, 1000, 600)

        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.movie_id = QLineEdit()
        self.date_time = QLineEdit()
        self.hall_number = QLineEdit()
        self.id_v = QLineEdit()
        self.movie_id_v = QLineEdit()

        form_layout.addRow("Id фильма:", self.movie_id)
        form_layout.addRow("Время:", self.date_time)
        form_layout.addRow("Зал:", self.hall_number)
        form_layout.addRow("Id сеанса для удаления:", self.id_v)
        form_layout.addRow("Id фильма для поиска:", self.movie_id_v)

        self.add_screen_but = QPushButton("Добавить сеанс")
        self.add_screen_but.clicked.connect(self.add_new_screen)

        self.delete_screen_but = QPushButton("Удалить сеанс")
        self.delete_screen_but.clicked.connect(self.delete_screen)

        self.view_screenings_but = QPushButton("Показать сеансы")
        self.view_screenings_but.clicked.connect(self.get_screenings)

        self.screening_table = QTableWidget(0, 4)
        self.screening_table.setHorizontalHeaderLabels(["Id сеанса", "Id фильма", "Время", "Зал"])

        layout.addLayout(form_layout)
        layout.addWidget(self.add_screen_but)
        layout.addWidget(self.delete_screen_but)
        layout.addWidget(self.view_screenings_but)
        layout.addWidget(self.screening_table)

        self.setLayout(layout)

    def add_new_screen(self):
        movie_id = self.movie_id.text()
        date_time = self.date_time.text()
        hall_number = int(self.hall_number.text())

        accessor = DataAccessor()
        accessor.add_new_screen(movie_id, date_time, hall_number)

    def delete_screen(self):
        screen_id = self.id_v.text()

        accessor = DataAccessor()
        accessor.delete_screen(screen_id)

    def get_screenings(self):
        movie_id = int(self.movie_id_v.text())

        accessor = DataAccessor()
        screenings = accessor.get_screen(movie_id)

        self.screening_table.setRowCount(0)
        for row_index, row_data in enumerate(screenings):
            self.screening_table.insertRow(row_index)
            for col_index, value in enumerate(row_data):
                self.screening_table.setItem(row_index, col_index, QTableWidgetItem(str(value)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
