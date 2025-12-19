from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QLabel,
                             QPushButton, QGroupBox, QComboBox, QApplication)
from PyQt6.QtCore import Qt, QSettings
from PyQt6.QtGui import QFont, QPalette, QColor, QPixmap, QPainter
from styles import apply_app_theme

class Settings(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ANK Software")

        self.settings = QSettings("ANK Software")
        self.current_theme = self.settings.value("theme", "light")
        self.current_style = self.settings.value("style", "Windows")

        self.apply_theme_and_style(self.current_theme, self.current_style)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        menu_bar = self.menuBar()
        tools_menu = menu_bar.addMenu("Tools")
        back_action = tools_menu.addAction("Back")
        back_action.triggered.connect(self.open_main_window)

        title_label = QLabel("Settings")
        title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        font = QFont()
        font.setPointSize(18)
        title_label.setFont(font)
        main_layout.addWidget(title_label)

        color_theme_label = QLabel("Light/Dark themes")
        color_theme_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPointSize(14)
        color_theme_label.setFont(font)
        main_layout.addWidget(color_theme_label)

        theme_group = QGroupBox()
        theme_group.setFixedSize(250, 80)
        theme_layout = QVBoxLayout()

        self.light_theme_btn = QPushButton("Light theme")
        self.dark_theme_btn = QPushButton("Dark theme")

        self.light_theme_btn.clicked.connect(lambda: self.change_color_theme("light"))
        self.dark_theme_btn.clicked.connect(lambda: self.change_color_theme("dark"))

        theme_layout.addWidget(self.light_theme_btn)
        self.light_theme_btn.setFixedSize(225, 20)
        theme_layout.addWidget(self.dark_theme_btn)
        self.dark_theme_btn.setFixedSize(225, 20)
        theme_group.setLayout(theme_layout)

        main_layout.addWidget(theme_group)

        style_label = QLabel("Style themes")
        style_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPointSize(14)
        style_label.setFont(font)
        main_layout.addWidget(style_label)

        self.style_combo = QComboBox()
        self.style_combo.addItems(['Fusion', 'Windows'])
        self.style_combo.setCurrentText(self.current_style)
        self.style_combo.setFixedSize(250, 30)
        main_layout.addWidget(self.style_combo)

        self.apply_btn = QPushButton('Confirm Style')
        self.apply_btn.setFixedSize(250, 25)
        main_layout.addWidget(self.apply_btn)

        self.apply_btn.clicked.connect(self.change_style)

    def change_color_theme(self, theme):
        self.current_theme = theme
        self.settings.setValue("theme", theme)
        apply_app_theme(theme, self.style_combo.currentText())

    def change_style(self):
        style = self.style_combo.currentText()
        self.current_style = style
        self.settings.setValue("style", style)
        self.apply_theme_and_style(self.current_theme, style)

    def apply_theme_and_style(self, theme, style):
        apply_app_theme(theme, style)

    def open_main_window(self):
        from main_window import MainWindow
        self.main_window = MainWindow()
        self.main_window.showMaximized()
        self.close()

    def show_maximized(self):
        self.show()
        self.showMaximized()