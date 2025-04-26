import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize

class frmQuestions(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("1920x1020 Form")
        self.setFixedSize(1920, 1020)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.btnYes = QPushButton("Yes", self)
        self.btnYes.setFixedSize(300, 100)
        self.btnYes.move(651, 780)
        self.btnYes.setObjectName("btnYes")

        self.btnNo = QPushButton("No", self)
        self.btnNo.setFixedSize(300, 100)
        self.btnNo.move(981, 780)
        self.btnNo.setObjectName("btnNo")

        self.btnSubmit = QPushButton("Submit", self)
        self.btnSubmit.setFixedSize(300, 80)
        self.btnSubmit.move(1550, 885)
        self.btnSubmit.setObjectName("btnSubmit")

        self.btnBack = QPushButton("Back", self)
        self.btnBack.setFixedSize(199, 56)
        self.btnBack.move(1685, 40)
        self.btnBack.setObjectName("btnBack")
        self.btnBack.setIcon(QIcon("back.png"))
        self.btnBack.setIconSize(QSize(45, 45))
        self.btnBack.setLayoutDirection(Qt.RightToLeft)
        self.btnBack.clicked.connect(self.close)

        self.btnRight = QPushButton(self)
        self.btnRight.setFixedSize(70, 70)
        self.btnRight.move(1185, 125)
        self.btnRight.setObjectName("btnRight")
        self.btnRight.setIcon(QIcon("right.png"))
        self.btnRight.setIconSize(QSize(50, 50))

        self.btnLeft = QPushButton(self)
        self.btnLeft.setFixedSize(70, 70)
        self.btnLeft.move(670, 125)
        self.btnLeft.setObjectName("btnLeft")
        self.btnLeft.setIcon(QIcon("left.png"))
        self.btnLeft.setIconSize(QSize(50, 50))
       
        self.load_stylesheet("Questions.qss")

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("Q1.png")  
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            painter.drawPixmap(0, 0, scaled_pixmap)

    def load_stylesheet(self, file_path):
        try:
            with open(file_path, "r") as file:
                self.setStyleSheet(file.read())
        except Exception as e:
            print(f"Failed to load stylesheet: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = frmQuestions()
    form.show()
    sys.exit(app.exec_())
