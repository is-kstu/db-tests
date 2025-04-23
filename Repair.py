import sys
import psycopg2
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QListWidget, QTableWidget, QTableWidgetItem,
    QPushButton, QMessageBox, QInputDialog, QLabel
)

class RepairApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Учёт ремонтов техники")
        self.conn = self.connect_to_db()
        self.init_ui()
        self.load_devices()

    def connect_to_db(self):
        try:
            return psycopg2.connect(
                dbname="library_db",
                user="postgres",
                password="1234",
                host="localhost",
                port=5433
            )
        except psycopg2.Error as e:
            QMessageBox.critical(self, "Ошибка подключения", str(e))
            return None

    def init_ui(self):
        layout = QVBoxLayout(self)

        self.device_list = QListWidget()
        self.device_list.itemClicked.connect(self.load_repairs)
        layout.addWidget(QLabel("Устройства"))
        layout.addWidget(self.device_list)

        self.repairs_table = QTableWidget()
        self.repairs_table.setColumnCount(4)
        self.repairs_table.setHorizontalHeaderLabels(["ID", "Описание проблемы", "Статус", "Дата приёма"])
        layout.addWidget(QLabel("Ремонты"))
        layout.addWidget(self.repairs_table)

        button_layout = QHBoxLayout()

        self.add_button = QPushButton("Добавить ремонт")
        self.add_button.clicked.connect(self.add_repair)
        button_layout.addWidget(self.add_button)

        self.update_button = QPushButton("Изменить статус")
        self.update_button.clicked.connect(self.update_status)
        button_layout.addWidget(self.update_button)

        self.refresh_button = QPushButton("Обновить таблицу")
        self.refresh_button.clicked.connect(self.refresh_status)
        button_layout.addWidget(self.refresh_button)

        layout.addLayout(button_layout)

    def refresh_status(self):
        item = self.device_list.currentItem()
        if item:
            self.load_repairs(item)


    def load_devices(self):
        if not self.conn:
            return
        cur = self.conn.cursor()
        cur.execute("SELECT id, name FROM devices")
        devices = cur.fetchall()
        self.device_list.clear()
        for device in devices:
            self.device_list.addItem(f"{device[0]} - {device[1]}")

    def load_repairs(self, item):
        device_id = int(item.text().split(" - ")[0])
        cur = self.conn.cursor()
        cur.execute("SELECT id, problem_description, status, date_received FROM repairs WHERE device_id = %s", (device_id,))
        repairs = cur.fetchall()
        self.repairs_table.setRowCount(len(repairs))
        for row, repair in enumerate(repairs):
            for col, data in enumerate(repair):
                self.repairs_table.setItem(row, col, QTableWidgetItem(str(data)))

    def add_repair(self):
        item = self.device_list.currentItem()
        if not item:
            QMessageBox.warning(self, "Ошибка", "Выберите устройство")
            return
        device_id = int(item.text().split(" - ")[0])
        desc, ok = QInputDialog.getText(self, "Описание проблемы", "Введите описание проблемы:")
        if ok and desc:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO repairs (device_id, problem_description, status, date_received)
                VALUES (%s, %s, 'В обработке', now())
            """, (device_id, desc))
            self.conn.commit()
            self.load_repairs(item)

    def update_status(self):
        row = self.repairs_table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите ремонт")
            return
        repair_id = int(self.repairs_table.item(row, 0).text())
        new_status, ok = QInputDialog.getText(self, "Обновить статус", "Введите новый статус:")
        if ok and new_status:
            cur = self.conn.cursor()
            cur.execute("UPDATE repairs SET status = %s WHERE id = %s", (new_status, repair_id))
            self.conn.commit()
            self.device_list.setCurrentItem(self.device_list.currentItem())  # перезагрузить

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RepairApp()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
