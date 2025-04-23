import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QComboBox, QTableWidget, QInputDialog,
    QTableWidgetItem, QPushButton, QLabel, QMessageBox, QHeaderView,
    QAbstractItemView
)
from env import DB_PARAMS
from dataAccessor import DataAccessor

class RepairApp(QWidget):
    def __init__(self):
        super().__init__()
        self.db = DataAccessor(DB_PARAMS)
        self.current_master_id = None
        self.possible_statuses = ['Новый', 'В работе', 'Ожидает запчасть', 'Готов', 'Отменен']

        self.setWindowTitle('Мастерская: Заказы')
        self.setGeometry(250, 250, 600, 450)
        self.initUI()
        self.load_masters()

    def initUI(self):
        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Мастер:"))
        self.master_combo = QComboBox()
        self.master_combo.currentIndexChanged.connect(self.master_changed)
        layout.addWidget(self.master_combo)

        layout.addWidget(QLabel("Заказы мастера:"))
        self.repairs_table = QTableWidget()
        self.repairs_table.setColumnCount(4)
        self.repairs_table.setHorizontalHeaderLabels(["ID", "Предмет", "Проблема", "Статус"])
        layout.addWidget(self.repairs_table)
        
        self.add_button = QPushButton("Добавить заказ")
        self.add_button.clicked.connect(self.add_repair_dialog)
        layout.addWidget(self.add_button)

        self.update_button = QPushButton("Обновить статус")
        self.update_button.clicked.connect(self.update_status_dialog)
        layout.addWidget(self.update_button)

        self.setLayout(layout)

    def load_masters(self):
        self.master_combo.clear()
        masters = self.db.get_masters()
        self.master_combo.addItem("Нет мастера", None)
        if masters:
            for m_id, name in masters:
                self.master_combo.addItem(name, m_id)

    def master_changed(self):
        selected_index = self.master_combo.currentIndex()
        if selected_index >= 0:
            self.current_master_id = self.master_combo.itemData(selected_index)
            self.load_repairs(self.current_master_id)
        else:
            self.current_master_id = None
            self.repairs_table.setRowCount(0)

    def load_repairs(self, master_id):
        repairs = self.db.get_repairs_by_master(master_id)
        self.repairs_table.setRowCount(len(repairs))

        for row_idx, repair_data in enumerate(repairs):
            repair_id, item, issue, status = repair_data
            id_item = QTableWidgetItem(str(repair_id))
            id_item.setData(1, repair_id)
            item_item = QTableWidgetItem(item)
            issue_item = QTableWidgetItem(issue)
            status_item = QTableWidgetItem(status)
            self.repairs_table.setItem(row_idx, 0, id_item) 
            self.repairs_table.setItem(row_idx, 1, item_item)
            self.repairs_table.setItem(row_idx, 2, issue_item)
            self.repairs_table.setItem(row_idx, 3, status_item)
        self.repairs_table.resizeColumnsToContents()
        self.repairs_table.horizontalHeader().setStretchLastSection(True)

    def add_repair_dialog(self):
        master_name = self.master_combo.currentText()
        master_id_to_assign = self.current_master_id

        item, ok1 = QInputDialog.getText(self, 'Новый заказ', f'Предмет (Мастер: {master_name}):')
        if ok1 and item:
            issue, ok2 = QInputDialog.getText(self, 
            'Новый заказ', 'Проблема:')
            if ok2:input dialog pyqt6
                self.db.add_repair(master_id_to_assign, item, issue if issue else "")
                self.load_repairs(self.current_master_id)
        elif ok1 and not item:
             QMessageBox.warning(self, "Отмена", "Название пустое")

    def update_status_dialog(self):
        selected_rows = self.repairs_table.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Ошибка", "Выберите вариант")
            return

        selected_row_index = selected_rows[0].row()
        repair_id_item = self.repairs_table.item(selected_row_index, 0)
        if not repair_id_item: return
        repair_id = repair_id_item.data(1)

        current_status_item = self.repairs_table.item(selected_row_index, 3)
        current_status = current_status_item.text() if current_status_item else ""

        new_status, ok = QInputDialog.getItem(self, 'Обновить статус',
                                              f'Новый статус ID: {repair_id}',
                                              self.possible_statuses,
                                              self.possible_statuses.index(current_status) if current_status in self.possible_statuses else 0,
                                              editable=False)input dialog pyqt6`

        if ok and new_status:
            self.db.update_repair_status(repair_id, new_status)
            self.load_repairs(self.current_master_id)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RepairApp()
    window.show()
    sys.exit(app.exec())
