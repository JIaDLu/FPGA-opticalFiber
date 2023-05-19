from log_in import Ui_MainWindow
from register import Example as register_ui
from PyQt5 import QtWidgets,QtCore
import sys
from inner_main import MyWindow
from PyQt5 import QtWidgets,QtCore
from PyMysql import *
from PyQt5.Qt import *

# 主窗口
class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    switch_window1 = QtCore.pyqtSignal() # 跳转信号
    switch_window2 = QtCore.pyqtSignal()  # 跳转信号
    switch_window3 = QtCore.pyqtSignal()
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_register.clicked.connect(self.goPic)
        self.pushButtonOK.clicked.connect(self.goapp)
        self.pushButtonCancel.clicked.connect(self.cancel_Log)
    def goPic(self):
        self.switch_window1.emit()
    def goapp(self):
        self.switch_window2.emit()
    def cancel_Log(self):
        self.switch_window3.emit()

# 图片识别窗口
class PicWindow(QtWidgets.QMainWindow, register_ui):
    switch_window5 = QtCore.pyqtSignal()  # 跳转信号
    def __init__(self):
        super(PicWindow, self).__init__()
        self.setui(self)
        self.pushButton_exit.clicked.connect(self.goPic_main)
    def goPic_main(self):
        self.switch_window5.emit()

# 图片识别窗口
class AppWindow(QtWidgets.QMainWindow, MyWindow):
    def __init__(self):
        super(AppWindow, self).__init__()

# 利用一个控制器来控制页面的跳转
class Controller1(QWidget):
    def __init__(self):
        super().__init__()
        self.reg = PicWindow()
        self.main = MainWindow()
        self.app = AppWindow()
        self.reg.hide()
        self.main.hide()
        self.app.hide()


    # 跳转到 main 窗口
    def show_main(self):
        self.main.show()
        self.main.switch_window1.connect(self.show_reg)
        self.main.switch_window2.connect(self.show_app)
        self.main.switch_window3.connect(self.cancel_Log)


    # # 跳转到 main 窗口
    def show_main_app(self):
        self.main.switch_window2.connect(self.show_app)

    # 跳转到 pic窗口
    def show_reg(self):
        self.main.close()
        self.reg.show()

    def cancel_Log(self):
        self.main.close()

    # 跳转到 pic窗口
    def show_app(self):
        usr_name = self.main.sr_zh.text()
        usr_pwd = self.main.sr_mm.text()
        #2 查询数据库，判定是否有匹配
        ms = MSSQL()
        table_name = 'client_info'
        args = ('acount', 'password')
        result = ms.query_super(table_name, args,usr_name,usr_pwd)
        if(result > 0):
            print("密码正确")
            QMessageBox.information(self, '消息', '登录成功')
            self.app.usr = usr_name
            self.app.show()
            self.main.close()
        else:
            print("密码错误")
            QMessageBox.warning(self,
                                "警告",
                                "用户名或密码错误！",
                                QMessageBox.Yes)
            self.main.sr_zh.setFocus()

# 控制器2，实现子界面返回主界面
class Controller2:
    def __init__(self, Con1):
        self.reg = Con1.reg
        self.main = Con1.main
    #pic窗口返回main窗口
    def show_pic_main(self):
        self.reg.switch_window5.connect(self.show_main_)
        self.reg.hide()
    # 显示main窗口
    def show_main_(self):
        self.reg.close()
        self.main.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller1 = Controller1()
    controller2 = Controller2(controller1)
    controller1.show_main()
    controller2.show_pic_main()
    sys.exit(app.exec_())