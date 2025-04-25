from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QListWidget,
    QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QMessageBox, QInputDialog
)
import db

class ProductManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Управление товарами")
        self.resize(600, 400)

        self.layout = QVBoxLayout(self)

        self.category_list = QListWidget()
        self.category_list.itemClicked.connect(self.load_products)
        self.layout.addWidget(self.category_list)

        self.product_table = QTableWidget()
        self.product_table.setColumnCount(3)
        self.product_table.setHorizontalHeaderLabels(["ID", "Название", "Цена"])
        self.layout.addWidget(self.product_table)

        btn_layout = QHBoxLayout()
        self.btn_add = QPushButton("Добавить товар")
        self.btn_delete = QPushButton("Удалить товар")
        self.btn_add.clicked.connect(self.add_product)
        self.btn_delete.clicked.connect(self.delete_product)
        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_delete)
        self.layout.addLayout(btn_layout)

        self.load_categories()

    def load_categories(self):
        self.categories = db.get_categories()
        self.category_list.clear()
        for cat_id, name in self.categories:
            self.category_list.addItem(f"{cat_id}: {name}")

    def load_products(self):
        selected = self.category_list.currentItem()
        if not selected:
            return
        cat_id = int(selected.text().split(":")[0])
        self.current_category_id = cat_id

        products = db.get_products_by_category(cat_id)
        self.product_table.setRowCount(len(products))
        for row, (prod_id, name, price) in enumerate(products):
            self.product_table.setItem(row, 0, QTableWidgetItem(str(prod_id)))
            self.product_table.setItem(row, 1, QTableWidgetItem(name))
            self.product_table.setItem(row, 2, QTableWidgetItem(str(price)))

    def add_product(self):
        if not hasattr(self, "current_category_id"):
            QMessageBox.warning(self, "Ошибка", "Выберите категорию")
            return
        name, ok = QInputDialog.getText(self, "Добавить товар", "Название товара:")
        if not ok or not name:
            return
        price, ok = QInputDialog.getDouble(self, "Цена", "Введите цену:")
        if not ok:
            return
        db.add_product(name, price, self.current_category_id)
        self.load_products()

    def delete_product(self):
        selected = self.product_table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите товар для удаления")
            return
        product_id = int(self.product_table.item(selected, 0).text())
        db.delete_product(product_id)
        self.load_products()


if __name__ == "__main__":
    app = QApplication([])
    window = ProductManager()
    window.show()
    app.exec()
