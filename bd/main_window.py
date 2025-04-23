# 2 вариант

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
import sys
from data_accessor import HotelDB

class HotelApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Бронирование отеля")

        self.db = HotelDB()

        self.layout = QVBoxLayout()

        self.room_list = QListWidget()
        self.layout.addWidget(self.room_list)
        self.room_list.itemClicked.connect(self.load_bookings)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Гость", "Заезд", "Выезд"])
        self.layout.addWidget(self.table)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Имя гостя")
        self.layout.addWidget(self.name_input)

        self.check_in_input = QLineEdit()
        self.check_in_input.setPlaceholderText("Дата заезда (год-месяц-день)")
        self.layout.addWidget(self.check_in_input)

        self.check_out_input = QLineEdit()
        self.check_out_input.setPlaceholderText("Дата выезда (год-месяц-день)")
        self.layout.addWidget(self.check_out_input)

        self.book_button = QPushButton("Забронировать")
        self.book_button.clicked.connect(self.book_room)
        self.layout.addWidget(self.book_button)

        self.setLayout(self.layout)

        self.rooms = []
        self.load_rooms()

    def load_rooms(self):
        self.rooms = self.db.get_rooms()
        self.room_list.clear()
        for room in self.rooms:
            self.room_list.addItem(f"Номер {room[1]}")

    def get_selected_room_id(self):
        index = self.room_list.currentRow()
        if index >= 0:
            return self.rooms[index][0]
        return None

    def load_bookings(self):
        room_id = self.get_selected_room_id()
        if not room_id:
            return

        bookings = self.db.get_bookings_by_room(room_id)
        self.table.setRowCount(0)
        for booking in bookings:
            row = self.table.rowCount()
            self.table.insertRow(row)
            for col, value in enumerate(booking):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))

    def book_room(self):
        room_id = self.get_selected_room_id()
        name = self.name_input.text()
        check_in = self.check_in_input.text()
        check_out = self.check_out_input.text()
        if room_id and name and check_in and check_out:
            self.db.add_booking(room_id, name, check_in, check_out)
            self.load_bookings()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HotelApp()
    window.show()
    sys.exit(app.exec())
