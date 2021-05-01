
"""
Created on Sat May  1 17:58:07 2021

@author: Sumanth
"""

import sys  # importing sys
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel)


# import required modules from pyqt5,QWidget package


class Window2(QMainWindow):  # create class for second window
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window22222")  # naming the 2nd window


class Window(QMainWindow):  # create class for 1st main window
    def __init__(self):
        super().__init__()

        self.label = QLabel(current_time, self)  # display content in the main window
        self.title = "First Window"  # defining 1st window name
        self.top = 100  # distance from top of screen
        self.left = 100  # distance from left side
        self.width = 680  # width of window
        self.height = 500  # height of window

        self.label1 = QLabel(current_time, self)  # create a button named start to get into new 2nd window
        self.label1.move(0, 0)  # locating the push button 'start'
        self.label1.setToolTip("<h3>NewDelhi</h3>")
        # displays the given line when cursor placed on the pushbutton

        # self.pushButton.clicked.connect(self.window2)
        # after a click on push button,it connects to second window class and executes it

        self.main_window()  # calling main window function

    def main_window(self):  # defining main_window function
        self.label.move(610, 0)  # positioning the content in main window
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()  # displaying the main window

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
