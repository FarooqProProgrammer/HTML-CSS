import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QFileDialog


class ReadGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Read Generator")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel("Enter text:", self)
        self.label.setGeometry(50, 50, 100, 30)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(50, 80, 300, 150)

        self.generate_button = QPushButton("Generate", self)
        self.generate_button.setGeometry(150, 250, 100, 30)
        self.generate_button.clicked.connect(self.generate_text)

    def generate_text(self):
        input_text = self.text_edit.toPlainText()
        formatted_text = input_text.upper()  # Modify the text generation logic as per your requirements

        file_path, _ = QFileDialog.getSaveFileName(self, "Save Readme File", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, "w") as file:
                file.write(formatted_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    read_generator = ReadGenerator()
    read_generator.show()
    sys.exit(app.exec_())
