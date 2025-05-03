from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame
from PyQt5.QtGui import QPainter, QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize

class frmArtistic(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1206, 790)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 5px solid #CECFC8; background-color: transparent; }")

        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1153, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        self.btnSave = QPushButton("Save", self)
        self.btnSave.setFixedSize(250, 60)
        self.btnSave.move(893, 697)
        self.btnSave.setObjectName("btnSave")

        self.load_stylesheet("RIASEC.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("ArtisticResult.png")  
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            x = (self.width() - scaled_pixmap.width()) // 2
            y = (self.height() - scaled_pixmap.height()) // 2
            painter.drawPixmap(x, y, scaled_pixmap)

        super().paintEvent(event)

    def load_stylesheet(self, file_path):
        try:
            with open(file_path, "r") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print(f"Stylesheet file '{file_path}' not found.")

if __name__ == "__main__":
    app = QApplication([])
    window = frmArtistic()
    window.show()
    app.exec_()




