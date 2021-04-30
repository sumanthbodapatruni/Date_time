import sys  # importing sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel)
# import required modules from pyqt5,QWidget package


class Window2(QMainWindow):    # create class for second window
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window22222")  # naming the 2nd window


class Window(QMainWindow):    # create class for 1st main window
    def __init__(self):
        super().__init__()

        self.title = "First Window"     # defining 1st window name
        self.top = 100  # distance from top of screen
        self.left = 100  # distance from left side
        self.width = 680  # width of window
        self.height = 500    # height of window

        self.pushButton = QPushButton("Start", self)   # create a button named start to get into new 2nd window
        self.pushButton.move(275, 200)                  # locating the push button 'start'
        self.pushButton.setToolTip("<h3>Start the Session</h3>")
        # displays the given line when cursor placed on the pushbutton

        self.pushButton.clicked.connect(self.window2)  
        # after a click on push button,it connects to second window class and executes it
        
        self.main_window()   # calling main window function

    def main_window(self):   # defining main_window function
        self.label = QLabel("Manager", self)  # display content in the main window
        self.label.move(285, 175)  # positioning the content in main window
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()  # displaying the main window

    def window2(self):
        self.w = Window2()  # calling 2nd window function and assign
        self.w.show()   # display the second window
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
