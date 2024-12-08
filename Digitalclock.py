import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, Qt, QTime
from PyQt5.QtGui import QFont, QFontDatabase

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("Digital Clock")
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        font_id = QFontDatabase.addApplicationFont("../topics/GUI/DS-DIGIT.TTF")
        if font_id != -1:
            family_font = QFontDatabase.applicationFontFamilies(font_id)[0]
            my_font = QFont(family_font, 100)
            self.time_label.setFont(QFont(my_font))
        else:
            print("Failed to load the font, Using default font")
            self.time_label.setStyleSheet("font-style: poppins;"
                                          "font-size: 100px;")

        self.time_label.setStyleSheet("color: lime;")
        self.setStyleSheet("background-color: black;")

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    digi_clock = Widget()
    digi_clock.show()
    sys.exit(app.exec_())