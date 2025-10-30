import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QLineEdit, QLabel, QFileDialog, QGroupBox
)
from collections import Counter


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Текстовый редактор")
        self.resize(600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # --- Основная сетка: слева панель управления, справа текст ---
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # ==== Левая панель ====
        left_layout = QVBoxLayout()

        # Поле для имени файла
        self.file_name_edit = QLineEdit()
        self.file_name_edit.setPlaceholderText("Имя файла...")
        left_layout.addWidget(self.file_name_edit)

        # Кнопки
        self.new_btn = QPushButton("Создать новый")
        self.save_btn = QPushButton("Сохранить файл")
        self.open_btn = QPushButton("Открыть файл")

        left_layout.addWidget(self.new_btn)
        left_layout.addWidget(self.save_btn)
        left_layout.addWidget(self.open_btn)

        # Блок информации
        info_group = QGroupBox("Информация о тексте")
        info_layout = QVBoxLayout()

        self.char_label = QLabel("Символов: 0")
        self.word_label = QLabel("Слов: 0")
        self.longest_label = QLabel("Длинное слово: —")
        self.shortest_label = QLabel("Короткое слово: —")
        self.common_label = QLabel("Частое слово: —")

        for label in [
            self.char_label,
            self.word_label,
            self.longest_label,
            self.shortest_label,
            self.common_label
        ]:
            info_layout.addWidget(label)

        info_group.setLayout(info_layout)
        left_layout.addWidget(info_group)
        left_layout.addStretch()

        # ==== Правое поле ====
        self.text_edit = QTextEdit()

        # Добавляем всё в главный layout
        main_layout.addLayout(left_layout, 1)
        main_layout.addWidget(self.text_edit, 3)

        # === Сигналы ===
        self.new_btn.clicked.connect(self.new_file)
        self.save_btn.clicked.connect(self.save_file)
        self.open_btn.clicked.connect(self.open_file)
        self.text_edit.textChanged.connect(self.update_info)

        self.current_file = None

    # ==== Методы ====

    def new_file(self):
        self.text_edit.clear()
        self.file_name_edit.clear()
        self.current_file = None
        self.update_info()

    def save_file(self):
        text = self.text_edit.toPlainText()

        if not self.current_file:
            file_path, _ = QFileDialog.getSaveFileName(
                self, "Сохранить файл", "", "Текстовые файлы (*.txt);;Все файлы (*)"
            )
            if not file_path:
                return
            self.current_file = file_path
        else:
            file_path = self.current_file

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)

        self.file_name_edit.setText(os.path.basename(file_path))

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Открыть файл", "", "Текстовые файлы (*.txt);;Все файлы (*)"
        )
        if not file_path:
            return

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        self.text_edit.setText(content)
        self.file_name_edit.setText(os.path.basename(file_path))
        self.current_file = file_path
        self.update_info()

    def update_info(self):
        text = self.text_edit.toPlainText()
        words = text.split()
        chars = len(text)
        word_count = len(words)

        if words:
            longest = max(words, key=len)
            shortest = min(words, key=len)
            common = Counter(words).most_common(1)[0][0]
        else:
            longest = shortest = common = "—"

        self.char_label.setText(f"Символов: {chars}")
        self.word_label.setText(f"Слов: {word_count}")
        self.longest_label.setText(f"Длинное слово: {longest}")
        self.shortest_label.setText(f"Короткое слово: {shortest}")
        self.common_label.setText(f"Частое слово: {common}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec())



