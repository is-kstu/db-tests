import sys
import psycopg2
import warnings
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QListWidget, QMessageBox
)

# Подавляем DeprecationWarning для устаревшей функции sipPyTypeDict()
warnings.filterwarnings("ignore", category=DeprecationWarning)

class ProductApp(QWidget):
    def __init__(self):
        QWidget.__init__(self)  # Явный вызов конструктора родителя
        self.setWindowTitle("Управление товарами")
        self.resize(400, 400)
        self.init_ui()
        self.connect_db()
        self.load_data()

    def connect_db(self):
        try:
            self.conn = psycopg2.connect(
                dbname="shop_db",
                user="postgres",
                password="your_password",  # ← замените на ваш реальный пароль
                host="localhost",
                port="5432"
            )
            print("Подключение к базе данных успешно!")  # Debug: проверяем подключение
            self.cursor = self.conn.cursor()  # Создаём курсор для выполнения SQL-запросов
            print("Курсор создан!")  # Debug: проверяем создание курсора

            # Дополнительная проверка, что курсор является объектом курсора
            if not hasattr(self.cursor, 'execute'):
                print("Ошибка: self.cursor не является объектом курсора!")
                QMessageBox.critical(self, "Ошибка", "Ошибка с созданием курсора.")
            else:
                print("Курсор корректен!")

        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")
            QMessageBox.critical(self, "Ошибка подключения", str(e))

    def init_ui(self):
        layout = QVBoxLayout()

        self.product_list = QListWidget()
        self.category_list = QListWidget()

        form_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Название товара")
        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Цена")
        self.category_input = QLineEdit()
        self.category_input.setPlaceholderText("ID категории")
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.price_input)
        form_layout.addWidget(self.category_input)

        self.add_button = QPushButton("Добавить товар")
        self.add_button.clicked.connect(self.add_product)

        layout.addWidget(QLabel("Товары:"))
        layout.addWidget(self.product_list)
        layout.addWidget(QLabel("Категории:"))
        layout.addWidget(self.category_list)
        layout.addLayout(form_layout)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def load_data(self):
        self.product_list.clear()
        self.category_list.clear()
        try:
            # Проверка, что курсор правильно создан
            if hasattr(self.cursor, 'execute'):
                print("Загружаем товары...")
                self.cursor.execute("SELECT id, name, price, category_id FROM products")
                products = self.cursor.fetchall()
                for p in products:
                    self.product_list.addItem(f"[{p[0]}] {p[1]} - {p[2]} тг (категория {p[3]})")

                print("Загружаем категории...")
                self.cursor.execute("SELECT id, name FROM categories")
                categories = self.cursor.fetchall()
                for c in categories:
                    self.category_list.addItem(f"[{c[0]}] {c[1]}")
            else:
                raise Exception("Курсор не был создан должным образом!")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка загрузки", f"Ошибка: {str(e)}")

    def add_product(self):
        name = self.name_input.text()
        try:
            price = float(self.price_input.text())
            category_id = int(self.category_input.text())
        except ValueError:
            QMessageBox.warning(self, "Неверный ввод", "Цена и ID категории должны быть числами.")
            return

        if not name:  # Проверка на пустое название
            QMessageBox.warning(self, "Неверный ввод", "Название товара не может быть пустым.")
            return

        try:
            self.cursor.execute(
                "INSERT INTO products (name, price, category_id) VALUES (%s, %s, %s)",
                (name, price, category_id)
            )
            self.conn.commit()
            self.name_input.clear()
            self.price_input.clear()
            self.category_input.clear()
            self.load_data()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка добавления", f"Ошибка: {str(e)}")

    def closeEvent(self, event):
        try:
            self.conn.close()  # Закрытие соединения при закрытии приложения
        except Exception as e:
            print(f"Ошибка при закрытии соединения: {e}")
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductApp()
    window.show()
    sys.exit(app.exec())
