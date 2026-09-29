from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget,
    QLineEdit, QComboBox, QListWidgetItem, QLabel, QHBoxLayout
)
from PySide6.QtCore import QTimer, QTime, Qt
import sys

STATUS_COLORS = {               #SŁOWNIK
    "Do zrobienia": "red",
    "W trakcie": "orange",
    "Zrobione": "green"
}


class TaskManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Planowanie zadań")
        self.setGeometry(100, 100, 400, 500)

        self.layout = QVBoxLayout()

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Wprowadź zadanie...")
        self.layout.addWidget(self.task_input)

        self.add_button = QPushButton("Dodaj zadanie")
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        self.remove_button = QPushButton("Usuń zadanie")
        self.remove_button.clicked.connect(self.remove_task)
        self.layout.addWidget(self.remove_button)

        self.quit_button = QPushButton("Wyjście")
        self.quit_button.clicked.connect(self.close)
        self.layout.addWidget(self.quit_button)

        self.setLayout(self.layout)

    def add_task(self):
        task_name = self.task_input.text()
        if task_name:
            item = QListWidgetItem()
            widget = TaskWidget(task_name)
            item.setSizeHint(widget.sizeHint())
            self.task_list.addItem(item)
            self.task_list.setItemWidget(item, widget)
            self.task_input.clear()

    def remove_task(self):
        for item in self.task_list.selectedItems():
            row = self.task_list.row(item)
            self.task_list.takeItem(row)


class TaskWidget(QWidget):
    def __init__(self, task_name):
        super().__init__()
        self.layout = QHBoxLayout()

        self.label = QLabel(task_name)
        self.layout.addWidget(self.label)

        self.status_dropdown = QComboBox()
        self.status_dropdown.addItems(["Do zrobienia", "W trakcie", "Zrobione"])
        self.status_dropdown.currentTextChanged.connect(self.update_status)
        self.layout.addWidget(self.status_dropdown)

        self.timer_label = QLabel("00:00:00")
        self.layout.addWidget(self.timer_label)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.elapsed_time = QTime(0, 0, 0)

        self.setLayout(self.layout)
        self.update_status("Do zrobienia")

    def update_status(self, status):
        self.setStyleSheet(f"background-color: {STATUS_COLORS[status]};")

        if status == "Do zrobienia":            #kolory listy rozwijanej, CSS
            self.setStyleSheet("background-color: red; color: white; margin-left: 1%;")
        elif status == "W trakcie":
            self.setStyleSheet("background-color: orange; color: black; margin-left: 1%;")
        elif status == "Zrobione":
            self.setStyleSheet("background-color: green; color: white; margin-left: 1%;")

        if status == "W trakcie":
            self.timer.start(1000)
        elif status == "Zrobione":
            self.timer.stop()
        else:
            self.timer.stop()
            self.timer_label.setText("00:00:00")
            self.elapsed_time = QTime(0, 0, 0)

    def update_timer(self):
        self.elapsed_time = self.elapsed_time.addSecs(1)
        self.timer_label.setText(self.elapsed_time.toString("hh:mm:ss"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskManager()
    window.show()
    sys.exit(app.exec())
