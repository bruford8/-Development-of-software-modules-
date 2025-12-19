from PyQt6.QtGui import QPainter, QPixmap
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from styles import apply_app_theme
from manage_window import ManageWindow
from computers_window import ComputersWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ANN Software")
        self.settings = QSettings("ANK Software")

        theme = self.settings.value("theme", "light")
        style = self.settings.value("style", "Fusion")
        apply_app_theme(theme, style)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        main_layout = QVBoxLayout(self.central_widget)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        menu_bar = self.menuBar()
        manager_menu = menu_bar.addMenu("Manager")
        manager_menu.addAction("Shift report").triggered.connect(self.open_shift_report)
        manager_menu.addAction("Exit").triggered.connect(self.open_autorization_window)

        tools_menu = menu_bar.addMenu("Tools")
        tools_menu.addAction("Settings").triggered.connect(self.open_settings_window)

        self.computers = QPushButton("Computers")
        self.computers.setFixedSize(200, 40)
        main_layout.addStretch()
        main_layout.addWidget(self.computers)
        self.computers.clicked.connect(self.open_computers_db)

        self.users = QPushButton("Users")
        self.computers.setFixedSize(200, 40)
        main_layout.addWidget(self.users)

        self.manage = QPushButton("Manage")
        self.manage.setFixedSize(200, 40)
        self.manage.clicked.connect(self.open_manage)
        main_layout.addWidget(self.manage)

    def open_manage(self):
        self.man_win = ManageWindow()
        self.man_win.showMaximized()
        self.close()

    def open_autorization_window(self):
        from auth_window import Autorization
        self.auth = Autorization()
        self.auth.showMaximized()
        self.close()

    def open_settings_window(self):
        from settings_window import Settings
        self.st = Settings()
        self.st.showMaximized()
        self.close()

    def open_shift_report(self):
        from report_window import ShiftReport
        self.sr = ShiftReport()
        self.sr.showMaximized()
        self.close()

    def open_computers_db(self):
        self.comp_win = ComputersWindow()
        self.comp_win.showMaximized()
        self.close()