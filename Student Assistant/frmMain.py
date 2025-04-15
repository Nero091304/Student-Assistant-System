import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QUrl

class frmMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Dashboard")
        self.resize(1920, 1020)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Video Widget
        self.videoWidget = QVideoWidget(self)
        self.videoWidget.setGeometry(1130, 450, 700, 500)  # adjust as needed

        # Media Player
        self.player = QMediaPlayer(self)
        self.player.setVideoOutput(self.videoWidget)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("LspuVideo.wmv")))
        self.player.setVolume(100)  
        self.player.play()         

        # Loop video when finished
        self.player.mediaStatusChanged.connect(self.handle_media_status)

        # Buttons setup
        self.btn1 = QPushButton("1", self)
        self.btn1.setFixedSize(150, 150)
        self.btn1.move(110, 160)

        self.btn2 = QPushButton("2", self)
        self.btn2.setFixedSize(150, 150)
        self.btn2.move(270, 160)

        self.btn3 = QPushButton("3", self)
        self.btn3.setFixedSize(150, 150)
        self.btn3.move(430, 160)

        self.btn4 = QPushButton("4", self)
        self.btn4.setFixedSize(150, 150)
        self.btn4.move(590, 160)

        self.btn5 = QPushButton("5", self)
        self.btn5.setFixedSize(150, 150)
        self.btn5.move(750, 160)

        self.btnTest = QPushButton("Test Now", self)
        self.btnTest.setFixedSize(350, 72)
        self.btnTest.move(180, 830)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("chess.png")
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            x = (self.width() - scaled_pixmap.width()) // 2
            y = (self.height() - scaled_pixmap.height()) // 2
            painter.drawPixmap(x, y, scaled_pixmap)

    def handle_media_status(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.player.setPosition(0)
            self.player.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = frmMain()
    window.show()
    sys.exit(app.exec_())
