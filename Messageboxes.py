
from PyQt5.QtWidgets import QMessageBox
from Messageboxes import *

	
def showDialog(mode,msgText,msgTitle):
   msgBox = QMessageBox()
   msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
   
   if mode.upper() == "INFO":
        msgBox.setIcon(QMessageBox.Information)
      #   msgBox.setStandardButtons(QMessageBox.Ok)
   msgBox.setText(msgText)
   msgBox.setWindowTitle(msgTitle)
   msgBox.buttonClicked.connect(msgButtonClick)

   returnValue = msgBox.exec()
   if returnValue == QMessageBox.Ok:
      print('OK clicked')
      
   else:
      print("Canceled!")

   return returnValue
   
def msgButtonClick(i):
   
   
   print("Button clicked is:",i.text())


