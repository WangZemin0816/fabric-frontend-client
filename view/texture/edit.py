# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap


class EditTextureDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__initUI()

    def __initUI(self):
        self.setWindowTitle('编辑纹理图')
        self.resize(400, 450)  # set dialog size to 400*300
        self.__addTextureLabel()
        self.__addSelectTextureButton()

    def __addTextureLabel(self):
        self.label_texture = QLabel("当前图片为空", self)
        self.label_texture.setGeometry(QRect(10,10, 380, 380))

    def __addSelectTextureButton(self):
        self.pushButton_select_texture = QPushButton("选取原始图片",self)
        self.pushButton_select_texture.setGeometry(QRect(200, 420, 80, 20))
        self.pushButton_select_texture.clicked.connect(self.__clickSelectTexture)

    def __clickSelectTexture(self):
        texture_path = QFileDialog.getOpenFileName(self, "OpenFile", ".","Image Files(*.jpg *.jpeg *.png)")[0]
        texture = QPixmap(texture_path).scaled(self.label_texture.width(),self.label_texture.height())
        self.label_texture.setPixmap(texture)
