import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidgetItem, QDialog, QAbstractItemView, QFormLayout, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt
from create_tables import create_tables
from data_accessor import DataAccessor
	

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.data_accessor = DataAccessor()
		self.initUI()
		self.load_devices()


	def initUI(self):
		
		self.setWindowTitle("Управление ремонтами техники")
	        # self.setFixedSize(800, 600)
		self.resize(1000, 600)
		
		main_horizontal_layout = QHBoxLayout()
		vertical_layout = QVBoxLayout()
		buttons_horizontal_layout = QHBoxLayout()


		# Таблица устройств
		self.devices_table = QTableWidget()
		self.devices_table.setColumnCount(3)
		self.devices_table.setHorizontalHeaderLabels(['id', 'name', 'serial_number'])
		self.devices_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
		self.devices_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
		self.devices_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
		self.devices_table.horizontalHeader().setStretchLastSection(True)
		self.devices_table.setMinimumWidth(300)
		self.devices_table.itemSelectionChanged.connect(self.on_device_selected) # сигнал

 

		# Таблица ремонтов
		self.repairs_table = QTableWidget()
		self.repairs_table.setColumnCount(5)
		self.repairs_table.setHorizontalHeaderLabels(['id', 'device_id', 'problem_description', 'status', 'data_recived'])
		self.repairs_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
		self.repairs_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
		self.repairs_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
		self.repairs_table.horizontalHeader().setStretchLastSection(True)


		# Кнопки
		self.add_repair_button = QPushButton('Добавить ремонт')
		self.add_repair_button.clicked.connect(self.add_repair_clicked)

		self.change_status_button = QPushButton('Изменить статус')
		self.change_status_button.clicked.connect(self.change_status_clicked)

		self.refresh_table_button = QPushButton('Обновить таблицу')
		self.refresh_table_button.clicked.connect(self.load_devices)


		buttons_horizontal_layout.addWidget(self.add_repair_button)
		buttons_horizontal_layout.addWidget(self.change_status_button)
		buttons_horizontal_layout.addWidget(self.refresh_table_button)

		vertical_layout.addWidget(self.repairs_table)
		vertical_layout.addLayout(buttons_horizontal_layout)
		
		main_horizontal_layout.addWidget(self.devices_table)
		main_horizontal_layout.addLayout(vertical_layout)

		container = QWidget()
		container.setLayout(main_horizontal_layout)
	
		self.setCentralWidget(container)

	def load_devices(self):
		devices = self.data_accessor.get_all_devices()
		self.devices_table.setRowCount(0)
		
		for row, device in enumerate (devices):
			self.devices_table.insertRow(row)
			self.devices_table.setItem(row, 0, QTableWidgetItem(str(device[0])))
			self.devices_table.setItem(row, 1, QTableWidgetItem(device[1]))
			self.devices_table.setItem(row, 2, QTableWidgetItem(str(device[2])))

	def load_repairs(self, device_id):
		repairs = self.data_accessor.get_all_repairs(device_id)
		self.repairs_table.setRowCount(0)
		
		for row, repair in enumerate (repairs):
			self.repairs_table.insertRow(row)
			self.repairs_table.setItem(row, 0, QTableWidgetItem(str(repair[0])))
			self.repairs_table.setItem(row, 1, QTableWidgetItem(str(repair[1])))
			self.repairs_table.setItem(row, 2, QTableWidgetItem(repair[2]))
			self.repairs_table.setItem(row, 3, QTableWidgetItem(repair[3]))
			
			date_str = repair[4].strftime("%d.%m.%Y %H:%M")
			self.repairs_table.setItem(row, 4, QTableWidgetItem(date_str)) # дата
	
	def on_device_selected(self):
		selected_items = self.devices_table.selectedItems()
		if selected_items:

			selected_row = selected_items[0].row()
			device_id = int(self.devices_table.item(selected_row, 0).text())
			self.load_repairs(device_id)

	def add_repair_clicked(self):
		selected_items = self.devices_table.selectedItems()
		if not selected_items:
			QMessageBox.warning(self, "", "Выберите устройство из списка")
			return
		selected_row = selected_items[0].row()
		device_id = int(self.devices_table.item(selected_row, 0).text())
		device_name = self.devices_table.item(selected_row, 1).text()
		dia_window = AddRepairDialog(device_id, device_name)
		if dia_window.exec() == QDialog.DialogCode.Accepted:
			repair_data = dia_window.get_repair_data()
			self.data_accessor.add_repair(repair_data[0], repair_data[1], repair_data[2])

		self.load_repairs(device_id)
		
	def change_status_clicked(self):
		selected_items = self.repairs_table.selectedItems()
		if not selected_items:
			QMessageBox.warning(self, "", "Выберите запись ремонта для изменения статуса")
			return
		row = selected_items[0].row()
		repair_id = int(self.repairs_table.item(row, 0).text())
		current_status = self.repairs_table.item(row, 3).text()
		dia_window = ChangeStatusDialog(current_status)
		if dia_window.exec() == QDialog.DialogCode.Accepted:
			new_status = dia_window.get_new_status()
			self.data_accessor.change_status(repair_id, new_status)

			device_items = self.devices_table.selectedItems()
			if device_items:
				selected_row = device_items[0].row()
				device_id = int(self.devices_table.item(selected_row, 0).text())
				self.load_repairs(device_id)

			
class AddRepairDialog(QDialog):
	def __init__(self, device_id, device_name):
		super().__init__()
		self.device_id = device_id
		self.device_name = device_name
		self.initUI()
        
	def initUI(self):
		self.setWindowTitle("Добавить ремонт")
		layout = QFormLayout()

		self.device_label = QLabel(f"Устройство: {self.device_name}")
		self.problem_description = QLineEdit('Проблема устройства')
		self.status = QLineEdit('Введите статус')
	
        
		layout.addRow(self.device_label)
		layout.addRow("Описание проблемы:", self.problem_description)
		layout.addRow("Статус:", self.status)
        
		button_layout = QHBoxLayout()
		self.ok_button = QPushButton("OK")
		self.cancel_button = QPushButton("Отмена")
        
		self.ok_button.clicked.connect(self.accept)
		self.cancel_button.clicked.connect(self.reject)
        
		button_layout.addWidget(self.ok_button)
		button_layout.addWidget(self.cancel_button)
        
		layout.addRow(button_layout)
		self.setLayout(layout)
        
	def get_repair_data(self):
		return (self.device_id, self.problem_description.text(), self.status.text())
	

class ChangeStatusDialog(QDialog):
	def __init__(self, current_status):
		super().__init__()
		self.current_status = current_status
		self.initUI()
        
	def initUI(self):
		self.setWindowTitle("Изменить статус")
		layout = QFormLayout()
        
		self.status = QLineEdit('Введите другой статус')
    
        
		layout.addRow("Новый статус:", self.status)
        
		button_layout = QHBoxLayout()
		self.ok_button = QPushButton("OK")
		self.cancel_button = QPushButton("Отмена")
        
		self.ok_button.clicked.connect(self.accept)
		self.cancel_button.clicked.connect(self.reject)
        
		button_layout.addWidget(self.ok_button)
		button_layout.addWidget(self.cancel_button)
        
		layout.addRow(button_layout)
		self.setLayout(layout)
        
	def get_new_status(self):
		return self.status.text()
		
            	
if __name__ == "__main__":
    create_tables()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())









