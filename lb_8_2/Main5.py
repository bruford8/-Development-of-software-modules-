import sys
import csv
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QTableWidget, QTableWidgetItem,
    QFileDialog, QComboBox, QLabel, QHBoxLayout
)
from PyQt6.QtGui import QColor


class OlympiadResults(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Результаты олимпиады")
        self.resize(700, 500)

        self.data = []
        self.schools = set()
        self.classes = set()

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()
        central.setLayout(layout)

        # --- Панель фильтров ---
        filter_layout = QHBoxLayout()

        self.school_label = QLabel("Школа:")
        self.school_combo = QComboBox()
        self.school_combo.addItem("Все")

        self.class_label = QLabel("Класс:")
        self.class_combo = QComboBox()
        self.class_combo.addItem("Все")

        self.filter_button = QPushButton("Применить фильтр")
        self.load_button = QPushButton("Загрузить CSV")

        filter_layout.addWidget(self.school_label)
        filter_layout.addWidget(self.school_combo)
        filter_layout.addWidget(self.class_label)
        filter_layout.addWidget(self.class_combo)
        filter_layout.addWidget(self.filter_button)
        filter_layout.addWidget(self.load_button)
        layout.addLayout(filter_layout)

        # --- Таблица ---
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Логин", "ФИО", "Баллы"])
        layout.addWidget(self.table)

        # --- Сигналы ---
        self.load_button.clicked.connect(self.load_csv)
        self.filter_button.clicked.connect(self.apply_filter)

    # ====== Загрузка данных ======
    def load_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Открыть CSV файл", "", "CSV файлы (*.csv);;Все файлы (*)"
        )
        if not file_path:
            return

        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            self.data = []
            self.schools.clear()
            self.classes.clear()

            for row in reader:
                login = row["login"]
                name = row["user_name"]
                score = row["Score"]

                # Парсим логин: sh-kaluga16-SS-CC-N
                parts = login.split("-")
                if len(parts) >= 5:
                    school = parts[2]
                    cls = parts[3]
                    self.schools.add(school)
                    self.classes.add(cls)
                else:
                    school = cls = "?"

                self.data.append({
                    "login": login,
                    "name": name,
                    "score": int(score),
                    "school": school,
                    "class": cls
                })

        # Обновляем списки фильтров
        self.school_combo.clear()
        self.school_combo.addItem("Все")
        self.school_combo.addItems(sorted(self.schools))

        self.class_combo.clear()
        self.class_combo.addItem("Все")
        self.class_combo.addItems(sorted(self.classes))

        # Отобразим таблицу
        self.show_table(self.data)

    # ====== Применение фильтра ======
    def apply_filter(self):
        if not self.data:
            return

        school_filter = self.school_combo.currentText()
        class_filter = self.class_combo.currentText()

        filtered = []
        for d in self.data:
            if (school_filter == "Все" or d["school"] == school_filter) and \
               (class_filter == "Все" or d["class"] == class_filter):
                filtered.append(d)

        # Сортируем по баллам (по убыванию)
        filtered.sort(key=lambda x: x["score"], reverse=True)

        # Определяем места
        places = self.calculate_places(filtered)

        # Отображаем
        self.show_table(filtered, places)

    # ====== Подсчёт мест ======
    def calculate_places(self, data):
        places = {}
        if not data:
            return places

        place = 1
        prev_score = None
        for idx, entry in enumerate(data):
            score = entry["score"]
            if score != prev_score:
                place = idx + 1
            places[entry["login"]] = place
            prev_score = score
        return places

    # ====== Отображение таблицы ======
    def show_table(self, dataset, places=None):
        self.table.setRowCount(len(dataset))

        for i, row in enumerate(dataset):
            login_item = QTableWidgetItem(row["login"])
            name_item = QTableWidgetItem(row["name"])
            score_item = QTableWidgetItem(str(row["score"]))

            self.table.setItem(i, 0, login_item)
            self.table.setItem(i, 1, name_item)
            self.table.setItem(i, 2, score_item)

            if places:
                place = places.get(row["login"], 0)
                color = None
                if place == 1:
                    color = QColor(255, 223, 0)  # золото
                elif place == 2:
                    color = QColor(192, 192, 192)  # серебро
                elif place == 3:
                    color = QColor(205, 127, 50)  # бронза

                if color:
                    for j in range(3):
                        self.table.item(i, j).setBackground(color)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OlympiadResults()
    window.show()
    sys.exit(app.exec())
