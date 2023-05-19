from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from inner_main import *
from register import *
from PyQt5 import QtWidgets,QtCore
from PyQt5 import QtCore, QtGui, QtWidgets

# class Ui_MainWindow(QWidget):
#     def __init__(self):
#         super(Ui_MainWindow, self).__init__()
#         self.setupUi()
#
#     def setupUi(self):
#         self.resize(800, 600)
#         self.setWindowTitle('登陆页面')
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap("D:\Pycharm\Lab_pro\PyQtFiberSort\logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#
#         _translate = QtCore.QCoreApplication.translate
#         self.pushButton_register = QtWidgets.QPushButton(self)
#         self.pushButton_register.setGeometry(QtCore.QRect(250, 500, 100, 53))
#         self.pushButton_register.setObjectName("pushButton_register")
#         self.pushButton_register.setText(_translate("MainWindow", "注册"))
#
#
#         self.pushButtonOK = QtWidgets.QPushButton(self)
#         self.pushButtonOK.setGeometry(QtCore.QRect(150, 350, 100, 53))
#         self.pushButtonOK.setObjectName("pushButtonOK")
#         self.pushButtonOK.setText(_translate("MainWindow", "确定"))
#
#         self.pushButtonCancel = QtWidgets.QPushButton(self)
#         self.pushButtonCancel.setGeometry(QtCore.QRect(350, 350, 100, 53))
#         self.pushButtonCancel.setObjectName("pushButtonCancel")
#         self.pushButtonCancel.setText(_translate("MainWindow", "取消"))
#
#         label_wzbj = 'border-width:1px;border-style:solid;font-size:15px;border-color:rgb(0,0,0,0.5);background-color:rgb(255,255,255,0.3);'
#         self.label_zh = QLabel(self)
#         self.label_zh.setText("账户 :")
#         self.label_zh.move(100, 170)
#         self.label_zh.setFixedSize(100, 30)
#         self.label_zh.setStyleSheet(label_wzbj)
#         self.label_zh.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
#
#         self.label_mm = QLabel(self)
#         self.label_mm.setText("密码 :")
#         self.label_mm.move(100, 250)
#         self.label_mm.setFixedSize(100, 30)
#         self.label_mm.setStyleSheet(label_wzbj)
#         self.label_mm.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
#
#         self.sr_zh = QLineEdit(self)
#         # self.sr_zh.setText("32261228")  # 用户名
#         self.sr_zh.setPlaceholderText("请输入您的账号")
#         self.sr_zh.move(210, 170)
#         self.sr_zh.setFixedSize(400, 30)
#         self.sr_zh.setStyleSheet(label_wzbj)
#
#         self.sr_mm = QLineEdit(self)
#         self.sr_mm.setPlaceholderText("请输入您的密码")
#         self.sr_mm.setEchoMode(QLineEdit.PasswordEchoOnEdit)  # 密码输入正常，之后特殊显示
#         self.sr_mm.move(210, 250)
#         self.sr_mm.setFixedSize(400, 30)
#         self.sr_mm.setStyleSheet(label_wzbj)


# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     app.setStyleSheet(open('./custom/styleSheet.qss', encoding='utf-8').read())
#     MainWindow = QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#
#     ui_Register = Example()
#     # ui_hello = MyApp()
#     sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log_in.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("FPGA-opticalFiber")
        MainWindow.resize(875, 646)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 40, 451, 151))
        self.label.setStyleSheet("#label{\n"
"    color:rgb(170, 85, 0);background:rgb(255, 254, 239);border:2px solid #F3F3F5;border-radius:45px;\n"
"                font-size:15pt; font-weight:400;font-family: Roman times;\n"
"}")
        self.label.setObjectName("label")
        self.label_zh = QtWidgets.QLabel(self.centralwidget)
        self.label_zh.setGeometry(QtCore.QRect(110, 250, 101, 41))
        self.label_zh.setObjectName("label_zh")
        self.label_mm = QtWidgets.QLabel(self.centralwidget)
        self.label_mm.setGeometry(QtCore.QRect(110, 320, 101, 41))
        self.label_mm.setObjectName("label_mm")
        self.sr_zh = QtWidgets.QLineEdit(self.centralwidget)
        self.sr_zh.setGeometry(QtCore.QRect(180, 250, 531, 41))
        # self.sr_zh.setText("")
        self.sr_zh.setStyleSheet("#sr_zh{\n"
"color:rgb(170, 0, 0);\n"
"                    border:2px solid #F3F3F5;\n"
"                    border-radius:15px;\n"
"                    background:rgb(230, 255, 255);\n"
"border:2px solid #423f48;\n"
"}")
        self.sr_zh.setObjectName("sr_zh")
        self.sr_mm = QtWidgets.QLineEdit(self.centralwidget)
        self.sr_mm.setGeometry(QtCore.QRect(180, 320, 531, 41))
        self.sr_mm.setEchoMode(2)
        self.sr_mm.setStyleSheet("#sr_mm{\n"
"color:rgb(170, 0, 0);\n"
"                    border:2px solid #F3F3F5;\n"
"                    border-radius:15px;\n"
"                    background:rgb(230, 255, 255);\n"
"border:2px solid #423f48;\n"
"}")
        self.sr_mm.setObjectName("sr_mm")
        self.pushButtonOK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOK.setGeometry(QtCore.QRect(220, 410, 131, 51))
        self.pushButtonOK.setStyleSheet("")
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.pushButton_register = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.pushButton_register.setGeometry(QtCore.QRect(670, 500, 111, 52))
        self.pushButton_register.setObjectName("pushButton_register")
        self.pushButtonCancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCancel.setGeometry(QtCore.QRect(520, 410, 131, 51))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 875, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("FPGA-opticalFiber", "细长光纤排列顺序检测助手"))
        self.label.setText(_translate("MainWindow", "   基于机器视觉的细长光纤排列顺序检测软件"))
        self.label_zh.setText(_translate("MainWindow", "账户："))
        self.label_mm.setText(_translate("MainWindow", "密码："))
        self.pushButtonOK.setText(_translate("MainWindow", "确定"))
        self.pushButton_register.setText(_translate("MainWindow", "注册"))
        self.pushButtonCancel.setText(_translate("MainWindow", "取消"))