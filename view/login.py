# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QRect
from PyQt5.QtCore import pyqtSlot
from service.login_service import login
"""
用户登录对话框
"""


class LoginDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__initUI()

    def __initUI(self):
        self.setModal(True)
        self.setWindowTitle('用户登录')
        self.resize(400, 300)  # set dialog size to 400*300
        self.__addUsernameComponent()
        self.__addPasswordComponent()
        self.__addLoginButton()
        self.__addCancelButton()
        pass

    # 添加用户登录信息的组件
    def __addUsernameComponent(self):
        self.label_username = QLabel("用户名:", self)
        self.label_username.setGeometry(QRect(70, 40, 50, 20))
        self.lineEdit_username = QLineEdit(self)
        self.lineEdit_username.setGeometry(QRect(120, 40, 150, 20))

    def __addPasswordComponent(self):
        self.label_password = QLabel("密码:", self)
        self.label_password.setGeometry(QRect(70, 100, 50, 20))
        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setGeometry(QRect(120, 100, 150, 20))

    def __addLoginButton(self):
        self.pushButton_login = QPushButton("登录",self)
        self.pushButton_login.setGeometry(QRect(80, 150, 80, 20))
        self.pushButton_login.setToolTip("用户点击登录")
        self.pushButton_login.clicked.connect(self.__clickLogin)

    def __addCancelButton(self):
        self.pushButton_cancel = QPushButton("取消",self)
        self.pushButton_cancel.setGeometry(QRect(180, 150, 80, 20))
        self.pushButton_cancel.clicked.connect(self.__clickCancel)


    def __clickLogin(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        remember_me = False
        resp=login_service.login(username,password,remember_me)
        print(resp.content)


    def __clickCancel(self):
        self.destroy()
