import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QFont, QFontDatabase

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.timer_label = QLabel("00:00:00.00", self)
        self.time = QTime(0, 0, 0, 0)
        self.timer = QTimer(self)
        self.button1 = QPushButton("Start", self)
        self.button2 = QPushButton("Stop", self)
        self.button3 = QPushButton("Reset", self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle("Stop Watch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.timer_label)
        self.setLayout(vbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        vbox.addLayout(hbox)

        font_id = QFontDatabase.addApplicationFont("C:/Users/udayk/OneDrive/Desktop/python/topics/GUI/DS-DIGIT.TTF")
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            my_font = QFont(font_family, 100)
            self.timer_label.setFont(my_font)
        else:
            print("Failed to load the font, using default font")
            self.timer_label.setStyleSheet("font-style: calibre;"
                                           "font-size: 100px;")

        self.timer_label.setStyleSheet("color: lime;"
                                       "background-color: black;")

        self.setStyleSheet("""
            QPushButton{
                font-style: calibre;
                font-size: 40px;
                border: 2px solid black;
                background-color: hsl(90, 10%, 83%)
            }
            QLabel, QPushButton{
                padding: 15px;
                border-radius: 15px;
            }
            QPushButton:hover{
                background-color: hsl(83, 1%, 58%)
            }
        """)

        self.button1.clicked.connect(self.start)
        self.button2.clicked.connect(self.stop)
        self.button3.clicked.connect(self.reset)

    def start(self):
        self.timer.timeout.connect(self.update_time)
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.timer_label.setText("00:00:00.00")

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.timer_label.setText(self.time.toString("hh:mm:ss.zzz")[:-1])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stop_watch = Widget()
    stop_watch.show()
    sys.exit(app.exec_())