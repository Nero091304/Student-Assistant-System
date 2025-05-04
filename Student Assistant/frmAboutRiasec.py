from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame
from PyQt5.QtGui import QPainter, QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
from frmAboutRiasecDesign import frmRealisticLearn
from frmAboutRiasecDesign import frmInvestigativeLearn
from frmAboutRiasecDesign import frmArtisticLearn
from frmAboutRiasecDesign import frmSocialLearn
from frmAboutRiasecDesign import frmEnterprisingLearn
from frmAboutRiasecDesign import frmConventionalLearn

class frmJHL(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1120, 649)
        self.setWindowFlags(Qt.FramelessWindowHint) 

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 4px solid #CECFC8; background-color: transparent; }")

        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1066, 13)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        self.load_stylesheet("RIASEC.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("JLH.png")
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
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

class frmAboutRiasec(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1920, 1020)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.btnBack = QPushButton("Back", self)
        self.btnBack.setFixedSize(199, 56)
        self.btnBack.move(1700, 20)
        self.btnBack.setObjectName("btnBack")
        self.btnBack.setIcon(QIcon("back.png"))
        self.btnBack.setIconSize(QSize(45, 45))
        self.btnBack.setLayoutDirection(Qt.RightToLeft)
        self.btnBack.clicked.connect(self.exit_app)

        self.btnAbout = QPushButton(self)
        self.btnAbout.setFixedSize(90, 90)
        self.btnAbout.move(42, 33)
        self.btnAbout.setObjectName("btnAbout")
        self.btnAbout.setIcon(QIcon("About.png"))
        self.btnAbout.setIconSize(QSize(82, 82))
        self.btnAbout.clicked.connect(self.show_jhl)

        self.btnClickHere1 = QPushButton("Learn More", self)
        self.btnClickHere1.setFixedSize(200, 50)
        self.btnClickHere1.move(299, 453)
        self.btnClickHere1.setObjectName("btnClickHere1")
        self.btnClickHere1.clicked.connect(self.Realistic_Result)

        self.btnClickHere2 = QPushButton("Learn More", self)
        self.btnClickHere2.setFixedSize(200, 50)
        self.btnClickHere2.move(863, 453)
        self.btnClickHere2.setObjectName("btnClickHere2")
        self.btnClickHere2.clicked.connect(self.Investigative_Result)

        self.btnClickHere3 = QPushButton("Learn More", self)
        self.btnClickHere3.setFixedSize(200, 50)
        self.btnClickHere3.move(1432, 453)
        self.btnClickHere3.setObjectName("btnClickHere3")     
        self.btnClickHere3.clicked.connect(self.Artistic_Result)

        self.btnClickHere4 = QPushButton("Learn More", self)
        self.btnClickHere4.setFixedSize(200, 50)
        self.btnClickHere4.move(299, 864)
        self.btnClickHere4.setObjectName("btnClickHere4")
        self.btnClickHere4.clicked.connect(self.Social_Result)

        self.btnClickHere5 = QPushButton("Learn More", self)
        self.btnClickHere5.setFixedSize(200, 50)
        self.btnClickHere5.move(863, 864)
        self.btnClickHere5.setObjectName("btnClickHere5")
        self.btnClickHere5.clicked.connect(self.Enterprising_Result)

        self.btnClickHere6 = QPushButton("Learn More", self)
        self.btnClickHere6.setFixedSize(200, 50)
        self.btnClickHere6.move(1432, 864)
        self.btnClickHere6.setObjectName("btnClickHere6")
        self.btnClickHere6.clicked.connect(self.Conventional_Result)

        self.load_stylesheet("AboutRiasec.qss")

        self.jhl_window = None  # Placeholder for the second window

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("RiasecModel.png")  
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

    def show_jhl(self):
        if self.jhl_window is None:
            self.jhl_window = frmJHL()
        self.jhl_window.show()

    def Realistic_Result(self):
        self.LSPU_form = frmRealisticLearn() 
        self.LSPU_form.show()

    def Investigative_Result(self):
        self.LSPU_form = frmInvestigativeLearn() 
        self.LSPU_form.show()

    def Artistic_Result(self):
        self.LSPU_form = frmArtisticLearn() 
        self.LSPU_form.show()

    def Social_Result(self):
        self.LSPU_form = frmSocialLearn() 
        self.LSPU_form.show()

    def Enterprising_Result(self):
        self.LSPU_form = frmEnterprisingLearn() 
        self.LSPU_form.show()

    def Conventional_Result(self):
        self.LSPU_form = frmConventionalLearn() 
        self.LSPU_form.show()

if __name__ == "__main__":
    app = QApplication([])
    window = frmAboutRiasec()
    window.show()
    app.exec_()
