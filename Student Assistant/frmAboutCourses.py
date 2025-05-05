from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox
from PyQt5.QtGui import QPainter, QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize

class frmAboutCourses(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1920, 1020)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.btnBack = QPushButton("Back", self)
        self.btnBack.setFixedSize(199, 46)
        self.btnBack.move(1708, 10)
        self.btnBack.setObjectName("btnBack")
        self.btnBack.setIcon(QIcon("back.png"))
        self.btnBack.setIconSize(QSize(42, 42))
        self.btnBack.setLayoutDirection(Qt.RightToLeft)
        self.btnBack.clicked.connect(self.confirm_back)

        self.cbDepartment = QComboBox(self)
        self.cbDepartment.addItems(["Default", "College of Teacher Education (CTE)", "College of Hospitality Management and Tourism (CHMT)", "College of Arts and Science (CAS)", "College of Criminal Justice Education (CCJE)", "College of Business Administration and Accountancy (CBAA)", "College of Engineering (COE)", "College of Computer Studies (CCS)", "College of Industrial Technology (CIT)"])
        self.cbDepartment.setFixedSize(650, 70)
        self.cbDepartment.move(105, 562)
        self.cbDepartment.setObjectName("cbDept")

        self.cbCampuses = QComboBox(self)
        self.cbCampuses.addItems(["LSPU San Pablo City", "LSPU Sta. Cruz", "LSPU Los Banos", "LSPU Siniloan"])
        self.cbCampuses.setFixedSize(650, 70)
        self.cbCampuses.move(105, 729)
        self.cbCampuses.setObjectName("cbDept")

        # College of Teacher Education (CTE) ====================================================================

        self.btnCTE1 = QPushButton("View Course", self)
        self.btnCTE1.setFixedSize(240, 60)
        self.btnCTE1.move(1504, 267)
        self.btnCTE1.setObjectName("cbCTE")

        self.btnCTE2 = QPushButton("View Course", self)
        self.btnCTE2.setFixedSize(240, 60)
        self.btnCTE2.move(1504, 376)
        self.btnCTE2.setObjectName("cbCTE")

        self.btnCTE3 = QPushButton("View Course", self)
        self.btnCTE3.setFixedSize(240, 60)
        self.btnCTE3.move(1504, 483)
        self.btnCTE3.setObjectName("cbCTE")

        self.btnCTE4 = QPushButton("View Course", self)
        self.btnCTE4.setFixedSize(240, 60)
        self.btnCTE4.move(1504, 587)
        self.btnCTE4.setObjectName("cbCTE")

        self.btnCTE5 = QPushButton("View Course", self)
        self.btnCTE5.setFixedSize(240, 60)
        self.btnCTE5.move(1504, 695)
        self.btnCTE5.setObjectName("cbCTE")

        self.btnCTE6 = QPushButton("View Course", self)
        self.btnCTE6.setFixedSize(240, 60)
        self.btnCTE6.move(1504, 799)
        self.btnCTE6.setObjectName("cbCTE")

        # College of Hospitality Management and Tourism (CHMT) ====================================================================

        self.btnCHMT1 = QPushButton("View Course", self)
        self.btnCHMT1.setFixedSize(240, 60)
        self.btnCHMT1.move(1504, 267)
        self.btnCHMT1.setObjectName("cbCHMT")

        self.btnCHMT2 = QPushButton("View Course", self)
        self.btnCHMT2.setFixedSize(240, 60)
        self.btnCHMT2.move(1504, 376)
        self.btnCHMT2.setObjectName("cbCHMT")

        # College of Arts and Science (CAS) ====================================================================

        self.btnCAS1 = QPushButton("View Course", self)
        self.btnCAS1.setFixedSize(240, 60)
        self.btnCAS1.move(1504, 267)
        self.btnCAS1.setObjectName("cbCAS")

        self.btnCAS2 = QPushButton("View Course", self)
        self.btnCAS2.setFixedSize(240, 60)
        self.btnCAS2.move(1504, 376)
        self.btnCAS2.setObjectName("cbCAS")

        # College of Criminal Justice Education (CCJE) ====================================================================

        self.btnCCJE1 = QPushButton("View Course", self)
        self.btnCCJE1.setFixedSize(240, 60)
        self.btnCCJE1.move(1504, 267)
        self.btnCCJE1.setObjectName("cbCCJE")

        # College of Business Administration and Accountancy (CBAA) ====================================================================

        self.btnCBAA1 = QPushButton("View Course", self)
        self.btnCBAA1.setFixedSize(240, 60)
        self.btnCBAA1.move(1504, 267)
        self.btnCBAA1.setObjectName("cbCBAA")

        self.btnCBAA2 = QPushButton("View Course", self)
        self.btnCBAA2.setFixedSize(240, 60)
        self.btnCBAA2.move(1504, 376)
        self.btnCBAA2.setObjectName("cbCBAA")

        self.btnCBAA3 = QPushButton("View Course", self)
        self.btnCBAA3.setFixedSize(240, 60)
        self.btnCBAA3.move(1504, 483)
        self.btnCBAA3.setObjectName("cbCBAA")

        # College of Engineering (COE) ====================================================================

        self.btnCOE1 = QPushButton("View Course", self)
        self.btnCOE1.setFixedSize(240, 60)
        self.btnCOE1.move(1504, 267)
        self.btnCOE1.setObjectName("cbCOE")

        self.btnCOE2 = QPushButton("View Course", self)
        self.btnCOE2.setFixedSize(240, 60)
        self.btnCOE2.move(1504, 376)
        self.btnCOE2.setObjectName("cbCOE")

        self.btnCOE3 = QPushButton("View Course", self)
        self.btnCOE3.setFixedSize(240, 60)
        self.btnCOE3.move(1504, 483)
        self.btnCOE3.setObjectName("cbCOE")

        # College of Computer Studies (CCS) ====================================================================

        self.btnCCS1 = QPushButton("View Course", self)
        self.btnCCS1.setFixedSize(240, 60)
        self.btnCCS1.move(1504, 267)
        self.btnCCS1.setObjectName("cbCCS")

        self.btnCCS2 = QPushButton("View Course", self)
        self.btnCCS2.setFixedSize(240, 60)
        self.btnCCS2.move(1504, 376)
        self.btnCCS2.setObjectName("cbCCS")

        # College of Industrial Technology) ====================================================================

        self.btnCIT1 = QPushButton("View Course", self)
        self.btnCIT1.setFixedSize(240, 60)
        self.btnCIT1.move(1504, 267)
        self.btnCIT1.setObjectName("cbCIT")

        self.load_stylesheet("AboutCourses.qss")

    def confirm_back(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("AboutCourses1.png")  
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
    window = frmAboutCourses()
    window.show()
    app.exec_()
