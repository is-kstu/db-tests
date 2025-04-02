from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.button_get_all = QPushButton()
		self.button_add_new = QPushButton()
		self.button_del = QPushButton()
		
		
		buttons = QVBoxLayout()
		buttons.addWidget(self.button_get_all)
		buttons.addWidget(self.button_add_new)
		buttons.addWidget(self.button_del)
		

		
		
		widget = QWidget()
		widget.setLayout(buttons)
		
		self.setCentralWidget(widget)
		
		
		
		

app = QApplication([])
window = MainWindow()
window.show()
app.exec()