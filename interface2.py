from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QComboBox, QTableWidget, QTableWidgetItem, QLabel, QHBoxLayout
)
import sys
import psycopg2


class WorkshopApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Распределение заказов")

        self.conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="ghost0596",
            host="localhost",
            port="5432"
        )
        self.cur = self.conn.cursor()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Комбобокс мастеров
        self.master_combo = QComboBox()
        self.load_masters()
        self.master_combo.currentIndexChanged.connect(self.load_orders)
        self.layout.addWidget(self.master_combo)

        # Таблица заказов
        self.orders_table = QTableWidget()
        self.layout.addWidget(self.orders_table)

        # Панель обновления статуса
        status_layout = QHBoxLayout()
        self.status_label = QLabel("Новый статус:")
        self.status_combo = QComboBox()
        self.status_combo.addItems(["Принят", "В работе", "Готов"])
        status_layout.addWidget(self.status_label)
        status_layout.addWidget(self.status_combo)
        self.layout.addLayout(status_layout)

        # Кнопки
        self.add_order_btn = QPushButton("Добавить заказ")
        self.update_status_btn = QPushButton("Обновить статус")
        self.layout.addWidget(self.add_order_btn)
        self.layout.addWidget(self.update_status_btn)

        # Подключение кнопок к действиям
        self.add_order_btn.clicked.connect(self.add_order)
        self.update_status_btn.clicked.connect(self.update_status)

        # Загрузка заказов при старте
        self.load_orders()

    def load_masters(self):
        self.cur.execute("SELECT id, name FROM masters")
        self.masters = self.cur.fetchall()
        self.master_combo.clear()
        for master in self.masters:
            self.master_combo.addItem(master[1], master[0])

    def load_orders(self):
        master_id = self.master_combo.currentData()
        self.cur.execute("SELECT item, issue, status FROM repairs WHERE master_id = %s", (master_id,))
        orders = self.cur.fetchall()

        self.orders_table.setRowCount(len(orders))
        self.orders_table.setColumnCount(3)
        self.orders_table.setHorizontalHeaderLabels(["Изделие", "Проблема", "Статус"])
        for row_idx, row_data in enumerate(orders):
            for col_idx, value in enumerate(row_data):
                self.orders_table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def add_order(self):
        master_id = self.master_combo.currentData()
        item = "Смартфон"
        issue = "Быстро разряжается"
        status = "Принят"
        self.cur.execute(
            "INSERT INTO repairs (master_id, item, issue, status) VALUES (%s, %s, %s, %s)",
            (master_id, item, issue, status)
        )
        self.conn.commit()
        self.load_orders()

    def update_status(self):
        selected_row = self.orders_table.currentRow()
        if selected_row == -1:
            return

        master_id = self.master_combo.currentData()
        item = self.orders_table.item(selected_row, 0).text()
        new_status = self.status_combo.currentText()

        self.cur.execute(
            "UPDATE repairs SET status = %s WHERE master_id = %s AND item = %s",
            (new_status, master_id, item)
        )
        self.conn.commit()
        self.load_orders()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WorkshopApp()
    window.show()
    sys.exit(app.exec_())