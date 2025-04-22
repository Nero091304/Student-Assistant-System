from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QScrollArea, QFrame
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys

class frmMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web-style Scrollable Form")
        self.resize(1920, 1020)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # === Scrollable layout like a webpage ===
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setGeometry(0, 0, 1920, 1020)

        scroll_content = QWidget()
        scroll_area.setWidget(scroll_content)

        layout = QVBoxLayout(scroll_content)
        layout.setSpacing(40)

        # === Title like a webpage header ===
        header = QLabel("?? Student Assistant System", self)
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 40px; font-weight: bold; margin: 40px;")
        layout.addWidget(header)

        # === Video player like a banner/video embed ===
        self.videoWidget = QVideoWidget()
        self.videoWidget.setFixedSize(1280, 720)
        layout.addWidget(self.videoWidget, alignment=Qt.AlignCenter)

        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.videoWidget)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("LspuVideo.wmv")))
        self.player.setVolume(100)
        self.player.play()
        self.player.mediaStatusChanged.connect(self.handle_media_status)

        # === Profile Upload Button (styled like a profile icon) ===
        btnUpload = QPushButton()
        btnUpload.setFixedSize(80, 80)
        btnUpload.setIcon(QIcon(QPixmap("user.png").scaled(75, 75, Qt.KeepAspectRatio, Qt.SmoothTransformation)))
        btnUpload.setIconSize(QSize(75, 75))
        btnUpload.setStyleSheet("border: none; margin: 20px;")
        layout.addWidget(btnUpload, alignment=Qt.AlignCenter)

        # === Add Chess Option Buttons ===
        chess_icons = ["knight.png", "bishop.png", "rook.png", "queen.png", "king.png"]
        for i, icon in enumerate(chess_icons, 1):
            btn = QPushButton(f"Option {i}")
            btn.setFixedSize(200, 200)
            btn.setIcon(QIcon(icon))
            btn.setIconSize(QSize(120, 120))
            btn.setStyleSheet("""
                QPushButton {
                    border: 2px solid #ccc;
                    border-radius: 20px;
                    background-color: white;
                }
                QPushButton:hover {
                    background-color: #f0f0f0;
                }
            """)
            layout.addWidget(btn, alignment=Qt.AlignCenter)

        # === Spacer at the bottom ===
        spacer = QFrame()
        spacer.setFixedHeight(200)
        layout.addWidget(spacer)

    def handle_media_status(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.player.setPosition(0)
            self.player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = frmMain()
    window.show()
    sys.exit(app.exec_())
