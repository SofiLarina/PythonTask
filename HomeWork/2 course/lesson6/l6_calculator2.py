import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.setStyleSheet("background-color: purple;")

        self.text_edit = QLineEdit()
        self.text_edit.setStyleSheet("background-color: white; font-size: 24px;")
        self.text_edit.setReadOnly(True)

        self.buttons = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "/": (0, 3),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "*": (1, 3),
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            "-": (2, 3),
            "0": (3, 0),
            ".": (3, 1),
            "=": (3, 2),
            "+": (3, 3),
            "C": (4, 0),
            "Mem+": (4, 1),
            "Mem-": (4, 2),
            "Mem": (4, 3),
        }

        self.memory = 0

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)

        grid_layout = QGridLayout()
        for button_text, position in self.buttons.items():
            button = QPushButton(button_text)
            button.setStyleSheet("font-size: 18px;")
            button.clicked.connect(lambda _, txt=button_text: self.button_clicked(txt))
            grid_layout.addWidget(button, *position)

        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def button_clicked(self, text):
        if text == "=":
            try:
                result = eval(self.text_edit.text())
                self.text_edit.setText(str(result))
            except Exception as e:
                self.text_edit.setText("Ошибка")
        elif text == "C":
            self.text_edit.clear()
        elif text == "Mem+":
            self.memory += float(self.text_edit.text())
        elif text == "Mem-":
            self.memory -= float(self.text_edit.text())
        elif text == "Mem":
            self.text_edit.setText(str(self.memory))
        else:
            self.text_edit.insert(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())