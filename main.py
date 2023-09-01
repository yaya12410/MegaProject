from PyQt5.uic import loadUi
from MegaProj1 import Ui_MainWindow
from FirstScreen import Ui_FirstScreen
from Auto import Ui_Atonomous
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
#The Manual Control screen class:
class ControlWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.control = Ui_MainWindow()
        self.control.setupUi(self)
        #loadUi("MegaProj1", self)
        self.control.SpeedLevel.setValue(0)
        self.control.Speed.setValue(0)
        self.control.Accelerate.clicked.connect(self.Acc)
        self.control.Decelerate.clicked.connect(self.Dec)
        self.control.Forwards.clicked.connect(self.Forward)
        self.control.Backwards.clicked.connect(self.Back)
        self.control.Right.clicked.connect(self.Right)
        self.control.Left.clicked.connect(self.Left)
        self.control.Stop.clicked.connect(self.Stop)
        self.control.Screenshot.clicked.connect(self.SS)
        self.control.SpeedLevel.valueChanged.connect(self.SpeedLev)
        #On clicking the "Switch to Auto" button it calls the switchAuto function.
        self.control.M2A.clicked.connect(self.switchAuto)
        self.control.M2A.clicked.connect(self.closingManual)
    #Switching modes from Manual to Auto whilst being in Manual Control window.
    def switchAuto(self):
        self.windowAuto = AutoScreen()
        self.windowAuto.show()
    def closingManual(self):
        self.hide()
    def SetSpeedPercentage(self):
        self.control.Speed.setValue(int((self.control.SpeedLevel.value()/3)*100))
    def Acc(self):
        self.control.SpeedLevel.setValue(self.control.SpeedLevel.value() + 1)
        return 'A'
    def Dec(self):
        self.control.SpeedLevel.setValue(self.control.SpeedLevel.value() - 1)
        return 'D'
    def Forward(self):
        return 'F'
    def Right(self):
        return 'R'
    def Left(self):
        return 'L'
    def Back(self):
        return 'B'
    def SpeedLev(self):
        self.SetSpeedPercentage()
        return self.control.SpeedLevel.value()
    def Stop(self):
        self.control.SpeedLevel.setValue(0)
        return 'S'
    def SS(self):
        print("Still looking how to take a screenshot")
        return 0
#The next screen is the first to appear upon launching the program:
class AutoScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.autoPilot=Ui_Atonomous()
        self.autoPilot.setupUi(self)
        self.autoPilot.A2M.clicked.connect(self.switchManual)
        self.autoPilot.A2M.clicked.connect(self.closingAuto)
        self.autoPilot.Speed.setValue((200//3))
        self.autoPilot.Stop.clicked.connect(self.Stop)
        self.autoPilot.Distance.textChanged.connect(self.setDistance)
        #self.autoPilot.Screenshot.clicked.connect(self.SS)
    def setDistance(self):
        self.myText = self.autoPilot.Distance.toPlainText()
        return int(self.myText)
    def Stop(self):
        self.autoPilot.Speed.setValue(0)
    def switchManual(self):
        self.windowManual = ControlWindow()
        self.windowManual.show()
    def closingAuto(self):
        self.hide()

class firstScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.screen1 = Ui_FirstScreen()
        self.screen1.setupUi(self)
        self.screen1.Manual.clicked.connect(self.openManual)
        self.screen1.Auto.clicked.connect(self.openAuto)
    def openManual(self):
        self.windowManual = ControlWindow()
        mainWindow.hide()
        self.windowManual.show()
    def openAuto(self):
        #User opened the program and chose the manual mode, so we are switching to the Manual Control screen.
        self.windowAuto = AutoScreen()
        mainWindow.hide()
        self.windowAuto.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = firstScreen()
    mainWindow.show()
    sys.exit(app.exec_())
