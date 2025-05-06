from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame
from PyQt5.QtGui import QPainter, QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize

class frmCTE1(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("CTE1.png")  
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

class frmCTE2(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("CTE2.png")  
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

class frmCTE3(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("CTE3.png")  
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

class frmCTE4(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("CTE4.png")  
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

class frmCTE5(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("CTE5.png")  
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

class frmCHMT1(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("CHMT1.png")  
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

class frmCHMT2(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("CHMT2.png")  
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

class frmCAS1(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("CAS1.png")  
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

class frmCAS2(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("CAS2.png")  
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

class frmCCJE1(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("CCJE1.png")  
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

class frmCBAA1(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("CBAA1.png")  
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

class frmCBAA2(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("CBAA2.png")  
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

class frmCBAA3(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("CBAA3.png")  
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

class frmCOE1(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("COE1.png")  
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

class frmCOE2(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("COE2.png")  
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

class frmCOE3(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("COE3.png")  
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

class frmCCS1(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("CCS1.png")  
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

class frmCCS2(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("CCS2.png")  
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

class frmCIT1(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 840)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #CECFC8; background-color: transparent; }")
        
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1665, 11)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("AboutCourses.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("CIT1.png")  
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
    window = frmCTE1()
    window.show()
    app.exec_()

