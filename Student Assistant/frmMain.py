import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QPainter, QPixmap, QIcon
from PyQt5.QtCore import Qt, QUrl, QSize, pyqtSignal, pyqtSlot

class frmUpload(QWidget):
    picture_uploaded = pyqtSignal(QPixmap)  # Signal to send image back

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Upload Picture")
        self.resize(500, 527)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.current_pixmap = None

        # Picture display label
        self.picLabel = QLabel(self)
        self.picLabel.setFixedSize(200, 200)
        self.picLabel.move(155, 78)
        self.picLabel.setStyleSheet("background-color: #f0f0f0; border: 2px dashed #aaa;")
        self.picLabel.setScaledContents(True)

        # Upload button
        self.btnUpload = QPushButton("Upload Picture", self)
        self.btnUpload.setFixedSize(377, 56)
        self.btnUpload.move(65, 300)
        self.btnUpload.clicked.connect(self.upload_picture)
        self.btnUpload.setObjectName("btnUpload1")

        # Remove button
        self.btnRemove = QPushButton("Remove Picture", self)
        self.btnRemove.setFixedSize(377, 56)
        self.btnRemove.move(65, 370)
        self.btnRemove.clicked.connect(self.remove_picture)
        self.btnRemove.setObjectName("btnRemove")

        # Save button (now triggers signal)
        self.btnSave = QPushButton("Save", self)
        self.btnSave.setFixedSize(199, 56)
        self.btnSave.move(150, 450)
        self.btnSave.clicked.connect(self.save_picture)
        self.btnSave.setObjectName("btnSave")

        # Close button (top-right corner)
        self.btnClose = QPushButton("", self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(self.width() - 50, 5)  # Top-right corner
        self.btnClose.clicked.connect(self.close)
        self.btnClose.setObjectName("btnClose")  
        self.btnClose.setIcon(QIcon("Close.png"))
        self.btnClose.setIconSize(QSize(28, 28))

        self.load_stylesheet("Main.qss")

    def upload_picture(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Picture", "", "Image Files (*.png *.jpg *.jpeg *.bmp)", options=options)
        if file_path:
            self.current_pixmap = QPixmap(file_path)
            self.picLabel.setPixmap(self.current_pixmap)

    def remove_picture(self):
        self.picLabel.clear()
        self.picLabel.setStyleSheet("background-color: #f0f0f0; border: 2px dashed #aaa;")
        self.current_pixmap = None

    def save_picture(self):
        if self.current_pixmap:
            self.picture_uploaded.emit(self.current_pixmap)  # Emit signal with the image
            self.close()
        else:
            print("No picture to save.")

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("UploadBG.png")  # Adjust filename if needed
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            painter.drawPixmap(0, 0, scaled_pixmap)

    def load_stylesheet(self, file_path):
        try:
            with open(file_path, "r") as file:
                style = file.read()
                self.setStyleSheet(style)
        except Exception as e:
            print(f"Failed to load stylesheet: {e}")

# Original frmMain
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

        # Button to open upload form
        self.btnOpenUpload = QPushButton("", self)
        self.btnOpenUpload.setFixedSize(65, 65)
        self.btnOpenUpload.move(115, 45)
        self.btnOpenUpload.clicked.connect(self.open_upload_form)
        self.btnOpenUpload.setObjectName("btnUpload")

        self.btn1 = QPushButton("", self)
        self.btn1.setFixedSize(150, 150)
        self.btn1.move(110, 160)
        self.btn1.setIcon(QIcon("knight.png"))
        self.btn1.setIconSize(QSize(75, 75))
        self.btn1.setObjectName("btn1")  

        self.btn2 = QPushButton("", self)
        self.btn2.setFixedSize(150, 150)
        self.btn2.move(270, 160)
        self.btn2.setIcon(QIcon("compass.png"))
        self.btn2.setIconSize(QSize(80, 80))
        self.btn2.setObjectName("btn2")  

        self.btn3 = QPushButton("", self)
        self.btn3.setFixedSize(150, 150)
        self.btn3.move(430, 160)
        self.btn3.setIcon(QIcon("pin.png"))
        self.btn3.setIconSize(QSize(80, 80))
        self.btn3.setObjectName("btn3")  

        self.btn4 = QPushButton("", self)
        self.btn4.setFixedSize(150, 150)
        self.btn4.move(590, 160)
        self.btn4.setIcon(QIcon("brain.png"))
        self.btn4.setIconSize(QSize(90, 90))
        self.btn4.setObjectName("btn4")  

        self.btn5 = QPushButton("", self)
        self.btn5.setFixedSize(150, 150)
        self.btn5.move(750, 160)
        self.btn5.setIcon(QIcon("trends.png"))
        self.btn5.setIconSize(QSize(75, 75))
        self.btn5.setObjectName("btn5")  

        self.btnTest = QPushButton("Test Now", self)
        self.btnTest.setFixedSize(350, 72)
        self.btnTest.move(150, 830)
        self.btnTest.setObjectName("btnTest")  

        self.btnTest = QPushButton("Test Now", self)
        self.btnTest.setFixedSize(350, 72)
        self.btnTest.move(150, 830)
        self.btnTest.setObjectName("btnTest") 

        self.load_stylesheet("Main.qss")

    def load_stylesheet(self, file_path):
        try:
            with open(file_path, "r") as file:
                style = file.read()
                self.setStyleSheet(style)
        except Exception as e:
            print(f"Failed to load stylesheet: {e}")

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

    def open_upload_form(self):
        self.upload_window = frmUpload()
        self.upload_window.picture_uploaded.connect(self.set_upload_button_image)
        self.upload_window.show()

    @pyqtSlot(QPixmap)
    def set_upload_button_image(self, pixmap):
    # Scale the image to fit the button size exactly
        scaled_pixmap = pixmap.scaled(
        self.btnOpenUpload.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
    )
        self.btnOpenUpload.setIcon(QIcon(scaled_pixmap))
        self.btnOpenUpload.setIconSize(self.btnOpenUpload.size())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = frmMain()
    window.show()
    sys.exit(app.exec_())
