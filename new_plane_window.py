'''
29/04/2021
B Sumanth
Creating a new window
'''

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,QLabel) # import required modules from pyqt5,QWidget package
app = QApplication([])
class Window(QMainWindow):                                                  # create class for 1st main window
    def __init__(s):
        super().__init__()

        s.pushButton = QPushButton("Start", s)                        # create a button named start to get into new 2nd window
        s.pushButton.move(275, 200)                                      # locating the push button'start'
        s.label = QLabel("Hello World", s)                                # display content in the main window
        s.label.move(285, 175)                                           # positioning the content in main window
        s.setWindowTitle('www.Ecorvi.com')
        s.setGeometry(100,100,680,500)
        s.show()                                                         # displaying the main window
        

 
window = Window()

