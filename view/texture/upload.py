# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QRect
from service.texture_service import texture
import json
class UploadTextureDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__initUI()


    def __initUI(self):
        self.setWindowTitle('上传纹理图')
        self.resize(400, 400)  # set dialog size to 400*300
        self.__addNameComponent()
        self.__addSelectOriginButton()
        pass

    # 添加图片名称组件
    def __addNameComponent(self):
        self.label_name = QLabel("图片名称:", self)
        self.label_name.setGeometry(QRect(70, 40, 50, 20))
        self.lineEdit_name = QLineEdit(self)
        self.lineEdit_name.setGeometry(QRect(120, 40, 150, 20))

    def __addSelectOriginButton(self):
        self.pushButton_select_origin = QPushButton("选取原始图片",self)
        self.pushButton_select_origin.setGeometry(QRect(180, 150, 80, 20))
        self.pushButton_select_origin.clicked.connect(self.__clickSelectOrigin)

    def __clickSelectOrigin(self):
        self.origin_path =QFileDialog.getOpenFileName(self,'选取原始纹理图','.','Image Files(*.jpg *.png)')

        origin = open(self.origin_path[0], 'rb')
        division = open(self.origin_path[0], 'rb')
        imgInfo={}
        imgInfo['name']='11111111'
        resp=texture.upload(imgInfo,origin,division)
        origin.close()
        division.close()
        print(self.origin_path)

