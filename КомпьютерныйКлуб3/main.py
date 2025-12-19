# main.py
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSettings
from auth_window import Autorization
from computers_window import ComputersWindow
from main_window import MainWindow
from styles import apply_app_theme


def main():
    app = QApplication(sys.argv)

    settings = QSettings("ANK Software")
    saved_theme = settings.value("theme", "light")
    saved_style = settings.value("style", "Fusion")

    apply_app_theme(saved_theme, saved_style)

    window = Autorization()
    window.showMaximized()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()