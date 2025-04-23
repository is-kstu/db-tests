from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QComboBox, QLineEdit, QLabel, QListWidget, QMessageBox
)
from Data_accessor import DataAccessor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Туристическое агентство")
        self.db = DataAccessor()
        self.setup_ui()

    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()

        self.tour_combo = QComboBox()
        self.tour_combo.currentIndexChanged.connect(self.load_clients)
        layout.addWidget(QLabel("Выберите тур:"))
        layout.addWidget(self.tour_combo)

        self.client_list = QListWidget()
        layout.addWidget(QLabel("Клиенты по туру:"))
        layout.addWidget(self.client_list)


        form = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Имя клиента")
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Телефон")
        form.addWidget(self.name_input)
        form.addWidget(self.phone_input)
        layout.addLayout(form)


        btn_layout = QHBoxLayout()
        add_btn = QPushButton("Зарегистрировать")
        del_btn = QPushButton("Удалить клиента")
        add_btn.clicked.connect(self.add_client)
        del_btn.clicked.connect(self.delete_client)
        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(del_btn)
        layout.addLayout(btn_layout)

        central.setLayout(layout)
        self.load_tours()

    def load_tours(self):
        self.tour_combo.clear()
        for tour_id, country in self.db.get_tours():
            self.tour_combo.addItem(country, tour_id)

    def load_clients(self):
        self.client_list.clear()
        tour_id = self.tour_combo.currentData()
        if tour_id:
            for name, phone in self.db.get_clients_by_tour(tour_id):
                self.client_list.addItem(f"{name} ({phone})")

    def add_client(self):
        tour_id = self.tour_combo.currentData()
        name = self.name_input.text()
        phone = self.phone_input.text()
        if not name or not phone:
            QMessageBox.warning(self, "Ошибка", "Имя и телефон обязательны")
            return
        self.db.add_client(tour_id, name, phone)
        self.load_clients()
        self.name_input.clear()
        self.phone_input.clear()

    def delete_client(self):
        selected = self.client_list.currentItem()
        if selected:
            name = selected.text().split(" (")[0]
            self.db.delete_client(name)
            self.load_clients()
