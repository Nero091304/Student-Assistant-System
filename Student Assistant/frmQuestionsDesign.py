from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QLabel, QFileDialog
from PyQt5.QtGui import QPainter, QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize

class frmRealisticResult(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setFixedSize(1206, 790)  
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.username = username

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 5px solid #CECFC8; background-color: transparent; }")

        self.lblUsername = QLabel(f"{self.username}", self)
        self.lblUsername.setFixedSize(256, 59)
        self.lblUsername.move(208, 45)
        self.lblUsername.setObjectName("lblUsername")

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
        self.btnSave.clicked.connect(self.save_screenshot)

        self.load_stylesheet("RIASEC.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("RealisticResult.png")  
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

    def save_screenshot(self):
        self.btnSave.setVisible(False)
        self.btnClose.setVisible(False)
        screenshot = self.grab()
        default_filename = f"{self.username}_RealisticResult.png"
        self.btnSave.setVisible(True)
        self.btnClose.setVisible(True)

        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", default_filename, "PNG Files (*.png)")

        if file_path:
            success = screenshot.save(file_path, "PNG")
            if success:
                print(f"Screenshot saved to {file_path}")
            else:
                print("Failed to save the screenshot.")

class frmInvestigativeResult(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setFixedSize(1206, 790)  
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.username = username

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 5px solid #CECFC8; background-color: transparent; }")

        self.lblUsername = QLabel(f"{self.username}", self)
        self.lblUsername.setFixedSize(256, 59)
        self.lblUsername.move(208, 45)
        self.lblUsername.setObjectName("lblUsername")

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
        self.btnSave.clicked.connect(self.save_screenshot)

        self.load_stylesheet("RIASEC.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("InvestigativeResult.png")  
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

    def save_screenshot(self):
        self.btnSave.setVisible(False)
        self.btnClose.setVisible(False)
        screenshot = self.grab()
        default_filename = f"{self.username}_InvestigativeResult.png"
        self.btnSave.setVisible(True)
        self.btnClose.setVisible(True)

        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", default_filename, "PNG Files (*.png)")

        if file_path:
            success = screenshot.save(file_path, "PNG")
            if success:
                print(f"Screenshot saved to {file_path}")
            else:
                print("Failed to save the screenshot.")

class frmArtisticResult(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setFixedSize(1206, 790)  
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.username = username

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 5px solid #CECFC8; background-color: transparent; }")

        self.lblUsername = QLabel(f"{self.username}", self)
        self.lblUsername.setFixedSize(256, 59)
        self.lblUsername.move(208, 45)
        self.lblUsername.setObjectName("lblUsername")

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
        self.btnSave.clicked.connect(self.save_screenshot)

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

    def save_screenshot(self):
        self.btnSave.setVisible(False)
        self.btnClose.setVisible(False)
        screenshot = self.grab()
        default_filename = f"{self.username}_ArtisticResult.png"
        self.btnSave.setVisible(True)
        self.btnClose.setVisible(True)

        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", default_filename, "PNG Files (*.png)")

        if file_path:
            success = screenshot.save(file_path, "PNG")
            if success:
                print(f"Screenshot saved to {file_path}")
            else:
                print("Failed to save the screenshot.")

class frmSocialResult(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setFixedSize(1206, 790)  
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.username = username

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 5px solid #CECFC8; background-color: transparent; }")

        self.lblUsername = QLabel(f"{self.username}", self)
        self.lblUsername.setFixedSize(256, 59)
        self.lblUsername.move(208, 45)
        self.lblUsername.setObjectName("lblUsername")

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
        self.btnSave.clicked.connect(self.save_screenshot)

        self.load_stylesheet("RIASEC.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("SocialResult.png")  
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

    def save_screenshot(self):
        self.btnSave.setVisible(False)
        self.btnClose.setVisible(False)
        screenshot = self.grab()
        default_filename = f"{self.username}_SocialResult.png"
        self.btnSave.setVisible(True)
        self.btnClose.setVisible(True)

        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", default_filename, "PNG Files (*.png)")

        if file_path:
            success = screenshot.save(file_path, "PNG")
            if success:
                print(f"Screenshot saved to {file_path}")
            else:
                print("Failed to save the screenshot.")

class frmEnterprisingResult(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setFixedSize(1206, 790)  
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.username = username

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 5px solid #CECFC8; background-color: transparent; }")

        self.lblUsername = QLabel(f"{self.username}", self)
        self.lblUsername.setFixedSize(256, 59)
        self.lblUsername.move(208, 45)
        self.lblUsername.setObjectName("lblUsername")

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
        self.btnSave.clicked.connect(self.save_screenshot)

        self.load_stylesheet("RIASEC.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("EnterprisingResult.png")  
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

    def save_screenshot(self):
        self.btnSave.setVisible(False)
        self.btnClose.setVisible(False)
        screenshot = self.grab()
        default_filename = f"{self.username}_EnterprisingResult.png"
        self.btnSave.setVisible(True)
        self.btnClose.setVisible(True)

        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", default_filename, "PNG Files (*.png)")

        if file_path:
            success = screenshot.save(file_path, "PNG")
            if success:
                print(f"Screenshot saved to {file_path}")
            else:
                print("Failed to save the screenshot.")

class frmConventionalResult(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setFixedSize(1206, 790)  
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.username = username

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 5px solid #CECFC8; background-color: transparent; }")

        self.lblUsername = QLabel(f"{self.username}", self)
        self.lblUsername.setFixedSize(256, 59)
        self.lblUsername.move(208, 45)
        self.lblUsername.setObjectName("lblUsername")

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
        self.btnSave.clicked.connect(self.save_screenshot)

        self.load_stylesheet("RIASEC.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("ConventionalResult.png")  
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

    def save_screenshot(self):
        self.btnSave.setVisible(False)
        self.btnClose.setVisible(False)
        screenshot = self.grab()
        default_filename = f"{self.username}_ConventionalResult.png"
        self.btnSave.setVisible(True)
        self.btnClose.setVisible(True)

        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", default_filename, "PNG Files (*.png)")

        if file_path:
            success = screenshot.save(file_path, "PNG")
            if success:
                print(f"Screenshot saved to {file_path}")
            else:
                print("Failed to save the screenshot.")


if __name__ == "__main__":
    app = QApplication([])
    window = frmRealisticResult()
    window.show()
    app.exec_()



