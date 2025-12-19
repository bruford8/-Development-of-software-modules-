import sqlite3

from PyQt6.QtGui import QPainter, QPixmap
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QTableWidget, QTableWidgetItem, QLabel, QPushButton,
                             QHeaderView, QMessageBox)
from PyQt6.QtCore import Qt, QSettings
from styles import apply_app_theme


class ComputersWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ANK Software")
        self.settings = QSettings("ANK Software")

        theme = self.settings.value("theme", "light")
        style = self.settings.value("style", "Fusion")
        apply_app_theme(theme, style)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.main_h_layout = QHBoxLayout(central_widget)

        self.left_container = QWidget()
        self.left_layout = QVBoxLayout(self.left_container)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Zone", "Status"])
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.left_layout.addWidget(self.table)

        self.button_back = QPushButton("Back")
        self.button_back.setFixedSize(150, 35)
        self.button_back.clicked.connect(self.open_main_window)
        self.left_layout.addWidget(self.button_back)

        self.main_h_layout.addWidget(self.left_container, stretch=4)

        self.right_panel = QWidget()
        self.right_layout = QVBoxLayout(self.right_panel)
        self.right_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.btn_turn_on = QPushButton("Включить ПК")
        self.btn_turn_on.setFixedSize(350, 40)
        self.btn_turn_on.clicked.connect(lambda: self.update_status("Online"))
        self.right_layout.addWidget(self.btn_turn_on)

        self.btn_turn_off = QPushButton("Выключить ПК")
        self.btn_turn_off.setFixedSize(350, 40)
        self.btn_turn_off.clicked.connect(lambda: self.update_status("Offline"))
        self.right_layout.addWidget(self.btn_turn_off)

        self.main_h_layout.addWidget(self.right_panel, stretch=1)

        self.load_data()

    def update_status(self, new_status):
        selected_row = self.table.currentRow()

        if selected_row < 0:
            QMessageBox.warning(self, "Внимание", "Пожалуйста, выберите компьютер в таблице!")
            return

        pc_id = self.table.item(selected_row, 0).text()

        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE computers SET status = ? WHERE id = ?", (new_status, pc_id))
        conn.commit()
        conn.close()

        self.load_data()

    def load_data(self):
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS computers
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT,
                            zone TEXT,
                           status TEXT,
                          authorization TEXT)''')

        cursor.execute("SELECT COUNT(*) FROM computers")
        count = cursor.fetchone()[0]

        if count == 0:
            for i in range(1, 26):
                name = f"PC-{i}"
                if i <= 20:
                    zone = "Standard"
                else:
                    zone = "VIP"

                status = "Offline"
                cursor.execute("INSERT INTO computers (name, zone, status) VALUES (?, ?, ?)",
                               (name, zone, status))
            conn.commit()

        cursor.execute("UPDATE computers SET zone = 'Standart' WHERE zone IS NULL OR zone = 'None'")
        conn.commit()

        cursor.execute("SELECT id, name, zone, status FROM computers")
        rows = cursor.fetchall()

        self.table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(i, j, item)

        conn.close()

    def open_main_window(self):
        from main_window import MainWindow
        self.mw = MainWindow()
        self.mw.showMaximized()
        self.close()

    def open_settings_window(self):
        from settings_window import Settings
        self.st = Settings()
        self.st.showMaximized()
        self.close()
