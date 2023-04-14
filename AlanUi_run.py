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

import sys
import os
sys.path.append("..")
sys.path.append("tts/")
sys.path.append("intent_classification/")
sys.path.append("features/")
sys.path.append("stt/")


from stt import whisper_stt
from tts import speak
from intent_classification import model,alan,nltk_utils
from features import system,api,greet,browser
from playsound import playsound

from main import mainexecution

class Gui_Start(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        timer=QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(1000)

        self.ui.start_button.clicked.connect(self.startTask)
        
    def startTask(self):
        while True:
            result=mainexecution()
            self.ui.terminal.append(result)      

    def showTimeLive(self):
        time_live=QTime.currentTime()
        time=time_live.toString()
        label_Time='TIME:'+time
        self.ui.time_browser.setText(label_Time)

GuiApp=QApplication(sys.argv)
Alan_ui=Gui_Start()
Alan_ui.show()
exit(GuiApp.exec_())