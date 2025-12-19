import sqlite3
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QTableWidget, QTableWidgetItem, QPushButton,
                             QHeaderView, QMessageBox, QInputDialog)
from PyQt6.QtCore import Qt, QSettings
from styles import apply_app_theme


class ManageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ANK Software - Management")
        self.settings = QSettings("ANK Software")
        apply_app_theme(self.settings.value("theme", "light"), self.settings.value("style", "Fusion"))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Основной макет
        self.main_h_layout = QHBoxLayout(self.central_widget)

        # Таблица (Слева)
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Zone", "Status"])
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.main_h_layout.addWidget(self.table, stretch=4)

        # Панель кнопок (Справа)
        self.right_panel = QWidget()
        self.right_layout = QVBoxLayout(self.right_panel)
        self.right_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Кнопка Добавить
        self.btn_add = QPushButton("Добавить ПК")
        self.btn_add.setFixedSize(180, 40)
        self.btn_add.clicked.connect(self.add_pc)
        self.right_layout.addWidget(self.btn_add)

        # Кнопка Изменить
        self.btn_edit = QPushButton("Изменить имя")
        self.btn_edit.setFixedSize(180, 40)
        self.btn_edit.clicked.connect(self.edit_pc)
        self.right_layout.addWidget(self.btn_edit)

        # Кнопка Удалить
        self.btn_delete = QPushButton("Удалить ПК")
        self.btn_delete.setFixedSize(180, 40)
        self.btn_delete.setStyleSheet("background-color: #c62828; color: white;")
        self.btn_delete.clicked.connect(self.delete_pc)
        self.right_layout.addWidget(self.btn_delete)

        # Кнопка Назад
        self.btn_back = QPushButton("Назад")
        self.btn_back.setFixedSize(180, 40)
        self.btn_back.clicked.connect(self.open_main_window)
        self.right_layout.addStretch()  # Отступ перед кнопкой Назад
        self.right_layout.addWidget(self.btn_back)

        self.main_h_layout.addWidget(self.right_panel, stretch=1)
        self.load_data()

    def load_data(self):
        self.table.setRowCount(0)
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, zone, status FROM computers")
        for i, row in enumerate(cursor.fetchall()):
            self.table.insertRow(i)
            for j, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(i, j, item)
        conn.close()

    def add_pc(self):
        name, ok1 = QInputDialog.getText(self, "Добавление", "Введите имя ПК:")
        zone, ok2 = QInputDialog.getItem(self, "Зона", "Выберите зону:", ["Standard", "VIP"], 0, False)

        if ok1 and ok2 and name:
            conn = sqlite3.connect("inventory.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO computers (name, zone, status) VALUES (?, ?, ?)", (name, zone, "Offline"))
            conn.commit()
            conn.close()
            self.load_data()

    def edit_pc(self):
        row = self.table.currentRow()
        if row < 0: return
        pc_id = self.table.item(row, 0).text()

        new_name, ok = QInputDialog.getText(self, "Изменение", "Новое имя ПК:")
        if ok and new_name:
            conn = sqlite3.connect("inventory.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE computers SET name = ? WHERE id = ?", (new_name, pc_id))
            conn.commit()
            conn.close()
            self.load_data()

    def delete_pc(self):
        row = self.table.currentRow()
        if row < 0: return
        pc_id = self.table.item(row, 0).text()

        reply = QMessageBox.question(self, 'Удаление', f'Удалить ПК с ID {pc_id}?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            conn = sqlite3.connect("inventory.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM computers WHERE id = ?", (pc_id,))
            conn.commit()
            conn.close()
            self.load_data()

    def open_main_window(self):
        from main_window import MainWindow
        self.mw = MainWindow()
        self.mw.showMaximized()
        self.close()