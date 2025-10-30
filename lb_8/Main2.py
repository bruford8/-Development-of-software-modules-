import sys
from PyQt6.QtGui import QPixmap, QTransform, QColor, QPainter
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Редактор фотографий")
        self.resize(800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(100)
        self.slider.setTickInterval(1)
        self.slider.valueChanged.connect(self.on_slider_change)
        main_layout.addWidget(self.slider)

        right_layout = QVBoxLayout()
        right_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel()
        self.pixmap = QPixmap("кот.jpg")
        self.original_pixmap = self.pixmap.copy()

        self.label.setPixmap(self.pixmap)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(1.0)
        self.label.setGraphicsEffect(self.opacity_effect)

        right_layout.addWidget(self.label)

        buttons_layout = QHBoxLayout()

        self.counterclockwise = QPushButton("Повернуть против часовой")
        self.counterclockwise.clicked.connect(self.rotate_counterclockwise)
        buttons_layout.addWidget(self.counterclockwise)

        self.clockwise = QPushButton("Повернуть по часовой")
        self.clockwise.clicked.connect(self.rotate_clockwise)
        buttons_layout.addWidget(self.clockwise)

        right_layout.addLayout(buttons_layout)

        filters_layout = QHBoxLayout()

        self.red_btn = QPushButton("R")
        self.red_btn.clicked.connect(lambda: self.tint_image(QColor(255, 0, 0, 120)))
        filters_layout.addWidget(self.red_btn)

        self.green_btn = QPushButton("G")
        self.green_btn.clicked.connect(lambda: self.tint_image(QColor(0, 255, 0, 120)))
        filters_layout.addWidget(self.green_btn)

        self.blue_btn = QPushButton("B")
        self.blue_btn.clicked.connect(lambda: self.tint_image(QColor(0, 0, 255, 120)))
        filters_layout.addWidget(self.blue_btn)

        self.all_btn = QPushButton("RGB")
        self.all_btn.clicked.connect(lambda: self.tint_image(QColor(255, 255, 255, 120)))
        filters_layout.addWidget(self.all_btn)

        self.clear_btn = QPushButton("Clear")
        self.clear_btn.clicked.connect(lambda: self.tint_image(QColor(0, 0, 0, 0)))
        filters_layout.addWidget(self.clear_btn)

        right_layout.addLayout(filters_layout)

        main_layout.addLayout(right_layout)

    def tint_image(self, color: QColor):
        if self.original_pixmap.isNull():
            return

        tinted = QPixmap(self.original_pixmap.size())
        tinted.fill(Qt.GlobalColor.transparent)

        painter = QPainter(tinted)
        painter.drawPixmap(0, 0, self.original_pixmap)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceAtop)
        painter.fillRect(self.original_pixmap.rect(), color)
        painter.end()

        self.label.setPixmap(tinted)
        self.pixmap = tinted.copy()

    def rotate_clockwise(self):
        transform = QTransform().rotate(90)
        self.pixmap = self.pixmap.transformed(transform)
        self.label.setPixmap(self.pixmap)

    def rotate_counterclockwise(self):
        transform = QTransform().rotate(-90)
        self.pixmap = self.pixmap.transformed(transform)
        self.label.setPixmap(self.pixmap)

    def on_slider_change(self, value):
        opacity = value / 100
        self.opacity_effect.setOpacity(opacity)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
