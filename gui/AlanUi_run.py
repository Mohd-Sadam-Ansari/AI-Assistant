#from AlanUI import Ui_ALAN
from alan_ui import Ui_MainWindow
from PyQt5 import QtCore ,QtGui ,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import os
from contextlib import redirect_stdout
import io

# Example for testing(in run function call Main() instead of wish())
#import wish
#import weather
#import jokes


class MainThread(QThread):

    def __init__(self):

        super(MainThread,self).__init__()
'''    def run(self):
        wish.wish()
        #weather.weather("kolkata")'''
    
startExecution=MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui=Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.start_button.clicked.connect(self.startTask)
    
        
    def startTask(self):

       
        timer=QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(1000)

        #f=io.StringIO()
        #with redirect_stdout(f):
        #greet=wish.wish()
            #weather.weather("Mumbai")
        #joke=jokes.jokes()
        #res=system.system()

        self.ui.terminal.setText('Alan: I am your personal Desktop Assistant')
        
        startExecution.start()

    def showTimeLive(self):
        time_live=QTime.currentTime()
        time=time_live.toString()
        label_Time='TIME:'+time

        self.ui.time_browser.setText(label_Time)

GuiApp=QApplication(sys.argv)
Alan_ui=Gui_Start()
Alan_ui.show()
exit(GuiApp.exec_())