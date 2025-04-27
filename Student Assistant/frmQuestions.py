import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QPainter, QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize

class frmQuestions(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1920, 1020)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.image_list = [
            {"file": "Q1.png", "category": "realistic"},
            {"file": "Q2.png", "category": "investigative"},
            {"file": "Q3.png", "category": "artistic"},
            {"file": "Q4.png", "category": "social"},
            {"file": "Q5.png", "category": "enterprising"},
            {"file": "Q6.png", "category": "conventional"},
            {"file": "Q7.png", "category": "realistic"},
            {"file": "Q8.png", "category": "artistic"},
            {"file": "Q9.png", "category": "conventional"},
            {"file": "Q10.png", "category": "enterprising"},
            {"file": "Q11.png", "category": "investigative"},
            {"file": "Q12.png", "category": "social"},
            {"file": "Q13.png", "category": "social"},
            {"file": "Q14.png", "category": "realistic"},
            {"file": "Q15.png", "category": "conventional"},
            {"file": "Q16.png", "category": "enterprising"},
            {"file": "Q17.png", "category": "artistic"},
            {"file": "Q18.png", "category": "investigative"},
            {"file": "Q19.png", "category": "enterprising"},
            {"file": "Q20.png", "category": "social"},
            {"file": "Q21.png", "category": "investigative"},
            {"file": "Q22.png", "category": "realistic"},
            {"file": "Q23.png", "category": "artistic"},
            {"file": "Q24.png", "category": "conventional"},
            {"file": "Q25.png", "category": "conventional"},
            {"file": "Q26.png", "category": "investigative"},
            {"file": "Q27.png", "category": "artistic"},
            {"file": "Q28.png", "category": "social"},
            {"file": "Q29.png", "category": "enterprising"},
            {"file": "Q30.png", "category": "realistic"},
            {"file": "Q31.png", "category": "artistic"},
            {"file": "Q32.png", "category": "realistic"},
            {"file": "Q33.png", "category": "investigative"},
            {"file": "Q34.png", "category": "social"},
            {"file": "Q35.png", "category": "conventional"},
            {"file": "Q36.png", "category": "enterprising"},
            {"file": "Q37.png", "category": "realistic"},
            {"file": "Q38.png", "category": "conventional"},
            {"file": "Q39.png", "category": "investigative"},
            {"file": "Q40.png", "category": "social"},
            {"file": "Q41.png", "category": "artistic"},
            {"file": "Q42.png", "category": "enterprising"},
        ]
        self.current_image_index = 0

        # Initialize scores
        self.realisticScore = 0
        self.investigativeScore = 0
        self.artisticScore = 0
        self.socialScore = 0
        self.enterprisingScore = 0
        self.conventionalScore = 0

        # Track user answers (None = unanswered, 1 = Yes, 0 = No)
        self.answers = [None for _ in self.image_list]

        self.btnYes = QPushButton("Yes", self)
        self.btnYes.setFixedSize(300, 100)
        self.btnYes.move(651, 780)
        self.btnYes.setObjectName("btnYes")
        self.btnYes.clicked.connect(lambda: self.answer_question(1))

        self.btnNo = QPushButton("No", self)
        self.btnNo.setFixedSize(300, 100)
        self.btnNo.move(981, 780)
        self.btnNo.setObjectName("btnNo")
        self.btnNo.clicked.connect(lambda: self.answer_question(0))

        self.btnSubmit = QPushButton("Submit", self)
        self.btnSubmit.setFixedSize(300, 80)
        self.btnSubmit.move(1550, 885)
        self.btnSubmit.setObjectName("btnSubmit")
        self.btnSubmit.clicked.connect(self.submit_answers)

        self.btnBack = QPushButton("Back", self)
        self.btnBack.setFixedSize(199, 56)
        self.btnBack.move(1685, 40)
        self.btnBack.setObjectName("btnBack")
        self.btnBack.setIcon(QIcon("back.png"))
        self.btnBack.setIconSize(QSize(45, 45))
        self.btnBack.setLayoutDirection(Qt.RightToLeft)
        self.btnBack.clicked.connect(self.close)

        self.btnRight = QPushButton(self)
        self.btnRight.setFixedSize(70, 70)
        self.btnRight.move(1185, 125)
        self.btnRight.setObjectName("btnRight")
        self.btnRight.setIcon(QIcon("right.png"))
        self.btnRight.setIconSize(QSize(50, 50))
        self.btnRight.clicked.connect(self.go_next)

        self.btnLeft = QPushButton(self)
        self.btnLeft.setFixedSize(70, 70)
        self.btnLeft.move(670, 125)
        self.btnLeft.setObjectName("btnLeft")
        self.btnLeft.setIcon(QIcon("left.png"))
        self.btnLeft.setIconSize(QSize(50, 50))
        self.btnLeft.clicked.connect(self.go_previous)
       
        self.load_stylesheet("Questions.qss")
        self.update_buttons_color()  # Initialize button colors properly

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(self.image_list[self.current_image_index]["file"])
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            painter.drawPixmap(0, 0, scaled_pixmap)

    def load_stylesheet(self, file_path):
        try:
            with open(file_path, "r") as file:
                self.setStyleSheet(file.read())
        except Exception as e:
            print(f"Failed to load stylesheet: {e}")

    def answer_question(self, answer_value):
        category = self.image_list[self.current_image_index]["category"]

        # Check previous answer
        previous_answer = self.answers[self.current_image_index]

        # Update scores by removing previous answer
        if previous_answer == 1:
            if category == "realistic":
                self.realisticScore -= 1
            elif category == "investigative":
                self.investigativeScore -= 1
            elif category == "artistic":
                self.artisticScore -= 1
            elif category == "social":
                self.socialScore -= 1
            elif category == "enterprising":
                self.enterprisingScore -= 1
            elif category == "conventional":
                self.conventionalScore -= 1

    # Save the new answer
        self.answers[self.current_image_index] = answer_value

    # Update scores with new answer
        if answer_value == 1:
            if category == "realistic":
                self.realisticScore += 1
            elif category == "investigative":
                self.investigativeScore += 1
            elif category == "artistic":
                self.artisticScore += 1
            elif category == "social":
                self.socialScore += 1
            elif category == "enterprising":
                self.enterprisingScore += 1
            elif category == "conventional":
                self.conventionalScore += 1

        self.update_buttons_color()

    # Automatically move to next question after answering
        if self.current_image_index < len(self.image_list) - 1:
            self.current_image_index += 1
            self.update()
            self.update_buttons_color()

    def go_next(self):
        if self.answers[self.current_image_index] is None:
            QMessageBox.warning(self, "Warning", "Answer the current question first.")
            return  # Stop here if not answered yet
        if self.current_image_index < len(self.image_list) - 1:
            self.current_image_index += 1
            self.update()
            self.update_buttons_color()

    def go_previous(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.update()
            self.update_buttons_color()

    def update_buttons_color(self):
        """Update Yes/No button colors based on the saved answer for the current question."""
        answer = self.answers[self.current_image_index]
        if answer is None:
            # No answer yet, reset colors
            self.btnYes.setStyleSheet("")
            self.btnNo.setStyleSheet("")
        elif answer == 1:
            # Yes selected
            self.btnYes.setStyleSheet("background-color: #007FCD;")
            self.btnNo.setStyleSheet("")
        elif answer == 0:
            # No selected
            self.btnNo.setStyleSheet("background-color: #AA0000;")
            self.btnYes.setStyleSheet("")

    def submit_answers(self):
        self.show_results()

    def show_results(self):
        print("Realistic Score:", self.realisticScore)
        print("Investigative Score:", self.investigativeScore)
        print("Artistic Score:", self.artisticScore)
        print("Social Score:", self.socialScore)
        print("Enterprising Score:", self.enterprisingScore)
        print("Conventional Score:", self.conventionalScore)

        scores = {
            "realistic": self.realisticScore,
            "investigative": self.investigativeScore,
            "artistic": self.artisticScore,
            "social": self.socialScore,
            "enterprising": self.enterprisingScore,
            "conventional": self.conventionalScore
        }

        highest_category = max(scores, key=scores.get)
        print(f"Highest category: {highest_category}")

        category_image_map = {
            "realistic": "Realistic.png",
            "investigative": "Investigate.png",
            "artistic": "Artistic.png",
            "social": "Social.png",
            "enterprising": "Enterprising.png",
            "conventional": "Conventional.png"
        }

        result_image = category_image_map.get(highest_category, "default.png")
        self.image_list = [{
            "file": result_image,
            "category": highest_category
        }]
        self.current_image_index = 0
        self.update()

        self.btnYes.setEnabled(False)
        self.btnNo.setEnabled(False)

        self.btnLeft.hide()
        self.btnRight.hide()
        self.btnYes.hide()
        self.btnNo.hide()
        self.btnSubmit.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = frmQuestions()
    form.show()
    sys.exit(app.exec_())
