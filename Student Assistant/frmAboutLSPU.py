from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QPainter, QPixmap, QIcon, QPalette, QColor
from PyQt5.QtCore import Qt, QSize

class frmAboutLSPU(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1920, 1020)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.background_image = "LspuHome.png"

        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1871, 6)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        self.btnHome = QPushButton("Home", self)
        self.btnHome.setFixedSize(70, 37)
        self.btnHome.move(1103, 45)
        self.btnHome.setObjectName("btnTaskBar")
        self.btnHome.clicked.connect(self.set_Home_background)

        self.btnAbout = QPushButton("About",self)
        self.btnAbout.setFixedSize(90, 37)
        self.btnAbout.move(1205, 45)
        self.btnAbout.setObjectName("btnTaskBar")
        self.btnAbout.clicked.connect(self.set_About_background)

        self.btnCampuses = QPushButton("Campuses",self)
        self.btnCampuses.setFixedSize(130, 37)
        self.btnCampuses.move(1322, 45)
        self.btnCampuses.setObjectName("btnTaskBar")
        self.btnCampuses.clicked.connect(self.set_Campuses_background)

        self.btnAdministration = QPushButton("Administration",self)
        self.btnAdministration.setFixedSize(200, 37)
        self.btnAdministration.move(1474, 45)
        self.btnAdministration.setObjectName("btnTaskBar")
        self.btnAdministration.clicked.connect(self.set_Administration_background)

        self.btnContacts = QPushButton("Contacts",self)
        self.btnContacts.setFixedSize(140, 37)
        self.btnContacts.move(1677, 45)
        self.btnContacts.setObjectName("btnTaskBar")
        self.btnContacts.clicked.connect(self.set_Contacts_background)

        #HOME BUTTON====================================================================
        self.btnLearnMore = QPushButton("Learn More",self)
        self.btnLearnMore.setFixedSize(233, 61)
        self.btnLearnMore.move(106, 676)
        self.btnLearnMore.setObjectName("btnLearnMore")
        self.btnLearnMore.clicked.connect(self.LearnMore)

        #ABOUT BUTTON====================================================================
        self.btnLearnMore1 = QPushButton("Learn More",self)
        self.btnLearnMore1.setFixedSize(233, 61)
        self.btnLearnMore1.move(215, 492)
        self.btnLearnMore1.setObjectName("btnLearnMore")
        self.btnLearnMore1.clicked.connect(self.LearnMore1)

        self.btnUp = QPushButton(self)
        self.btnUp.setFixedSize(70, 70)
        self.btnUp.move(68, 421)
        self.btnUp.setIcon(QIcon("Up.png"))  
        self.btnUp.setIconSize(QSize(50, 50))
        self.btnUp.setObjectName("btnUpDown")

        self.btnDown = QPushButton(self)
        self.btnDown.setFixedSize(70, 70)
        self.btnDown.move(68, 520)
        self.btnDown.setIcon(QIcon("Down.png"))  
        self.btnDown.setIconSize(QSize(50, 50))
        self.btnDown.setObjectName("btnUpDown")

        self.btnLearnMore1.hide()
        self.btnUp.hide()
        self.btnDown.hide()

         #CONTACTS BUTTON====================================================================
        self.btnSubmit = QPushButton("Submit", self)
        self.btnSubmit.setFixedSize(199, 56)
        self.btnSubmit.move(1580, 230)
        self.btnSubmit.setObjectName("btnSubmit")

        self.txtName = QLineEdit(self)
        self.txtName.setFixedSize(576, 70)
        self.txtName.move(1137, 436)
        self.txtName.setObjectName("txtContacts")
        self.txtName.setPlaceholderText("Type Your Full Name")

        self.txtNumber = QLineEdit(self)
        self.txtNumber.setFixedSize(576, 70)
        self.txtNumber.move(1137, 563)
        self.txtNumber.setObjectName("txtContacts")
        self.txtNumber.setPlaceholderText("Type Your Contact Number")

        self.txtMessage = QLineEdit(self)
        self.txtMessage.setFixedSize(576, 167)
        self.txtMessage.move(1137, 692)
        self.txtMessage.setObjectName("txtContacts")
        self.txtMessage.setPlaceholderText("Type Your Message")

        self.btnSubmit.hide()
        self.txtName.hide()
        self.txtNumber.hide()
        self.txtMessage.hide()

        palette = self.txtName.palette()
        palette.setColor(QPalette.PlaceholderText, QColor(255, 255, 255, 77))  
        self.txtName.setPalette(palette)
        self.txtNumber.setPalette(palette)
        self.txtMessage.setPalette(palette)
      
        self.btnHome.setStyleSheet("color: #01F5FE;")
        self.load_stylesheet("AboutLspu.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(self.background_image) 
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

    def set_Home_background(self):
        self.set_background_image("LspuHome.png")
        self.btnLearnMore.show()
        self.btnLearnMore1.hide()
        self.btnUp.hide()
        self.btnDown.hide()
        self.btnSubmit.hide()
        self.txtName.hide()
        self.txtNumber.hide()
        self.txtMessage.hide()
        self.reset_btnAbout()
        self.reset_btnCampuses()
        self.reset_btnAdministration()
        self.reset_btnContacts()
        self.btnHome.setStyleSheet("color: #01F5FE;")

    def set_About_background(self):
        self.background_image = "LspuAbout.png"
        self.btnLearnMore1.show()
        self.btnLearnMore.hide()
        self.btnUp.show()
        self.btnDown.show()
        self.btnSubmit.hide()
        self.txtName.hide()
        self.txtNumber.hide()
        self.txtMessage.hide()
        self.reset_btnHome()
        self.reset_btnCampuses()
        self.reset_btnAdministration()
        self.reset_btnContacts()
        self.btnAbout.setStyleSheet("color: #01F5FE;")
        self.update()

    def set_Campuses_background(self):
        self.background_image = "LspuCampuses.png"
        self.btnLearnMore.hide()
        self.btnLearnMore1.hide()
        self.btnUp.hide()
        self.btnDown.hide()
        self.btnSubmit.hide()
        self.txtName.hide()
        self.txtNumber.hide()
        self.txtMessage.hide()
        self.reset_btnHome()
        self.reset_btnAbout()
        self.reset_btnAdministration()
        self.reset_btnContacts()
        self.btnCampuses.setStyleSheet("color: #01F5FE;")
        self.update()

    def set_Administration_background(self):
        self.background_image = "LspuAdministration.png"
        self.btnLearnMore.hide()
        self.btnLearnMore1.hide()
        self.btnUp.hide()
        self.btnDown.hide()
        self.btnSubmit.hide()
        self.txtName.hide()
        self.txtNumber.hide()
        self.txtMessage.hide()
        self.reset_btnHome()
        self.reset_btnAbout()
        self.reset_btnCampuses()
        self.reset_btnContacts()
        self.btnAdministration.setStyleSheet("color: #01F5FE;")
        self.update()

    def set_Contacts_background(self):
        self.background_image = "LspuContacts.png"
        self.btnLearnMore.hide()
        self.btnLearnMore1.hide()
        self.btnUp.hide()
        self.btnDown.hide()
        self.btnSubmit.show()
        self.txtName.show()
        self.txtNumber.show()
        self.txtMessage.show()
        self.reset_btnHome()
        self.reset_btnAbout()
        self.reset_btnCampuses()
        self.reset_btnAdministration()
        self.btnContacts.setStyleSheet("color: #01F5FE;")
        self.update()

    def LearnMore(self):
        self.background_image = "LspuAbout.png"
        self.btnLearnMore1.show()
        self.btnLearnMore.hide()
        self.btnUp.show()
        self.btnDown.show()
        self.reset_btnHome()
        self.reset_btnCampuses()
        self.reset_btnAdministration()
        self.reset_btnContacts()
        self.btnAbout.setStyleSheet("color: #01F5FE;")
        self.update()

    def LearnMore1(self):
        self.background_image = "LspuCampuses.png"
        self.btnLearnMore.hide()
        self.btnLearnMore1.hide()
        self.btnUp.hide()
        self.btnDown.hide()
        self.reset_btnHome()
        self.reset_btnAbout()
        self.reset_btnAdministration()
        self.reset_btnContacts()
        self.btnCampuses.setStyleSheet("color: #01F5FE;")
        self.update()

    def set_background_image(self, image_path):
        self.background_image = image_path
        self.update() 

    def reset_btnHome(self):
        self.btnHome_clicked = False
        self.btnHome.setStyleSheet("background-color: none;")

    def reset_btnAbout(self):
        self.btnAbout_clicked = False
        self.btnAbout.setStyleSheet("background-color: none;")

    def reset_btnCampuses(self):
        self.btnCampuses_clicked = False
        self.btnCampuses.setStyleSheet("background-color: none;")

    def reset_btnAdministration(self):
        self.btnAdministration_clicked = False
        self.btnAdministration.setStyleSheet("background-color: none;")

    def reset_btnContacts(self):
        self.btnContacts_clicked = False
        self.btnContacts.setStyleSheet("background-color: none;")

if __name__ == "__main__":
    app = QApplication([])
    window = frmAboutLSPU()
    window.show()
    app.exec_()
