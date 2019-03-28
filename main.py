#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 教程
在这个例子中, 我们用PyQt5创建了一个简单的窗口。

作者: Jan Bodnar
网站: zetcode.com
最后一次编辑: January 2015
"""
import login
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog

if __name__ == '__main__':
    app = QApplication(sys.argv)

    loginDialog = login.LoginDialog()
    loginDialog.show()
    sys.exit(app.exec_())