from MegaProj1 import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
class ControlWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.control = Ui_MainWindow()
        self.control.setupUi(self)
        self.control.Accelerate.clicked.connect(self.Acc)
        self.control.Decelerate.clicked.connect(self.Dec)
        self.control.Forwards.clicked.connect(self.Forward)
        self.control.Backwards.clicked.connect(self.Back)
        self.control.Right.clicked.connect(self.Right)
        self.control.Left.clicked.connect(self.Left)
        self.control.Stop.clicked.connect(self.Stop)
        self.control.Screenshot.clicked.connect(self.SS)
        self.control.speed1.clicked.connect(self.lowSpeed)
        self.control.speed2.clicked.connect(self.mediumSpeed)
        self.control.speed3.clicked.connect(self.highSpeed)
    def Acc(self):
        print('A')
        return 'A'
    def Dec(self):
        print('D')
        return 'D'
    def Forward(self):
        print('F')
        return 'F'
    def Right(self):
        print('R')
        return 'R'
    def Left(self):
        print('L')
        return 'L'
    def Back(self):
        print('B')
        return 'B'
    def lowSpeed(self):
        print(1)
        return 1
    def mediumSpeed(self):
        print(2)
        return 2
    def highSpeed(self):
        print(3)
        return 3
    def Stop(self):
        print('S')
        return 'S'
    def SS(self):
        print(0)
        return 0

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = ControlWindow()
    MainWindow.show()
    sys.exit(app.exec_())
