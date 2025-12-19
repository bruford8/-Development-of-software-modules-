from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from styles import apply_app_theme


class ShiftReport(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ANK Software")
        self.settings = QSettings("ANK Software")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.menuBar().addMenu("Tools").addAction("Back").triggered.connect(self.open_main_window)

        label = QLabel("Report")
        label.setFont(QFont("Arial", 20))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(label)

        self.money = self.create_input("Cash")
        self.terminal = self.create_input("Receipt")
        self.remains = self.create_input("Remains")

        main_layout.addWidget(self.money)
        main_layout.addWidget(self.terminal)
        main_layout.addWidget(self.remains)

        btn_end = QPushButton("End shift")
        btn_end.clicked.connect(self.validate_and_save)
        main_layout.addWidget(btn_end)

    def create_input(self, placeholder):
        edit = QLineEdit()
        edit.setFixedSize(350, 35)
        edit.setPlaceholderText(placeholder)
        validator = QDoubleValidator(0.0, 999999.99, 2, self)
        validator.setNotation(QDoubleValidator.Notation.StandardNotation)
        edit.setValidator(validator)
        return edit

    def validate_and_save(self):
        if not self.money.text() or not self.terminal.text():
            QMessageBox.warning(self, "Error", "Fields cannot be empty!")
            return

        self.settings.setValue("last_cash", self.money.text())
        self.open_main_window()

    def open_main_window(self):
        from main_window import MainWindow
        self.mw = MainWindow()
        self.mw.showMaximized()
        self.close()