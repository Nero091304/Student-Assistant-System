from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QLabel, QFileDialog
from PyQt5.QtGui import QPainter, QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class frmRealisticPaper(QWidget):
    def __init__(self, username, date_value="", personality_value="", score_value="", all_scores=None):
        super().__init__()
        self.setFixedSize(693, 945)  
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.username = username

        if all_scores is None:
            all_scores = {} 

        personality_backgrounds = {
            "REALISTIC" : "RealisticPaper.png",
            "INVESTIGATIVE": "InvestigativePaper.png",
            "ARTISTIC": "ArtisticPaper.png",
            "SOCIAL": "SocialPaper.png",
            "ENTERPRISING": "EnterprisingPaper.png",
            "CONVENTIONAL": "ConventionalPaper.png"
        }
        self.background_image = personality_backgrounds.get(personality_value, "RealisticPaper.png")

        self.container = QFrame(self)
        self.container.setGeometry(0, 0, self.width(), self.height())
        self.container.setStyleSheet("QFrame { border: 3px solid #000000; background-color: transparent; }")

        self.lblUsername = QLabel(f"{self.username}", self)
        self.lblUsername.setFixedSize(256, 40)
        self.lblUsername.move(75, 186)
        self.lblUsername.setObjectName("lblUsername")

        self.lblDate = QLabel(self)
        self.lblDate.setFixedSize(125, 33)
        self.lblDate.move(135, 223)
        self.lblDate.setText(date_value)
        self.lblDate.setObjectName("lblDate")

        self.lblPersonality = QLabel("", self)
        self.lblPersonality.setFixedSize(360, 45)
        self.lblPersonality.move(378, 217)
        self.lblPersonality.setText(personality_value)
        self.lblPersonality.setObjectName("lblPersonality")

        self.lblScore = QLabel(self)
        self.lblScore.setFixedSize(360, 45)
        self.lblScore.move(521, 255)
        self.lblScore.setText(score_value)
        self.lblScore.setObjectName("lblScore")

        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(645, 5)
        self.btnClose.setIcon(QIcon("cross.png"))  
        self.btnClose.setIconSize(QSize(35, 35))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

        self.load_stylesheet("Export.qss")

        self.init_chart(all_scores)

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

    def init_chart(self, scores_dict):
        figure = Figure(figsize=(4, 3))
        canvas = FigureCanvas(figure)
        canvas.setParent(self)
        canvas.setGeometry(378, 357, 280, 211)  # Adjust position/size as needed

        ax = figure.add_subplot(111)
        labels = list(scores_dict.keys())
        values = list(scores_dict.values())  

        ax.bar(labels, values, color='blue')
        ax.set_ylim(0, 7)  # Max raw score is 42
        ax.set_ylabel("Raw Score")
        ax.set_title("Personality Type Scores")
        ax.tick_params(axis='x', rotation=45)

    def export_to_file(self):
        # Capture the window content to a QPixmap
        pixmap = QPixmap(self.size())
        self.render(pixmap)  # Render the window content into the pixmap

        # Open file dialog to select location to save the file
        file_dialog = QFileDialog(self)
        file_dialog.setDefaultSuffix('png')  # Default file type is PNG
        file_path, _ = file_dialog.getSaveFileName(self, "Save File", "", "Images (*.png *.jpg *.bmp)")
        
        if file_path:
            pixmap.save(file_path)  # Save the file to the selected path
            print(f"File saved to {file_path}")

    def export_to_png(self):
        self.btnClose.setVisible(False)
        pixmap = self.grab()

    # Get the personality value from lblPersonality to create the file name
        personality_value = self.lblPersonality.text()

    # Generate a custom filename based on the username and personality value
        filename = f"{self.username}_{personality_value}PAPER.png"

    # Sanitize the filename to replace any invalid characters for filenames
        filename = filename.replace(" ", "_").replace("/", "-").replace(":", "-")

    # Show file dialog to save the PNG with the generated filename
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save as PNG", filename, "PNG Files (*.png);;All Files (*)", options=options)

        if file_name:
        # Save the pixmap as PNG to the selected file location
            pixmap.save(file_name, "PNG")

if __name__ == "__main__":
    app = QApplication([])
    window = frmRealisticPaper()
    window.show()
    app.exec_()
