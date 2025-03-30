# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/ecc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'C:/Users/DELL/AppData/Local/Programs/Python/Python39/Lib/site-packages/PyQt5/Qt/plugins/platforms'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(341, 290)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 51, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 41, 16))
        self.label_3.setObjectName("label_3")
        self.txtInfo = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtInfo.setGeometry(QtCore.QRect(90, 50, 181, 64))
        self.txtInfo.setObjectName("txtInfo")
        self.txtSign = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtSign.setGeometry(QtCore.QRect(90, 130, 181, 64))
        self.txtSign.setObjectName("txtSign")
        self.btnGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerate.setGeometry(QtCore.QRect(210, 20, 61, 17))
        self.btnGenerate.setObjectName("btnGenerate")
        self.btnSign = QtWidgets.QPushButton(self.centralwidget)
        self.btnSign.setGeometry(QtCore.QRect(90, 210, 56, 17))
        self.btnSign.setObjectName("btnSign")
        self.btnVerify = QtWidgets.QPushButton(self.centralwidget)
        self.btnVerify.setGeometry(QtCore.QRect(180, 210, 56, 17))
        self.btnVerify.setObjectName("btnVerify")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 341, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ECC CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Infomation"))
        self.label_3.setText(_translate("MainWindow", "Signature"))
        self.btnGenerate.setText(_translate("MainWindow", "Generate keys"))
        self.btnSign.setText(_translate("MainWindow", "Sign"))
        self.btnVerify.setText(_translate("MainWindow", "Verify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
