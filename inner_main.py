import sys
import threading

import inspect

import ctypes
import xlwt
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget, QApplication, QMainWindow, QDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import serial
import time
import datetime
import xlrd
import re
import win32api, win32con
from PyMysql import MSSQL
import cv2
import numpy as np
from fistPyQtWin import Ui_MainWindow
from commSetDlg import Ui_Dialog
from ImgSet import Ui_ImgDlg
from threading import Thread
from xiaweiji import xiaweiji_Ui_MainWindow
from get_work_data import get_Data_Ui_MainWindow

class MyWindow(Ui_MainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

        # 串口配置对话框成员
        self.childDlg = MyDlg()

        # HSV 参数设置
        self.tip_QView = [self.fiber0,self.fiber1,self.fiber2,self.fiber3,self.fiber4,self.fiber5,self.fiber6,self.fiber7,self.fiber8,
                          self.fiber9,self.fiber10,self.fiber11,self.fiber12,self.fiber13,self.fiber14,self.fiber15,self.fiber16,self.fiber17,
                          self.fiber18,self.fiber19,self.fiber20,self.fiber21,self.fiber22,self.fiber23,self.fiber24,self.fiber25,self.fiber26,
                          self.fiber27,self.fiber28,self.fiber29,self.fiber30,self.fiber31,self.fiber32,self.fiber33,self.fiber34,self.fiber35]

        self.img_dlg = ImgSetDlg()
        self.link_xiaweiji_setui = Link_xiaweijie_SetDlg()
        self.show_Work_data_infomation = show_Get_data_windows()
        self.df = {}

        self.fiber_work_info = []
        self.start_time = ''
        self.usr = ''
        self.fiber_number = ''
        self.Notes = ''
        self.work_line_info = []
        self.mysql = MSSQL()

        self.mark = 0

        # 设备启停成员
        self.dev_stop = 0

        #急停的标志
        self.stop_mark = 0

        self.btn_start.clicked.connect(self.btn_start_func)
        self.btn_stop.clicked.connect(self.fake_btn_stop_func)
        self.pushButton_communicate_setting.clicked.connect(self.com_config)
        # self.img_set_menu.triggered.connect(self.img_set)
        self.ComConfigAction.triggered.connect(self.show_work_data_)
        self.pushButton_img_setting.clicked.connect(self.img_set)
        self.pushButton_link_xiaweiji.clicked.connect(self.link_xiaweiji_ui)

    def _async_raise(self, tid, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")

    def stop_thread(self, thread):
        self._async_raise(thread.ident, SystemExit)

    def fake_btn_stop_func(self):
        self.stop_thread(self.thread_start_btn)
        QMessageBox.information(self, '消息', '检测已紧急停止')
        self.mark = 1

    def btn_start_func(self):  # pushbutton对应的响应函数
        #先将标记还原
        self.label_zh_qr.setText('*')
        self.label_mm_qr.setText('*')
        self.label_qmm_qr.setText('*')

        if self.pushButton_communicate_setting.text() != '通讯设置已完成':
            self.label_zh_qr.setText('串口通信为空')

        elif self.pushButton_link_xiaweiji.text() != '下位机连接已完成':
            self.label_mm_qr.setText('未连接下位机')

        elif self.pushButton_img_setting.text() != '图像参数设置已完成':
            self.label_qmm_qr.setText('图像参数为空')
        else:
            if self.mark == 0:
                QMessageBox.information(self, '消息', '正式开始工作')
                self.infoLineEdit.append("检测进行中……")
                self.thread_start_btn = Thread(target=self.fake_start_func)
                self.thread_start_btn.start()
            else:
                self.infoLineEdit.clear()
                for num in range(len(self.tip_QView)):
                    self.tip_QView[num].setStyleSheet("background-color: rgb(85, 170, 255);")
                self.lcdNumber.display(0)
                self.fiber_work_info = []
                self.work_line_info = []
                QMessageBox.information(self, '消息', '已为您更新数据，检测继续')
                self.infoLineEdit.append("检测进行中……")
                self.thread_start_btn = Thread(target=self.fake_start_func)
                self.thread_start_btn.start()


    def fake_start_func(self):
        now = datetime.datetime.now()
        self.start_time = now.strftime("%Y-%m-%d %H:%M:%S")
        self.fiber_number = self.comboBox.currentText()
        self.Notes = self.textEdit.toPlainText()
        '''读入txt文档'''
        f = open("./fake_data.txt", "r", encoding='UTF-8')
        lines = f.readlines()
        time.sleep(2)
        aaa = 0
        number = 0
        for numbe,line in enumerate(lines):
            line = str(line)
            if "未通过" in line:
                self.work_line_info.append(line)
                self.infoLineEdit.append(line)
                self.tip_QView[aaa].setStyleSheet("\n"
                                                  "background-color: rgb(235, 77, 75);")
                aaa = aaa + 1
                time.sleep(1)
            else:
                number = number + 1
                self.work_line_info.append(line)
                self.infoLineEdit.append(line)
                self.lcdNumber.display(number)
                self.tip_QView[aaa].setStyleSheet("\n"
                                                  "background-color: rgb(0, 255, 0);")
                aaa = aaa + 1
                time.sleep(1)
        self.infoLineEdit.append("检测结束！")
        win32api.MessageBox(0, "检测结束", "消息")
        self.btn_start.setStyleSheet("background-color: rgb(205, 205, 255);font-size:24px;color:blue")
        self.btn_start.setText('继续检测')
        self.fiber_work_info.append(self.start_time)
        self.fiber_work_info.append(self.usr)
        self.fiber_work_info.append(self.fiber_number)
        self.fiber_work_info.append(self.Notes)
        for i in self.work_line_info:
            self.fiber_work_info.append(i)
        print(tuple(self.fiber_work_info))
        self.mysql.insert_fiber_work_info_db(tuple(self.fiber_work_info))
        self.mark = 1


    #####################################
    def com_config(self):
        self.childDlg.show()
        self.childDlg.switch_window1.connect(self.modify_pu_com_set_CSS)
        self.childDlg.switch_window2.connect(self.close_childDlg)
        if self.childDlg.exec_():
            self.dlgText = self.childDlg.text
            self.dlgSerialNum = self.childDlg.serialNum
            print(self.dlgText)
            print(self.dlgSerialNum)

    def close_childDlg(self):
        self.childDlg.close()

    def modify_pu_com_set_CSS(self):
        self.pushButton_communicate_setting.setStyleSheet("\n"
        "background-color: rgb(245, 205, 121);")
        self.pushButton_communicate_setting.setText('通讯设置已完成')
        if self.label_zh_qr.text() != '*':
            self.label_zh_qr.setText('*')
        # reply = QMessageBox.information(self,'提示',self.dlgText, QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)


    def show_work_data_(self):
        self.show_Work_data_infomation.show()
        result = self.mysql.get_work_data_info()
        # print(result[0])
        dict = {}
        for number,i in enumerate(result):
            dict[number] = i
        self.df = pd.DataFrame(dict)
        model = PdTable(self.df)
        view = self.show_Work_data_infomation.tableView
        view.setModel(model)

        self.show_Work_data_infomation.D_switch_window1.connect(self.setBrowerPath)
        self.show_Work_data_infomation.D_switch_window2.connect(self.savefile)

    def setBrowerPath(self):  # 选择文件夹进行存储
        download_path = QtWidgets.QFileDialog.getExistingDirectory(None, "浏览", "/home")
        self.show_Work_data_infomation.lineEdit.setText(download_path)

    def savefile(self):
        if len(self.show_Work_data_infomation.lineEdit_2.text()) < 1:
            QMessageBox.information(self.show_Work_data_infomation.pushButton, ' ', '文件名不可为空', QMessageBox.Ok)
        else:
            try:
                self.df.to_csv(self.show_Work_data_infomation.lineEdit.text() + '/' + self.show_Work_data_infomation.lineEdit_2.text() + '.csv')
                QMessageBox.information(self, '消息', '已保存到指定路径')
                self.show_Work_data_infomation.close()
            except:
                QMessageBox.information(self.show_Work_data_infomation.pushButton, ' ', '所选目录错误！', QMessageBox.Ok)


    def link_xiaweiji_ui(self):
        self.link_xiaweiji_setui.show()
        self.link_xiaweiji_setui.L_switch_window1.connect(self.modify_pu_Link_s_CSS)
        self.link_xiaweiji_setui.L_switch_window2.connect(self.close_Link_dlg)

    def modify_pu_Link_s_CSS(self):
        self.pushButton_link_xiaweiji.setStyleSheet("\n"
        "background-color: rgb(245, 205, 121);")
        self.pushButton_link_xiaweiji.setText('下位机连接已完成')
        if self.label_mm_qr.text() != '*':
            self.label_mm_qr.setText('*')

    def close_Link_dlg(self):
        self.link_xiaweiji_setui.close()


    def img_set(self):
        self.img_dlg.show()
        self.img_dlg.switch_window1.connect(self.modify_pu_img_s_CSS)
        self.img_dlg.switch_window2.connect(self.close_img_dlg)
        # if self.img_dlg.exec_():
        #     self.h_min_val = int(self.img_dlg.h_min)
        #     self.h_max_val = int(self.img_dlg.h_max)
        #     self.s_min_val = int(self.img_dlg.s_min)
        #     self.s_max_val = int(self.img_dlg.s_max)
        #     self.v_min_val = int(self.img_dlg.v_min)
        #     self.v_max_val = int(self.img_dlg.v_max)
        #     self.min_noise_val = int(self.img_dlg.min_noise)
        #     self.dist_noise2fiber_line = int(self.img_dlg.dist_noise2fiber_line)
        #     self.fiber_total = int(self.img_dlg.fiber_cnt)


    def modify_pu_img_s_CSS(self):
        self.pushButton_img_setting.setStyleSheet("\n"
        "background-color: rgb(245, 205, 121);")
        self.pushButton_img_setting.setText('图像参数设置已完成')
        if self.label_qmm_qr.text() != '*':
            self.label_qmm_qr.setText('*')

    def close_img_dlg(self):
        self.img_dlg.close()


class MyDlg(QDialog, Ui_Dialog):
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(MyDlg, self).__init__(parent)
        self.text = '9600'
        self.serialNum = '1'
        self.__index = 0
        self.setupUi(self)

        self.pushButtonOK.clicked.connect(self.data_accept)
        self.pushButtoncancle.clicked.connect(self.close_img_set)

        self.textEdit.setText("9600")
        self.lineEdit.setText('1')

    def close_img_set(self):
        self.switch_window2.emit()

    def data_accept(self):
        QMessageBox.information(self, '消息', '设置成功')
        self.goPic()
        self.text = self.textEdit.toPlainText()
        self.serialNum = self.lineEdit.text()

    def goPic(self):
        self.switch_window1.emit()

class Link_xiaweijie_SetDlg(QMainWindow, xiaweiji_Ui_MainWindow):
    L_switch_window1 = QtCore.pyqtSignal()
    L_switch_window2 = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(Link_xiaweijie_SetDlg, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit.setText("1号下位机")

        self.pushButton.clicked.connect(self.Link_xieweiji_func)
        self.pushButton_2.clicked.connect(self.close_Link_set)

    def Link_xieweiji_func(self):
        QMessageBox.information(self, '消息', '连接成功')
        self.goPic()

    def goPic(self):
        self.L_switch_window1.emit()

    def close_Link_set(self):
        self.L_switch_window2.emit()


class show_Get_data_windows(QMainWindow, get_Data_Ui_MainWindow):
    D_switch_window1 = QtCore.pyqtSignal()
    D_switch_window2 = QtCore.pyqtSignal()
    def __init__(self,parent=None):
        super(show_Get_data_windows, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Send_Signal_1)
        self.pushButton_2.clicked.connect(self.Send_Signal_2)

    def Send_Signal_1(self):
        self.D_switch_window1.emit()

    def Send_Signal_2(self):
        self.D_switch_window2.emit()



class ImgSetDlg(QDialog, Ui_ImgDlg):
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(ImgSetDlg, self).__init__(parent)
        self.h_min = 0  # 80
        self.h_max = 255  # 180
        self.s_min = 0  # 170
        self.s_max = 255  # 255
        self.v_min = 0  # 0
        self.v_max = 255  # 85
        self.min_noise = 2
        self.dist_noise2fiber_line = 6
        self.fiber_cnt = 36
        self.setupUi(self)

        self.pushButtonOK.clicked.connect(self.img_data_accept)
        self.pushButtoncancle.clicked.connect(self.close_img_set)
        # print(self.h_min)

    def close_img_set(self):
        self.switch_window2.emit()

    def img_data_accept(self):
        QMessageBox.information(self, '消息', '设置成功')
        self.goPic()
        self.h_min = self.HDWlineEdit.text()
        self.h_max = self.HUPlineEdit.text()
        self.s_min = self.SDWlineEdit.text()
        self.s_max = self.SUPlineEdit.text()
        self.v_min = self.VDWlineEdit.text()
        self.v_max = self.VUPlineEdit.text()
        self.min_noise = self.MinstNoiseAreaLineEdit.text()
        self.fiber_cnt = self.FiberCntLineEdit.text()
        self.dist_noise2fiber_line = self.DistNoiseArea2FiberLineEdit.text()

    def goPic(self):
        self.switch_window1.emit()

    # def close_imgSet(self):
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class PdTable(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    # 显示数据
    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    # 显示行和列头
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._data.axes[0][col]
        return None



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

