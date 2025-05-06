from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QMessageBox 
from PyQt5.QtGui import QPainter, QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
from frmAboutCoursesDesign import frmCTE1
from frmAboutCoursesDesign import frmCTE2
from frmAboutCoursesDesign import frmCTE3
from frmAboutCoursesDesign import frmCTE4
from frmAboutCoursesDesign import frmCTE5
from frmAboutCoursesDesign import frmCHMT1
from frmAboutCoursesDesign import frmCHMT2
from frmAboutCoursesDesign import frmCAS1
from frmAboutCoursesDesign import frmCAS2
from frmAboutCoursesDesign import frmCCJE1
from frmAboutCoursesDesign import frmCBAA1
from frmAboutCoursesDesign import frmCBAA2
from frmAboutCoursesDesign import frmCBAA3
from frmAboutCoursesDesign import frmCOE1
from frmAboutCoursesDesign import frmCOE2
from frmAboutCoursesDesign import frmCOE3
from frmAboutCoursesDesign import frmCCS1
from frmAboutCoursesDesign import frmCCS2
from frmAboutCoursesDesign import frmCIT1

class frmAboutCourses(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1920, 1020)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.background_image = QPixmap("LspuCTE.png")

        self.btnBack = QPushButton("Back", self)
        self.btnBack.setFixedSize(199, 46)
        self.btnBack.move(1708, 10)
        self.btnBack.setObjectName("btnBack")
        self.btnBack.setIcon(QIcon("back.png"))
        self.btnBack.setIconSize(QSize(42, 42))
        self.btnBack.setLayoutDirection(Qt.RightToLeft)
        self.btnBack.clicked.connect(self.confirm_back)

        self.cbDepartment = QComboBox(self)
        self.cbDepartment.addItems(["College of Teacher Education (CTE)",
                                    "College of Hospitality Management and Tourism (CHMT)",
                                    "College of Arts and Science (CAS)", 
                                    "College of Criminal Justice Education (CCJE)", 
                                    "College of Business Administration and Accountancy (CBAA)", 
                                    "College of Engineering (COE)", 
                                    "College of Computer Studies (CCS)", 
                                    "College of Industrial Technology (CIT)"])
        self.cbDepartment.setFixedSize(650, 70)
        self.cbDepartment.move(105, 562)
        self.cbDepartment.setObjectName("cbDept")
        self.cbDepartment.currentTextChanged.connect(self.Department_selection)

        self.cbCampuses = QComboBox(self)
        self.cbCampuses.addItems(["LSPU San Pablo City", "LSPU Sta. Cruz", "LSPU Los Banos", "LSPU Siniloan"])
        self.cbCampuses.setFixedSize(650, 70)
        self.cbCampuses.move(105, 729)
        self.cbCampuses.setObjectName("cbDept")
        self.cbCampuses.currentTextChanged.connect(self.Campus_selection)

        # College of Teacher Education (CTE) ====================================================================

        self.btnCTE1 = QPushButton("View Course", self)
        self.btnCTE1.setFixedSize(240, 60)
        self.btnCTE1.move(1504, 267)
        self.btnCTE1.setObjectName("cbCTE")
        self.btnCTE1.clicked.connect(self.CTE1_Result)

        self.btnCTE2 = QPushButton("View Course", self)
        self.btnCTE2.setFixedSize(240, 60)
        self.btnCTE2.move(1504, 376)
        self.btnCTE2.setObjectName("cbCTE")
        self.btnCTE2.clicked.connect(self.CTE2_Result)

        self.btnCTE3 = QPushButton("View Course", self)
        self.btnCTE3.setFixedSize(240, 60)
        self.btnCTE3.move(1504, 483)
        self.btnCTE3.setObjectName("cbCTE")
        self.btnCTE3.clicked.connect(self.CTE3_Result)

        self.btnCTE4 = QPushButton("View Course", self)
        self.btnCTE4.setFixedSize(240, 60)
        self.btnCTE4.move(1504, 587)
        self.btnCTE4.setObjectName("cbCTE")
        self.btnCTE4.clicked.connect(self.CTE4_Result)

        self.btnCTE5 = QPushButton("View Course", self)
        self.btnCTE5.setFixedSize(240, 60)
        self.btnCTE5.move(1504, 695)
        self.btnCTE5.setObjectName("cbCTE")
        self.btnCTE5.clicked.connect(self.CTE5_Result)

        self.btnCTE6 = QPushButton("View Course", self)
        self.btnCTE6.setFixedSize(240, 60)
        self.btnCTE6.move(1504, 799)
        self.btnCTE6.setObjectName("cbCTE1")

        self.btnCTE6.setEnabled(False)

        # College of Hospitality Management and Tourism (CHMT) ====================================================================

        self.btnCHMT1 = QPushButton("View Course", self)
        self.btnCHMT1.setFixedSize(240, 60)
        self.btnCHMT1.move(1504, 267)
        self.btnCHMT1.setObjectName("cbCHMT")
        self.btnCHMT1.clicked.connect(self.CHMT1_Result)

        self.btnCHMT2 = QPushButton("View Course", self)
        self.btnCHMT2.setFixedSize(240, 60)
        self.btnCHMT2.move(1504, 376)
        self.btnCHMT2.setObjectName("cbCHMT")
        self.btnCHMT2.clicked.connect(self.CHMT2_Result)

        self.btnCHMT1.hide()
        self.btnCHMT2.hide()

        # College of Arts and Science (CAS) ====================================================================

        self.btnCAS1 = QPushButton("View Course", self)
        self.btnCAS1.setFixedSize(240, 60)
        self.btnCAS1.move(1504, 267)
        self.btnCAS1.setObjectName("cbCAS")
        self.btnCAS1.clicked.connect(self.CAS1_Result)

        self.btnCAS2 = QPushButton("View Course", self)
        self.btnCAS2.setFixedSize(240, 60)
        self.btnCAS2.move(1504, 376)
        self.btnCAS2.setObjectName("cbCAS")
        self.btnCAS2.clicked.connect(self.CAS2_Result)

        self.btnCAS3 = QPushButton("View Course", self)
        self.btnCAS3.setFixedSize(240, 60)
        self.btnCAS3.move(1504, 483)
        self.btnCAS3.setObjectName("cbCAS1")

        self.btnCAS4 = QPushButton("View Course", self)
        self.btnCAS4.setFixedSize(240, 60)
        self.btnCAS4.move(1504, 587)
        self.btnCAS4.setObjectName("cbCAS1")

        self.btnCAS5 = QPushButton("View Course", self)
        self.btnCAS5.setFixedSize(240, 60)
        self.btnCAS5.move(1504, 695)
        self.btnCAS5.setObjectName("cbCAS1")

        self.btnCAS6 = QPushButton("View Course", self)
        self.btnCAS6.setFixedSize(240, 60)
        self.btnCAS6.move(1504, 799)
        self.btnCAS6.setObjectName("cbCAS1")

        self.btnCAS1.hide()
        self.btnCAS2.hide()
        self.btnCAS3.hide()
        self.btnCAS4.hide()
        self.btnCAS5.hide()
        self.btnCAS6.hide()

        self.btnCAS3.setEnabled(False)
        self.btnCAS4.setEnabled(False)
        self.btnCAS5.setEnabled(False)
        self.btnCAS6.setEnabled(False)

        # College of Criminal Justice Education (CCJE) ====================================================================

        self.btnCCJE1 = QPushButton("View Course", self)
        self.btnCCJE1.setFixedSize(240, 60)
        self.btnCCJE1.move(1504, 267)
        self.btnCCJE1.setObjectName("cbCCJE")
        self.btnCCJE1.clicked.connect(self.CCJE1_Result)

        self.btnCCJE2 = QPushButton("View Course", self)
        self.btnCCJE2.setFixedSize(240, 60)
        self.btnCCJE2.move(1504, 376)
        self.btnCCJE2.setObjectName("cbCCJE1")

        self.btnCCJE3 = QPushButton("View Course", self)
        self.btnCCJE3.setFixedSize(240, 60)
        self.btnCCJE3.move(1504, 483)
        self.btnCCJE3.setObjectName("cbCCJE1")

        self.btnCCJE4 = QPushButton("View Course", self)
        self.btnCCJE4.setFixedSize(240, 60)
        self.btnCCJE4.move(1504, 587)
        self.btnCCJE4.setObjectName("cbCCJE1")

        self.btnCCJE1.hide()
        self.btnCCJE2.hide()
        self.btnCCJE3.hide()
        self.btnCCJE4.hide()

        self.btnCCJE2.setEnabled(False)
        self.btnCCJE3.setEnabled(False)
        self.btnCCJE4.setEnabled(False)

        # College of Business Administration and Accountancy (CBAA) ====================================================================

        self.btnCBAA1 = QPushButton("View Course", self)
        self.btnCBAA1.setFixedSize(240, 60)
        self.btnCBAA1.move(1504, 267)
        self.btnCBAA1.setObjectName("cbCBAA")
        self.btnCBAA1.clicked.connect(self.CBAA1_Result)

        self.btnCBAA2 = QPushButton("View Course", self)
        self.btnCBAA2.setFixedSize(240, 60)
        self.btnCBAA2.move(1504, 376)
        self.btnCBAA2.setObjectName("cbCBAA")
        self.btnCBAA2.clicked.connect(self.CBAA2_Result)

        self.btnCBAA3 = QPushButton("View Course", self)
        self.btnCBAA3.setFixedSize(240, 60)
        self.btnCBAA3.move(1504, 483)
        self.btnCBAA3.setObjectName("cbCBAA")
        self.btnCBAA3.clicked.connect(self.CBAA3_Result)

        self.btnCBAA4 = QPushButton("View Course", self)
        self.btnCBAA4.setFixedSize(240, 60)
        self.btnCBAA4.move(1504, 587)
        self.btnCBAA4.setObjectName("cbCBAA1")

        self.btnCBAA5 = QPushButton("View Course", self)
        self.btnCBAA5.setFixedSize(240, 60)
        self.btnCBAA5.move(1504, 695)
        self.btnCBAA5.setObjectName("cbCBAA1")

        self.btnCBAA1.hide()
        self.btnCBAA2.hide()
        self.btnCBAA3.hide()
        self.btnCBAA4.hide()
        self.btnCBAA5.hide()

        self.btnCBAA4.setEnabled(False)
        self.btnCBAA5.setEnabled(False)

        # College of Engineering (COE) ====================================================================

        self.btnCOE1 = QPushButton("View Course", self)
        self.btnCOE1.setFixedSize(240, 60)
        self.btnCOE1.move(1504, 267)
        self.btnCOE1.setObjectName("cbCOE")
        self.btnCOE1.clicked.connect(self.COE1_Result)

        self.btnCOE2 = QPushButton("View Course", self)
        self.btnCOE2.setFixedSize(240, 60)
        self.btnCOE2.move(1504, 376)
        self.btnCOE2.setObjectName("cbCOE")
        self.btnCOE2.clicked.connect(self.COE2_Result)

        self.btnCOE3 = QPushButton("View Course", self)
        self.btnCOE3.setFixedSize(240, 60)
        self.btnCOE3.move(1504, 483)
        self.btnCOE3.setObjectName("cbCOE")
        self.btnCOE3.clicked.connect(self.COE3_Result)

        self.btnCOE4 = QPushButton("View Course", self)
        self.btnCOE4.setFixedSize(240, 60)
        self.btnCOE4.move(1504, 587)
        self.btnCOE4.setObjectName("cbCOE1")

        self.btnCOE5 = QPushButton("View Course", self)
        self.btnCOE5.setFixedSize(240, 60)
        self.btnCOE5.move(1504, 695)
        self.btnCOE5.setObjectName("cbCOE1")

        self.btnCOE6 = QPushButton("View Course", self)
        self.btnCOE6.setFixedSize(240, 60)
        self.btnCOE6.move(1504, 799)
        self.btnCOE6.setObjectName("cbCOE1")

        self.btnCOE1.hide()
        self.btnCOE2.hide()
        self.btnCOE3.hide()
        self.btnCOE4.hide()
        self.btnCOE5.hide()
        self.btnCOE6.hide()

        self.btnCOE4.setEnabled(False)
        self.btnCOE5.setEnabled(False)
        self.btnCOE6.setEnabled(False)

        # College of Computer Studies (CCS) ====================================================================

        self.btnCCS1 = QPushButton("View Course", self)
        self.btnCCS1.setFixedSize(240, 60)
        self.btnCCS1.move(1504, 267)
        self.btnCCS1.setObjectName("cbCCS")
        self.btnCCS1.clicked.connect(self.CCS1_Result)

        self.btnCCS2 = QPushButton("View Course", self)
        self.btnCCS2.setFixedSize(240, 60)
        self.btnCCS2.move(1504, 376)
        self.btnCCS2.setObjectName("cbCCS")
        self.btnCCS2.clicked.connect(self.CCS2_Result)

        self.btnCCS3 = QPushButton("View Course", self)
        self.btnCCS3.setFixedSize(240, 60)
        self.btnCCS3.move(1504, 483)
        self.btnCCS3.setObjectName("cbCCS1")

        self.btnCCS4 = QPushButton("View Course", self)
        self.btnCCS4.setFixedSize(240, 60)
        self.btnCCS4.move(1504, 587)
        self.btnCCS4.setObjectName("cbCCS1")

        self.btnCCS5 = QPushButton("View Course", self)
        self.btnCCS5.setFixedSize(240, 60)
        self.btnCCS5.move(1504, 695)
        self.btnCCS5.setObjectName("cbCCS1")

        self.btnCCS6 = QPushButton("View Course", self)
        self.btnCCS6.setFixedSize(240, 60)
        self.btnCCS6.move(1504, 799)
        self.btnCCS6.setObjectName("cbCCS1")

        self.btnCCS1.hide()
        self.btnCCS2.hide()
        self.btnCCS3.hide()
        self.btnCCS4.hide()
        self.btnCCS5.hide()
        self.btnCCS6.hide()

        self.btnCCS3.setEnabled(False)
        self.btnCCS4.setEnabled(False)
        self.btnCCS5.setEnabled(False)
        self.btnCCS6.setEnabled(False)

        # College of Industrial Technology (CIT) ====================================================================

        self.btnCIT1 = QPushButton("View Course", self)
        self.btnCIT1.setFixedSize(240, 60)
        self.btnCIT1.move(1504, 267)
        self.btnCIT1.setObjectName("cbCIT")
        self.btnCIT1.clicked.connect(self.CIT1_Result)

        self.btnCIT2 = QPushButton("View Course", self)
        self.btnCIT2.setFixedSize(240, 60)
        self.btnCIT2.move(1504, 376)
        self.btnCIT2.setObjectName("cbCIT1")

        self.btnCIT3 = QPushButton("View Course", self)
        self.btnCIT3.setFixedSize(240, 60)
        self.btnCIT3.move(1504, 483)
        self.btnCIT3.setObjectName("cbCIT1")

        self.btnCIT1.hide()
        self.btnCIT2.hide()
        self.btnCIT3.hide()

        self.btnCIT2.setEnabled(False)
        self.btnCIT3.setEnabled(False)

        self.load_stylesheet("AboutCourses.qss")

    def confirm_back(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        if not self.background_image.isNull():
            scaled_pixmap = self.background_image.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
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

    def Department_selection(self, text):
        if text == "College of Teacher Education (CTE)":
            self.background_image = QPixmap("LspuCTE.png")  
            self.btnCTE1.show()
            self.btnCTE2.show()
            self.btnCTE3.show()
            self.btnCTE4.show()
            self.btnCTE5.show()
            self.btnCTE6.show()
            self.btnCHMT1.hide()
            self.btnCHMT2.hide()
            self.btnCAS1.hide()
            self.btnCAS2.hide()
            self.btnCAS3.hide()
            self.btnCAS4.hide()
            self.btnCAS5.hide()
            self.btnCAS6.hide()
            self.btnCCJE1.hide()
            self.btnCCJE2.hide()
            self.btnCCJE3.hide()
            self.btnCCJE4.hide()
            self.btnCBAA1.hide()
            self.btnCBAA2.hide()
            self.btnCBAA3.hide()
            self.btnCBAA4.hide()
            self.btnCBAA5.hide()
            self.btnCCS1.hide()
            self.btnCCS2.hide()
            self.btnCCS3.hide()
            self.btnCCS4.hide()
            self.btnCCS5.hide()
            self.btnCCS6.hide()
            self.btnCIT1.hide()
            self.btnCIT2.hide()
            self.btnCIT3.hide()
            self.update()  
        elif text == "College of Hospitality Management and Tourism (CHMT)":
            self.background_image = QPixmap("LspuCHMT.png")  
            self.btnCTE1.hide()
            self.btnCTE2.hide()
            self.btnCTE3.hide()
            self.btnCTE4.hide()
            self.btnCTE5.hide()
            self.btnCTE6.hide()
            self.btnCHMT1.show()
            self.btnCHMT2.show()
            self.btnCAS1.hide()
            self.btnCAS2.hide()
            self.btnCAS3.hide()
            self.btnCAS4.hide()
            self.btnCAS5.hide()
            self.btnCAS6.hide()
            self.btnCCJE1.hide()
            self.btnCCJE2.hide()
            self.btnCCJE3.hide()
            self.btnCCJE4.hide()
            self.btnCBAA1.hide()
            self.btnCBAA2.hide()
            self.btnCBAA3.hide()
            self.btnCBAA4.hide()
            self.btnCBAA5.hide()
            self.btnCOE1.hide()
            self.btnCOE2.hide()
            self.btnCOE3.hide()
            self.btnCOE4.hide()
            self.btnCOE5.hide()
            self.btnCOE6.hide()
            self.btnCCS1.hide()
            self.btnCCS2.hide()
            self.btnCCS3.hide()
            self.btnCCS4.hide()
            self.btnCCS5.hide()
            self.btnCCS6.hide()
            self.btnCIT1.hide()
            self.btnCIT2.hide()
            self.btnCIT3.hide()
            self.update()  
        elif text == "College of Arts and Science (CAS)":
            self.background_image = QPixmap("LspuCAS.png")  
            self.btnCTE1.hide()
            self.btnCTE2.hide()
            self.btnCTE3.hide()
            self.btnCTE4.hide()
            self.btnCTE5.hide()
            self.btnCTE6.hide()
            self.btnCHMT1.hide()
            self.btnCHMT2.hide()
            self.btnCAS1.show()
            self.btnCAS2.show()
            self.btnCAS3.show()
            self.btnCAS4.show()
            self.btnCAS5.show()
            self.btnCAS6.show()
            self.btnCCJE1.hide()
            self.btnCCJE2.hide()
            self.btnCCJE3.hide()
            self.btnCCJE4.hide()
            self.btnCBAA1.hide()
            self.btnCBAA2.hide()
            self.btnCBAA3.hide()
            self.btnCBAA4.hide()
            self.btnCBAA5.hide()
            self.btnCOE1.hide()
            self.btnCOE2.hide()
            self.btnCOE3.hide()
            self.btnCOE4.hide()
            self.btnCOE5.hide()
            self.btnCOE6.hide()
            self.btnCCS1.hide()
            self.btnCCS2.hide()
            self.btnCCS3.hide()
            self.btnCCS4.hide()
            self.btnCCS5.hide()
            self.btnCCS6.hide()
            self.btnCIT1.hide()
            self.btnCIT2.hide()
            self.btnCIT3.hide()
            self.update()  
        elif text == "College of Criminal Justice Education (CCJE)":
            self.background_image = QPixmap("LspuCCJE.png")
            self.btnCTE1.hide()
            self.btnCTE2.hide()
            self.btnCTE3.hide()
            self.btnCTE4.hide()
            self.btnCTE5.hide()
            self.btnCTE6.hide()
            self.btnCHMT1.hide()
            self.btnCHMT2.hide()
            self.btnCAS1.hide()
            self.btnCAS2.hide()
            self.btnCAS3.hide()
            self.btnCAS4.hide()
            self.btnCAS5.hide()
            self.btnCAS6.hide()
            self.btnCCJE1.show()
            self.btnCCJE2.show()
            self.btnCCJE3.show()
            self.btnCCJE4.show()
            self.btnCBAA1.hide()
            self.btnCBAA2.hide()
            self.btnCBAA3.hide()
            self.btnCBAA4.hide()
            self.btnCBAA5.hide()
            self.btnCOE1.hide()
            self.btnCOE2.hide()
            self.btnCOE3.hide()
            self.btnCOE4.hide()
            self.btnCOE5.hide()
            self.btnCOE6.hide()
            self.btnCCS1.hide()
            self.btnCCS2.hide()
            self.btnCCS3.hide()
            self.btnCCS4.hide()
            self.btnCCS5.hide()
            self.btnCCS6.hide()
            self.btnCIT1.hide()
            self.btnCIT2.hide()
            self.btnCIT3.hide()
            self.update()  
        elif text == "College of Business Administration and Accountancy (CBAA)":
            self.background_image = QPixmap("LspuCBAA.png")
            self.btnCTE1.hide()
            self.btnCTE2.hide()
            self.btnCTE3.hide()
            self.btnCTE4.hide()
            self.btnCTE5.hide()
            self.btnCTE6.hide()
            self.btnCHMT1.hide()
            self.btnCHMT2.hide()
            self.btnCAS1.hide()
            self.btnCAS2.hide()
            self.btnCAS3.hide()
            self.btnCAS4.hide()
            self.btnCAS5.hide()
            self.btnCAS6.hide()
            self.btnCCJE1.hide()
            self.btnCCJE2.hide()
            self.btnCCJE3.hide()
            self.btnCCJE4.hide()
            self.btnCBAA1.show()
            self.btnCBAA2.show()
            self.btnCBAA3.show()
            self.btnCBAA4.show()
            self.btnCBAA5.show()
            self.btnCOE1.hide()
            self.btnCOE2.hide()
            self.btnCOE3.hide()
            self.btnCOE4.hide()
            self.btnCOE5.hide()
            self.btnCOE6.hide()
            self.btnCCS1.hide()
            self.btnCCS2.hide()
            self.btnCCS3.hide()
            self.btnCCS4.hide()
            self.btnCCS5.hide()
            self.btnCCS6.hide()
            self.btnCIT1.hide()
            self.btnCIT2.hide()
            self.btnCIT3.hide()
            self.update()  
        elif text == "College of Engineering (COE)":
            self.background_image = QPixmap("LspuCOE.png")
            self.btnCTE1.hide()
            self.btnCTE2.hide()
            self.btnCTE3.hide()
            self.btnCTE4.hide()
            self.btnCTE5.hide()
            self.btnCTE6.hide()
            self.btnCHMT1.hide()
            self.btnCHMT2.hide()
            self.btnCAS1.hide()
            self.btnCAS2.hide()
            self.btnCAS3.hide()
            self.btnCAS4.hide()
            self.btnCAS5.hide()
            self.btnCAS6.hide()
            self.btnCCJE1.hide()
            self.btnCCJE2.hide()
            self.btnCCJE3.hide()
            self.btnCCJE4.hide()
            self.btnCBAA1.hide()
            self.btnCBAA2.hide()
            self.btnCBAA3.hide()
            self.btnCBAA4.hide()
            self.btnCBAA5.hide()
            self.btnCOE1.show()
            self.btnCOE2.show()
            self.btnCOE3.show()
            self.btnCOE4.show()
            self.btnCOE5.show()
            self.btnCOE6.show()
            self.btnCCS1.hide()
            self.btnCCS2.hide()
            self.btnCCS3.hide()
            self.btnCCS4.hide()
            self.btnCCS5.hide()
            self.btnCCS6.hide()
            self.btnCIT1.hide()
            self.btnCIT2.hide()
            self.btnCIT3.hide()
            self.update()  
        elif text == "College of Computer Studies (CCS)":
            self.background_image = QPixmap("LspuCCS.png")  
            self.btnCTE1.hide()
            self.btnCTE2.hide()
            self.btnCTE3.hide()
            self.btnCTE4.hide()
            self.btnCTE5.hide()
            self.btnCTE6.hide()
            self.btnCHMT1.hide()
            self.btnCHMT2.hide()
            self.btnCAS1.hide()
            self.btnCAS2.hide()
            self.btnCAS3.hide()
            self.btnCAS4.hide()
            self.btnCAS5.hide()
            self.btnCAS6.hide()
            self.btnCCJE1.hide()
            self.btnCCJE2.hide()
            self.btnCCJE3.hide()
            self.btnCCJE4.hide()
            self.btnCBAA1.hide()
            self.btnCBAA2.hide()
            self.btnCBAA3.hide()
            self.btnCBAA4.hide()
            self.btnCBAA5.hide()
            self.btnCOE1.hide()
            self.btnCOE2.hide()
            self.btnCOE3.hide()
            self.btnCOE4.hide()
            self.btnCOE5.hide()
            self.btnCOE6.hide()
            self.btnCCS1.show()
            self.btnCCS2.show()
            self.btnCCS3.show()
            self.btnCCS4.show()
            self.btnCCS5.show()
            self.btnCCS6.show()
            self.btnCIT1.hide()
            self.btnCIT2.hide()
            self.btnCIT3.hide()
            self.update()  
        elif text == "College of Industrial Technology (CIT)":
            self.background_image = QPixmap("LspuCIT.png")
            self.btnCTE1.hide()
            self.btnCTE2.hide()
            self.btnCTE3.hide()
            self.btnCTE4.hide()
            self.btnCTE5.hide()
            self.btnCTE6.hide()
            self.btnCHMT1.hide()
            self.btnCHMT2.hide()
            self.btnCAS1.hide()
            self.btnCAS2.hide()
            self.btnCAS3.hide()
            self.btnCAS4.hide()
            self.btnCAS5.hide()
            self.btnCAS6.hide()
            self.btnCCJE1.hide()
            self.btnCCJE2.hide()
            self.btnCCJE3.hide()
            self.btnCCJE4.hide()
            self.btnCBAA1.hide()
            self.btnCBAA2.hide()
            self.btnCBAA3.hide()
            self.btnCBAA4.hide()
            self.btnCBAA5.hide()
            self.btnCOE1.hide()
            self.btnCOE2.hide()
            self.btnCOE3.hide()
            self.btnCOE4.hide()
            self.btnCOE5.hide()
            self.btnCOE6.hide()
            self.btnCCS1.hide()
            self.btnCCS2.hide()
            self.btnCCS3.hide()
            self.btnCCS4.hide()
            self.btnCCS5.hide()
            self.btnCCS6.hide()
            self.btnCIT1.show()
            self.btnCIT2.show()
            self.btnCIT3.show()
            self.update()  
        else:
            self.set_background_image("LspuCTE.png")
            self.update()  

    # College of Teacher Education (CTE) ====================================================================
    def CTE1_Result(self):
        self.Courses_form = frmCTE1() 
        self.Courses_form.show()

    def CTE2_Result(self):
        self.Courses_form = frmCTE2() 
        self.Courses_form.show()

    def CTE3_Result(self):
        self.Courses_form = frmCTE3() 
        self.Courses_form.show()

    def CTE4_Result(self):
        self.Courses_form = frmCTE5() 
        self.Courses_form.show()

    def CTE5_Result(self):
        self.Courses_form = frmCTE4() 
        self.Courses_form.show()

     # College of Hospitality Management and Tourism (CHMT) ====================================================================
    def CHMT1_Result(self):
        self.Courses_form = frmCHMT1() 
        self.Courses_form.show()

    def CHMT2_Result(self):
        self.Courses_form = frmCHMT2() 
        self.Courses_form.show()

    # College of Arts and Science (CAS) ====================================================================
    def CAS1_Result(self):
        self.Courses_form = frmCAS1() 
        self.Courses_form.show()

    def CAS2_Result(self):
        self.Courses_form = frmCAS2() 
        self.Courses_form.show()

    # College of Criminal Justice Education (CCJE) ====================================================================
    def CCJE1_Result(self):
        self.Courses_form = frmCCJE1() 
        self.Courses_form.show()

    # College of Business Administration and Accountancy (CBAA) ====================================================================
    def CBAA1_Result(self):
        self.Courses_form = frmCBAA1() 
        self.Courses_form.show()

    def CBAA2_Result(self):
        self.Courses_form = frmCBAA2() 
        self.Courses_form.show()

    def CBAA3_Result(self):
        self.Courses_form = frmCBAA3() 
        self.Courses_form.show()

    # College of Engineering (COE) ====================================================================
    def COE1_Result(self):
        self.Courses_form = frmCOE1() 
        self.Courses_form.show()

    def COE2_Result(self):
        self.Courses_form = frmCOE2() 
        self.Courses_form.show()

    def COE3_Result(self):
        self.Courses_form = frmCOE3() 
        self.Courses_form.show()

     # College of Computer Studies (CCS) ====================================================================
    def CCS1_Result(self):
        self.Courses_form = frmCCS1() 
        self.Courses_form.show()

    def CCS2_Result(self):
        self.Courses_form = frmCCS2() 
        self.Courses_form.show()

    # College of Industrial Technology ====================================================================
    def CIT1_Result(self):
        self.Courses_form = frmCIT1() 
        self.Courses_form.show()

    def Campus_selection(self, text):
         if text in ["LSPU Sta. Cruz", "LSPU Los Banos", "LSPU Siniloan"]:
             QMessageBox.information(self, "Unavailable", f"Sorry, {text} is still unavailable.")
             self.cbCampuses.setCurrentText("LSPU San Pablo City") 

if __name__ == "__main__":
    app = QApplication([])
    window = frmAboutCourses()
    window.show()
    app.exec_()
