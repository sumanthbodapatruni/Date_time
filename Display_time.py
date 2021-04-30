'''
30/4/2021
B Sumanth
creating a digital clock
'''


import sys
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt
  
  
class Window(QWidget):
  
    def __init__(self):
        super().__init__()
  
                                                    
        self.setGeometry(100, 100, 800, 400)        # setting geometry of main window
        
        layout = QVBoxLayout()                      # creating a vertical layout
          
        font = QFont('Arial', 120, QFont.Bold)      # creating font object
          
        self.label = QLabel()                       # creating a label object
          
        self.label.setAlignment(Qt.AlignCenter)     # setting centre alignment to the label
          
        self.label.setFont(font)                    # setting font to the label
          
        layout.addWidget(self.label)                # adding label to the layout
          
        self.setLayout(layout)                      # setting the layout to main window
          
        timer = QTimer(self)                        # creating a timer object
          
        timer.timeout.connect(self.showTime)        # adding action to timer
         
        timer.start(1000)                           # update the timer every second
  
    
    def showTime(self):                             # method called by timer
  
        
        current_time = QTime.currentTime()          # getting current time
          
        label_time = current_time.toString('hh:mm:ss')# converting QTime object to string
  
        self.label.setText(label_time)               # showing it to the label
  
  

App = QApplication(sys.argv)                # create pyqt5 app
window = Window()                           # create the instance of our Window
window.show()                               # showing all the widgets
App.exit(App.exec_())                       # start the app
