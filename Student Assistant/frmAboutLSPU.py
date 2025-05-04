from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMessageBox, QComboBox, QTextEdit
from PyQt5.QtGui import QPainter, QPixmap, QIcon, QPalette, QColor
from PyQt5.QtCore import Qt, QSize, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class frmAboutLSPU(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1920, 1020)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.background_image = "LspuHome.png"

        self.about_pages = ["LspuAbout.png", "LspuAbout1.png", "LspuAbout2.png", "LspuAbout3.png"]
        self.current_about_index = 0

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
        self.btnUp.clicked.connect(self.go_up_about_page)

        self.btnDown = QPushButton(self)
        self.btnDown.setFixedSize(70, 70)
        self.btnDown.move(68, 520)
        self.btnDown.setIcon(QIcon("Down.png"))  
        self.btnDown.setIconSize(QSize(50, 50))
        self.btnDown.setObjectName("btnUpDown")
        self.btnDown.clicked.connect(self.go_down_about_page)

        self.btnPlay = QPushButton("Play Audio", self)
        self.btnPlay.setFixedSize(233, 61)
        self.btnPlay.move(1014, 694)
        self.btnPlay.setObjectName("btnLearnMore")
        self.btnPlay.clicked.connect(self.play_audio)

        self.btnStop = QPushButton("Stop Audio", self)
        self.btnStop.setFixedSize(233, 61)
        self.btnStop.move(1014, 694)
        self.btnStop.setObjectName("btnLearnMore")
        self.btnStop.clicked.connect(self.stop_audio)

        self.media_player = QMediaPlayer() 

        self.btnLearnMore1.hide()
        self.btnUp.hide()
        self.btnDown.hide()
        self.btnPlay.hide()
        self.btnStop.hide()

        #ADMINISTRATION BUTTON====================================================================

        self.cbAdmin = QComboBox(self)
        self.cbAdmin.addItems(["University-Wide Leadership", "Library Services", "Campus Directors", "Office of Student Affairs and Services (OSAS)", "National Service Training Program (NSTP)"])
        self.cbAdmin.setFixedSize(490, 70)
        self.cbAdmin.move(220, 757)
        self.cbAdmin.setObjectName("cbAdmin")
        self.cbAdmin.currentTextChanged.connect(self.admin_selection_changed)
        self.cbAdmin.hide()

        #CONTACTS BUTTON====================================================================
        self.btnSubmit = QPushButton("Submit", self)
        self.btnSubmit.setFixedSize(199, 56)
        self.btnSubmit.move(1580, 230)
        self.btnSubmit.setObjectName("btnSubmit")
        self.btnSubmit.clicked.connect(self.submit_form)

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

        self.txtMessage = QTextEdit(self)
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

    def go_down_about_page(self):
        if self.current_about_index < len(self.about_pages) - 1:
            self.current_about_index += 1
            self.background_image = self.about_pages[self.current_about_index]
            self.btnLearnMore1.setVisible(self.current_about_index == 0)
            self.update_btnPlay_visibility() 
            self.update()

    def go_up_about_page(self):
        if self.current_about_index > 0:
            self.current_about_index -= 1
            self.background_image = self.about_pages[self.current_about_index]
            self.btnLearnMore1.setVisible(self.current_about_index == 0)
            self.update_btnPlay_visibility()
            self.update()

    def play_audio(self):
        audio_file = QUrl.fromLocalFile("LspuHymn.mp3")
        content = QMediaContent(audio_file)
        self.media_player.setMedia(content)
        self.media_player.setVolume(80)
        self.media_player.play()
    
        self.btnPlay.hide()
        self.btnStop.show()

    def stop_audio(self):
        self.media_player.stop()
        self.btnStop.hide()
        self.btnPlay.show()

    def update_btnPlay_visibility(self):
        self.btnPlay.setVisible(self.background_image == "LspuAbout2.png")

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
        self.cbAdmin.hide()
        self.reset_btnAbout()
        self.reset_btnCampuses()
        self.reset_btnAdministration()
        self.reset_btnContacts()
        self.btnHome.setStyleSheet("color: #01F5FE;")

    def set_About_background(self):
        self.current_about_index = 0 
        self.background_image = "LspuAbout.png"
        self.btnLearnMore1.show()
        self.btnLearnMore.hide()
        self.btnUp.show()
        self.btnDown.show()
        self.btnSubmit.hide()
        self.txtName.hide()
        self.txtNumber.hide()
        self.txtMessage.hide()
        self.cbAdmin.hide()
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
        self.btnPlay.hide()
        self.txtName.hide()
        self.txtNumber.hide()
        self.txtMessage.hide()
        self.cbAdmin.hide()
        self.reset_btnHome()
        self.reset_btnAbout()
        self.reset_btnAdministration()
        self.reset_btnContacts()
        self.btnCampuses.setStyleSheet("color: #01F5FE;")
        self.update()

    def set_Administration_background(self):
        self.cbAdmin.setCurrentIndex(0)
        self.background_image = "LspuAdministration.png"
        self.btnLearnMore.hide()
        self.btnLearnMore1.hide()
        self.btnUp.hide()
        self.btnDown.hide()
        self.btnSubmit.hide()
        self.btnPlay.hide()
        self.txtName.hide()
        self.txtNumber.hide()
        self.txtMessage.hide()
        self.cbAdmin.show()
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
        self.btnPlay.hide()
        self.txtName.show()
        self.txtNumber.show()
        self.txtMessage.show()
        self.txtName.setFocus()
        self.cbAdmin.hide()
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
        self.update_btnPlay_visibility()
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
        self.update_btnPlay_visibility()
        self.update()

    def set_background_image(self, image_path):
        self.background_image = image_path
        self.update_btnPlay_visibility()
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

    def admin_selection_changed(self, text):
        if text == "Library Services":
            self.set_background_image("LspuAdministration1.png")
        elif text == "Campus Directors":
            self.set_background_image("LspuAdministration2.png")
        elif text == "Office of Student Affairs and Services (OSAS)":
            self.set_background_image("LspuAdministration3.png")
        elif text == "National Service Training Program (NSTP)":
            self.set_background_image("LspuAdministration4.png")
        else:
            self.set_background_image("LspuAdministration.png")

    def submit_form(self):
        name = self.txtName.text().strip()
        number = self.txtNumber.text().strip()
        message = self.txtMessage.toPlainText().strip()

        if name and number and message:
            try:
                import mysql.connector  
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",             
                    password="",             
                    database="smsdb"  
                )
                cursor = connection.cursor()

                query = "INSERT INTO tblinquiries (Name, Number, Message) VALUES (%s, %s, %s)"
                values = (name, number, message)

                cursor.execute(query, values)
                connection.commit()

                cursor.close()
                connection.close()

                QMessageBox.information(self, "Message Sent", "Your message has been successfully sent!")
                self.txtName.clear()
                self.txtNumber.clear()
                self.txtMessage.clear()
                self.txtName.setFocus()

            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Database Error", f"An error occurred:\n{err}")
        else:
            QMessageBox.warning(self, "Incomplete Form", "Please fill out all fields before submitting.")
        self.txtName.setFocus()

if __name__ == "__main__":
    app = QApplication([])
    window = frmAboutLSPU()
    window.show()
    app.exec_()
