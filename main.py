import sys
from PyQt5.uic import loadUi
from MegaProj1 import Ui_MainWindow
from FirstScreen import Ui_FirstScreen
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Auto import Ui_Atonomous
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import cv2
import serial
import bluetooth
def connect ():
    bd_addr = "00:19:08:00:30:24"
    port = 1
    sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))
    sock.send("standby")
    sock.close()
#The Manual Control screen class:
class ControlWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.control = Ui_MainWindow()
        self.control.setupUi(self)
        #Setting all the speed displays to zero
        self.control.SpeedLevel.setValue(0)
        self.control.Speed.setValue(0)
        #When Accelerate is clicked it goes to its desired function and so
        self.control.Accelerate.clicked.connect(self.Acc)
        self.control.Decelerate.clicked.connect(self.Dec)
        self.control.Forwards.clicked.connect(self.Forward)
        self.control.Backwards.clicked.connect(self.Back)
        self.control.Right.clicked.connect(self.Right)
        self.control.Left.clicked.connect(self.Left)
        self.control.Stop.clicked.connect(self.Stop)
        self.control.SpeedLevel.valueChanged.connect(self.SpeedLev)
        #On clicking the "Switch to Auto" button it calls the switchAuto function.
        self.control.M2A.clicked.connect(self.switchAuto)
        self.control.M2A.clicked.connect(self.closingManual)
        self.MyWebCam1 = MyWebcam()
        self.MyWebCam1.start()
        self.MyWebCam1.LiveCam.connect(self.LiveFeedSlot)
        # self.myScreenshot = ScreenshotThread()
        # self.myScreenshot.start()
        self.control.Screenshot.clicked.connect(self.SS)
    def LiveFeedSlot(self, Image):
        self.control.Webcam.setPixmap(QPixmap.fromImage(Image))
    #Switching modes from Manual to Auto whilst being in Manual Control window.
    def switchAuto(self):
        self.windowAuto = AutoScreen()
        self.windowAuto.show()
        return 98
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
        print("STILL NOTHING :<")

        #cv2.imwrite(filename, self.MyWebCam1.)
#The next screen is the first to appear upon launching the program:
class AutoScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.autoPilot=Ui_Atonomous()
        self.autoPilot.setupUi(self)
        self.autoPilot.A2M.clicked.connect(self.switchManual)
        self.autoPilot.A2M.clicked.connect(self.closingAuto)
        self.autoPilot.Speed.setValue(33)
        self.autoPilot.Stop.clicked.connect(self.Stop)
        self.autoPilot.Distance.valueChanged.connect(self.setDistance)
        self.MyWebCam2 = MyWebcam()
        self.MyWebCam2.start()
        self.MyWebCam2.LiveCam.connect(self.LiveFeedSlot2)
    def LiveFeedSlot2(self, Image):
        self.autoPilot.Webcam2.setPixmap(QPixmap.fromImage(Image))
        #self.autoPilot.Screenshot.clicked.connect(self.SS)
    def setDistance(self):
        return self.autoPilot.Distance.value()
    def Stop(self):
        self.autoPilot.Speed.setValue(0)
        return 0
    def switchManual(self):
        self.windowManual = ControlWindow()
        self.windowManual.show()
        return 99
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
class MyWebcam(QThread):
    LiveCam = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        FeedCam = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = FeedCam.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                self.Live = ConvertToQtFormat.scaled(1150, 701, Qt.KeepAspectRatio)
                self.LiveCam.emit(self.Live)
#     def ScS(self):
#         filename = 'Screens.jpg'
#         img = cv2.imwrite(filename, cv2.VideoCapture(0))
# class ScreenshotThread(QThread):
#     key = cv2.waitKey(1)
#     webcam = cv2.VideoCapture(0)
#     while True:
#         try:
#             check, frame = webcam.read()
#             print(check)  # prints true as long as the webcam is running
#             print(frame)  # prints matrix values of each framecd
#             cv2.imshow("Capturing", frame)
#             key = cv2.waitKey(1)
#             if key == ord('s'):
#                 cv2.imwrite(filename='saved_img.jpg', img=frame)
#                 webcam.release()
#                 img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
#                 img_new = cv2.imshow("Captured Image", img_new)
#                 cv2.waitKey(1650)
#                 cv2.destroyAllWindows()
#                 print("Processing image...")
#                 img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
#                 print("Converting RGB image to grayscale...")
#                 gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
#                 print("Converted RGB image to grayscale...")
#                 print("Resizing image to 28x28 scale...")
#                 img_ = cv2.resize(gray, (28, 28))
#                 print("Resized...")
#                 img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
#                 print("Image saved!")
#
#                 break
#             elif key == ord('q'):
#                 print("Turning off camera.")
#                 webcam.release()
#                 print("Camera off.")
#                 print("Program ended.")
#                 cv2.destroyAllWindows()
#                 break

        # except(KeyboardInterrupt):
        #     print("Turning off camera.")
        #     webcam.release()
        #     print("Camera off.")
        #     print("Program ended.")
        #     cv2.destroyAllWindows()
        #     break
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = firstScreen()
    mainWindow.show()
    sys.exit(app.exec_())
