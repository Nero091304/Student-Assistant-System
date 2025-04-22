import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt

class frmQuestions(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("1920x1020 Form")
        self.setFixedSize(1920, 1020) 
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.label = QLabel("Enter your name:")
        self.textbox = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = frmQuestions()
    form.show()
    sys.exit(app.exec_())

