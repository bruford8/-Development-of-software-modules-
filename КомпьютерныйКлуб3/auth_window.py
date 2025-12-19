from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from styles import apply_app_theme


class Autorization(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ANK Software")
        self.settings = QSettings("ANK Software", "ThemeSettings")

        saved_theme = self.settings.value("theme", "light")
        saved_style = self.settings.value("style", "Fusion")
        apply_app_theme(saved_theme, saved_style)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel("Autorization")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont();
        font.setPointSize(15)
        self.label.setFont(font)
        main_layout.addWidget(self.label)

        self.autorization1 = QLineEdit("управляющий")
        self.autorization2 = QLineEdit("09112001")
        for widget in [self.autorization1, self.autorization2]:
            widget.setFixedSize(350, 22)
            main_layout.addWidget(widget)

        self.autorization2.setEchoMode(QLineEdit.EchoMode.Password)
        self.button_auth = QPushButton("Login")
        self.button_auth.clicked.connect(self.check_credentials)
        main_layout.addWidget(self.button_auth)

    def check_credentials(self):
        if self.autorization1.text() == "управляющий" and self.autorization2.text() == "09112001":
            self.open_main_window()
        else:
            QMessageBox.warning(self, "Error", "Wrong login, or password!")

    def open_main_window(self):
        from main_window import MainWindow  # Импорт внутри метода во избежание циклической зависимости
        self.mw = MainWindow()
        self.mw.showMaximized()
        self.close()