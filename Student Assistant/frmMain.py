import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QMessageBox, QFrame
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QPainter, QPixmap, QIcon
from PyQt5.QtCore import Qt, QUrl, QSize, pyqtSignal, pyqtSlot
from frmQuestions import frmQuestions  
from frmAboutLSPU import frmAboutLSPU
from frmAboutCourses import frmAboutCourses
from frmAboutRiasec import frmAboutRiasec

class frmAboutSAS(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 4px solid #CECFC8; background-color: transparent; }")

        self.btnback = QPushButton("Back", self)
        self.btnback.setFixedSize(140, 40)
        self.btnback.move(self.width() - 150, 10)
        self.btnback.setObjectName("btnback")
        self.btnback.setIcon(QIcon("back.png"))
        self.btnback.setIconSize(QSize(40, 40))
        self.btnback.setLayoutDirection(Qt.RightToLeft)
        self.btnback.clicked.connect(self.close)

        self.load_stylesheet("Main.qss")

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("AboutUs.png")  
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            painter.drawPixmap(0, 0, scaled_pixmap)

    def load_stylesheet(self, file_path):
        try:
            with open(file_path, "r") as file:
                self.setStyleSheet(file.read())
        except Exception as e:
            print(f"Failed to load stylesheet: {e}")

class frmUpload(QWidget):
    picture_uploaded = pyqtSignal(QPixmap)  

    def __init__(self, existing_pixmap=None):
        super().__init__()
        self.resize(500, 527)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 5px solid #CECFC8; background-color: transparent; }")

        if existing_pixmap:
            self.current_pixmap = existing_pixmap
        else:
            self.current_pixmap = QPixmap("user.png") 

        # Picture display label
        self.picLabel = QLabel(self)
        self.picLabel.setFixedSize(200, 200)
        self.picLabel.move(155, 78)
        self.picLabel.setStyleSheet("background-color: transparent; border: 2px dashed #aaa;")
        self.picLabel.setScaledContents(True)

        if self.current_pixmap:
            self.picLabel.setPixmap(self.current_pixmap)

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

        # Save button 
        self.btnSave = QPushButton("Save", self)
        self.btnSave.setFixedSize(199, 56)
        self.btnSave.move(150, 450)
        self.btnSave.clicked.connect(self.save_picture)
        self.btnSave.setObjectName("btnSave")

        # Close button 
        self.btnClose = QPushButton("", self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(self.width() - 50, 5)  
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
        self.current_pixmap = QPixmap("user.png")  
        self.picLabel.setPixmap(self.current_pixmap)
        self.picLabel.setStyleSheet("background-color: transparent; border: 2px dashed #aaa;")

    def save_picture(self):
     if self.current_pixmap:
        reply = QMessageBox.question(
            self,
            "Confirm Save",
            "Do you want to save this picture?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.picture_uploaded.emit(self.current_pixmap)
            QMessageBox.information(self, "Success", "Picture uploaded successfully.")
            self.close()
        else:
            QMessageBox.information(self, "Cancelled", "Picture was not saved.")
            self.close() 
     else:
        QMessageBox.warning(self, "No Picture", "No picture to save.")

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("UploadBG.png")  
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

class frmMain(QWidget):
    def __init__(self): # , username
        super().__init__()
        self.resize(1920, 1020)
        self.setWindowFlags(Qt.FramelessWindowHint)
        #self.username = username

        self.upload_window = None
        self.about_sas_window = None
        self.last_uploaded_pixmap = None
        self.background_image = "chess.png"

        # Video Widget
        self.videoWidget = QVideoWidget(self)
        self.videoWidget.setGeometry(1130, 450, 700, 500)  

        # Media Player
        self.player = QMediaPlayer(self)
        self.player.setVideoOutput(self.videoWidget)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("LspuVideo.wmv")))
        self.player.setVolume(100)  
        self.player.play()         

        # Loop video when finished
        self.player.mediaStatusChanged.connect(self.handle_media_status)

        # Label to display username
        """self.lblUsername = QLabel(f"{username}", self)
        self.lblUsername.setFixedSize(400, 80)
        self.lblUsername.move(544, 43)
        self.lblUsername.setObjectName("lblUsername")"""

         # Text label
        self.lblSAS = QLabel("Student Assistant System", self)
        self.lblSAS.setFixedSize(800, 80)
        self.lblSAS.move(1050, 43)
        self.lblSAS.setObjectName("lblSAS")
        self.lblSAS.mousePressEvent = self.open_about_sas_form
       
        # Button to open upload form
        self.btnOpenUpload = QPushButton("", self)
        self.btnOpenUpload.setFixedSize(65, 65)
        self.btnOpenUpload.move(120, 48)
        self.btnOpenUpload.clicked.connect(self.open_upload_form)
        self.btnOpenUpload.setObjectName("btnUpload")

        # Set default user icon before any upload
        default_pixmap = QPixmap("user.png")
        if not default_pixmap.isNull():
            icon_size = QSize(55, 55)  
            scaled = default_pixmap.scaled(icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.btnOpenUpload.setIcon(QIcon(scaled))
            self.btnOpenUpload.setIconSize(icon_size)
            self.last_uploaded_pixmap = default_pixmap

        self.btn1_clicked = False
        self.btn2_clicked = False
        self.btn3_clicked = False
        self.btn4_clicked = False
        self.btn5_clicked = False

        self.btn1 = QPushButton("", self)
        self.btn1.setFixedSize(150, 150)
        self.btn1.move(110, 160)
        self.btn1.setIcon(QIcon("knight.png"))
        self.btn1.setIconSize(QSize(75, 75))
        self.btn1.setObjectName("btn1")  
        self.btn1.clicked.connect(self.set_chess_background)
        self.btn1.clicked.connect(self.handle_btn1_click)
        self.btn1.enterEvent = self.on_btn1_hover
        self.btn1.leaveEvent = self.on_btn1_leave

        self.btn2 = QPushButton("", self)
        self.btn2.setFixedSize(150, 150)
        self.btn2.move(270, 160)
        self.btn2.setIcon(QIcon("compass.png"))
        self.btn2.setIconSize(QSize(80, 80))
        self.btn2.setObjectName("btn2")
        self.btn2.clicked.connect(self.change_background)
        self.btn2.clicked.connect(self.handle_btn2_click)
        self.btn2.enterEvent = self.on_btn2_hover
        self.btn2.leaveEvent = self.on_btn2_leave

        self.btn3 = QPushButton("", self)
        self.btn3.setFixedSize(150, 150)
        self.btn3.move(430, 160)
        self.btn3.setIcon(QIcon("pin.png"))
        self.btn3.setIconSize(QSize(90, 90))
        self.btn3.setObjectName("btn3")  
        self.btn3.clicked.connect(self.change_background1)
        self.btn3.clicked.connect(self.handle_btn3_click)
        self.btn3.enterEvent = self.on_btn3_hover
        self.btn3.leaveEvent = self.on_btn3_leave

        self.btn4 = QPushButton("", self)
        self.btn4.setFixedSize(150, 150)
        self.btn4.move(590, 160)
        self.btn4.setIcon(QIcon("brain.png"))
        self.btn4.setIconSize(QSize(90, 90))
        self.btn4.setObjectName("btn4")  
        self.btn4.clicked.connect(self.change_background2)
        self.btn4.clicked.connect(self.handle_btn4_click)
        self.btn4.enterEvent = self.on_btn4_hover
        self.btn4.leaveEvent = self.on_btn4_leave

        self.btn5 = QPushButton("", self)
        self.btn5.setFixedSize(150, 150)
        self.btn5.move(750, 160)
        self.btn5.setIcon(QIcon("trends.png"))
        self.btn5.setIconSize(QSize(75, 75))
        self.btn5.setObjectName("btn5")  
        self.btn5.clicked.connect(self.change_background3)
        self.btn5.clicked.connect(self.handle_btn5_click)
        self.btn5.enterEvent = self.on_btn5_hover
        self.btn5.leaveEvent = self.on_btn5_leave

        self.btnCourse = QPushButton("View Courses", self)
        self.btnCourse.setFixedSize(350, 72)
        self.btnCourse.move(150, 830)
        self.btnCourse.setObjectName("btnCourse") 
        self.btnCourse.clicked.connect(self.About_Courses_form)

        self.btnLSPU = QPushButton("About LSPU", self)
        self.btnLSPU.setFixedSize(350, 72)
        self.btnLSPU.move(150, 830)
        self.btnLSPU.setObjectName("btnLSPU") 
        self.btnLSPU.clicked.connect(self.About_LSPU_form)
       
        self.btnRIASEC = QPushButton("View RIASEC", self)
        self.btnRIASEC.setFixedSize(350, 72)
        self.btnRIASEC.move(150, 830)
        self.btnRIASEC.setObjectName("btnRIASEC")  
        self.btnRIASEC.clicked.connect(self.About_Riasec_form)

        self.btnHistory = QPushButton("View History", self)
        self.btnHistory.setFixedSize(350, 72)
        self.btnHistory.move(150, 830)
        self.btnHistory.setObjectName("btnHistory") 

        self.btnTest = QPushButton("Test Now", self)
        self.btnTest.setFixedSize(350, 72)
        self.btnTest.move(150, 830)
        self.btnTest.setObjectName("btnTest")  
        self.btnTest.clicked.connect(self.open_questions_form)
      
        self.handle_btn1_click() 

        # Close Button
        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(self.width() - 50, 5)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.clicked.connect(self.handle_logout)
        self.btnClose.setObjectName("btnClose1")

        # Minimize Button
        self.btnMinimize = QPushButton("", self)
        self.btnMinimize.setFixedSize(43, 37)
        self.btnMinimize.move(self.width() - 150, 5)
        self.btnMinimize.setIcon(QIcon("Minimize.png")) 
        self.btnMinimize.setIconSize(QSize(25, 25))
        self.btnMinimize.clicked.connect(self.showMinimized)
        self.btnMinimize.setObjectName("btnMinimize")

        # Maximize / Restore Button
        self.btnMaximize = QPushButton("", self)
        self.btnMaximize.setFixedSize(43, 37)
        self.btnMaximize.move(self.width() - 100, 5)
        self.btnMaximize.setIcon(QIcon("Maximize.png"))  
        self.btnMaximize.setIconSize(QSize(21, 21))
        self.btnMaximize.clicked.connect(self.toggle_maximize_restore)
        self.btnMaximize.setObjectName("btnMaximize")

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

    def handle_logout(self):
        reply = QMessageBox.question(self, 'Logout Confirmation',
                                 'Do you want to logout?',
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            from frmLogin import frmLogin  
            self.login_window = frmLogin()
            self.login_window.show()
            self.close()  

    def open_upload_form(self):
        if self.about_sas_window and self.about_sas_window.isVisible():
            self.about_sas_window.close()

    # If already open, bring to front
        if self.upload_window and self.upload_window.isVisible():
            self.upload_window.raise_()
            self.upload_window.activateWindow()
        else:
            self.upload_window = frmUpload(existing_pixmap=self.last_uploaded_pixmap)
            self.upload_window.picture_uploaded.connect(self.set_upload_button_image)
            self.upload_window.show()

    def toggle_maximize_restore(self):
        if self.isMaximized():
            self.showNormal()
            self.btnMaximize.setIcon(QIcon("Maximize.png"))  
        else:
            self.showMaximized()
            self.btnMaximize.setIcon(QIcon("Maximize.png"))  

    @pyqtSlot(QPixmap)
    def set_upload_button_image(self, pixmap):
        self.last_uploaded_pixmap = pixmap  

        scaled_pixmap = pixmap.scaled(
        self.btnOpenUpload.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
    )
        self.btnOpenUpload.setIcon(QIcon(scaled_pixmap))
        self.btnOpenUpload.setIconSize(self.btnOpenUpload.size())

    def logout(self):
        from frmLogin import frmLogin  
        self.login_window = frmLogin()
        self.login_window.show()
        self.close()

    def open_about_sas_form(self, event):
        if self.upload_window and self.upload_window.isVisible():
            self.upload_window.close()

        if self.about_sas_window and self.about_sas_window.isVisible():
            self.about_sas_window.raise_()
            self.about_sas_window.activateWindow()
        else:
            self.about_sas_window = frmAboutSAS()
            self.about_sas_window.show()

    def set_chess_background(self):
        self.set_background_image("chess.png") 

    def change_background(self):
        self.background_image = "Navigation.png"
        self.update()  

    def change_background1(self):
        self.background_image = "LSPU.png"
        self.update()  

    def change_background2(self):
        self.background_image = "RIASEC.png"
        self.update()  

    def change_background3(self):
        self.background_image = "History.png"
        self.update()  

    def set_background_image(self, image_path):
        self.background_image = image_path
        self.update()  

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(self.background_image)  
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            x = (self.width() - scaled_pixmap.width()) // 2
            y = (self.height() - scaled_pixmap.height()) // 2
            painter.drawPixmap(x, y, scaled_pixmap)

    def handle_btn1_click(self):
        self.btnTest.setVisible(True) 
        self.btnCourse.setVisible(False)  
        self.btnLSPU.setVisible(False)     
        self.btnRIASEC.setVisible(False)   
        self.btnHistory.setVisible(False) 
        self.btn1_clicked = True
        self.btn1.setIcon(QIcon("knightR.png"))
        self.reset_btn2()
        self.reset_btn3()
        self.reset_btn4()
        self.reset_btn5()
        self.btn1.setStyleSheet("background-color: rgba(206, 207, 200, 0.9);")


    def handle_btn2_click(self):
        self.btnTest.setVisible(False) 
        self.btnCourse.setVisible(True)  
        self.btnLSPU.setVisible(False)     
        self.btnRIASEC.setVisible(False)   
        self.btnHistory.setVisible(False)
        self.btn2_clicked = True
        self.btn2.setIcon(QIcon("compassR.png"))
        self.reset_btn1()
        self.reset_btn3()
        self.reset_btn4()
        self.reset_btn5()
        self.btn2.setStyleSheet("background-color: rgba(206, 207, 200, 0.9);")

    def handle_btn3_click(self):
        self.btnTest.setVisible(False) 
        self.btnCourse.setVisible(False)  
        self.btnLSPU.setVisible(True)     
        self.btnRIASEC.setVisible(False)   
        self.btnHistory.setVisible(False)
        self.btn3_clicked = True
        self.btn3.setIcon(QIcon("pinR.png"))
        self.reset_btn1()
        self.reset_btn2()
        self.reset_btn4()
        self.reset_btn5()
        self.btn3.setStyleSheet("background-color: rgba(206, 207, 200, 0.9);")

    def handle_btn4_click(self):
        self.btnTest.setVisible(False) 
        self.btnCourse.setVisible(False)  
        self.btnLSPU.setVisible(False)     
        self.btnRIASEC.setVisible(True)   
        self.btnHistory.setVisible(False)
        self.btn4_clicked = True
        self.btn4.setIcon(QIcon("brainR.png"))
        self.reset_btn1()
        self.reset_btn2()
        self.reset_btn3()
        self.reset_btn5()
        self.btn4.setStyleSheet("background-color: rgba(206, 207, 200, 0.9);")

    def handle_btn5_click(self):
        self.btnTest.setVisible(False) 
        self.btnCourse.setVisible(False)  
        self.btnLSPU.setVisible(False)     
        self.btnRIASEC.setVisible(False)   
        self.btnHistory.setVisible(True) 
        self.btn5_clicked = True
        self.btn5.setIcon(QIcon("trendsR.png"))
        self.reset_btn1()
        self.reset_btn2()
        self.reset_btn3()
        self.reset_btn4()
        self.btn5.setStyleSheet("background-color: rgba(206, 207, 200, 0.9);")

    def reset_btn1(self):
        self.btn1_clicked = False
        self.btn1.setIcon(QIcon("knight.png"))
        self.btn1.setStyleSheet("background-color: none;")

    def reset_btn2(self):
        self.btn2_clicked = False
        self.btn2.setIcon(QIcon("compass.png"))
        self.btn2.setStyleSheet("background-color: none;")

    def reset_btn3(self):
        self.btn3_clicked = False
        self.btn3.setIcon(QIcon("pin.png"))
        self.btn3.setStyleSheet("background-color: none;")

    def reset_btn4(self):
        self.btn4_clicked = False
        self.btn4.setIcon(QIcon("brain.png"))
        self.btn4.setStyleSheet("background-color: none;")

    def reset_btn5(self):
        self.btn5_clicked = False
        self.btn5.setIcon(QIcon("trends.png"))
        self.btn5.setStyleSheet("background-color: none;")

    def on_btn1_hover(self, event):
        if not self.btn1_clicked:
            self.btn1.setIcon(QIcon("knightR.png"))
            self.btn1.setStyleSheet("background-color: rgba(61, 62, 60, 0.5);")
        super(QPushButton, self.btn1).enterEvent(event)  

    def on_btn1_leave(self, event):
        if not self.btn1_clicked:
            self.btn1.setIcon(QIcon("knight.png"))
            self.btn1.setStyleSheet("background-color: none;")
        super(QPushButton, self.btn1).leaveEvent(event)  

    def on_btn2_hover(self, event):
        if not self.btn2_clicked:
            self.btn2.setIcon(QIcon("compassR.png"))
            self.btn2.setStyleSheet("background-color: rgba(61, 62, 60, 0.5);")
        super(QPushButton, self.btn2).enterEvent(event)  

    def on_btn2_leave(self, event):
        if not self.btn2_clicked:
            self.btn2.setIcon(QIcon("compass.png"))
            self.btn2.setStyleSheet("background-color: none;")
        super(QPushButton, self.btn2).leaveEvent(event) 

    def on_btn3_hover(self, event):
        if not self.btn3_clicked:
            self.btn3.setIcon(QIcon("pinR.png"))
            self.btn3.setStyleSheet("background-color: rgba(61, 62, 60, 0.5);")
        super(QPushButton, self.btn3).enterEvent(event)   

    def on_btn3_leave(self, event):
        if not self.btn3_clicked:
            self.btn3.setIcon(QIcon("pin.png"))
            self.btn3.setStyleSheet("background-color: none;")
        super(QPushButton, self.btn3).leaveEvent(event) 

    def on_btn4_hover(self, event):
        if not self.btn4_clicked:
            self.btn4.setIcon(QIcon("brainR.png"))
            self.btn4.setStyleSheet("background-color: rgba(61, 62, 60, 0.5);")
        super(QPushButton, self.btn4).enterEvent(event)  

    def on_btn4_leave(self, event):
        if not self.btn4_clicked:
            self.btn4.setIcon(QIcon("brain.png"))
            self.btn4.setStyleSheet("background-color: none;")
        super(QPushButton, self.btn4).leaveEvent(event)  

    def on_btn5_hover(self, event):
         if not self.btn5_clicked:
            self.btn5.setIcon(QIcon("trendsR.png"))
            self.btn5.setStyleSheet("background-color: rgba(61, 62, 60, 0.5);")
         super(QPushButton, self.btn5).enterEvent(event)  

    def on_btn5_leave(self, event):
        if not self.btn5_clicked:
            self.btn5.setIcon(QIcon("trends.png"))
            self.btn5.setStyleSheet("background-color: none;")
        super(QPushButton, self.btn5).leaveEvent(event) 

    def open_questions_form(self):
        self.questions_form = frmQuestions() #self.username
        self.questions_form.show()
        #self.close()

    def About_LSPU_form(self):
        self.LSPU_form = frmAboutLSPU() 
        self.LSPU_form.show()
       
    def About_Riasec_form(self):
        self.Riasec_form = frmAboutRiasec() 
        self.Riasec_form.show()

    def About_Courses_form(self):
        self.Courses_form = frmAboutCourses() 
        self.Courses_form.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = frmMain()
    window.show()
    sys.exit(app.exec_())
