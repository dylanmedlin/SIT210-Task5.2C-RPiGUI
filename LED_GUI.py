from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO

pins = [12,10,8] # red green blue
GPIO.setmode(GPIO.BOARD)
for i in pins:
    GPIO.setup(i, GPIO.OUT)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(305, 218)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.RedButton = QtWidgets.QRadioButton(self.centralwidget)
        self.RedButton.setObjectName("RedButton")
        self.RedButton.toggled.connect(self.onClickedRed)
        self.verticalLayout.addWidget(self.RedButton)

        self.GreenButton = QtWidgets.QRadioButton(self.centralwidget)
        self.GreenButton.setObjectName("GreenButton")
        self.GreenButton.toggled.connect(self.onClickedGreen)
        self.verticalLayout.addWidget(self.GreenButton)

        self.BlueButton = QtWidgets.QRadioButton(self.centralwidget)
        self.BlueButton.setObjectName("BlueButton")
        self.BlueButton.toggled.connect(self.onClickedBlue)
        self.verticalLayout.addWidget(self.BlueButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Click button to turn on LED"))
        self.RedButton.setText(_translate("MainWindow", "Red"))
        self.GreenButton.setText(_translate("MainWindow", "Green"))
        self.BlueButton.setText(_translate("MainWindow", "Blue"))
    
    def onClickedRed(self):
        GPIO.output(pins[0], GPIO.HIGH)
        GPIO.output(pins[1], GPIO.LOW)
        GPIO.output(pins[2], GPIO.LOW)
    
    def onClickedGreen(self):
        GPIO.output(pins[0], GPIO.LOW)
        GPIO.output(pins[1], GPIO.HIGH)
        GPIO.output(pins[2], GPIO.LOW)

    def onClickedBlue(self):
        GPIO.output(pins[0], GPIO.LOW)
        GPIO.output(pins[1], GPIO.LOW)
        GPIO.output(pins[2], GPIO.HIGH)

if __name__ == "__main__":
    try:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    finally:
        GPIO.cleanup()
