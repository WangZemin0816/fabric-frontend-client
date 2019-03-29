#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 教程
在这个例子中, 我们用PyQt5创建了一个简单的窗口。

作者: Jan Bodnar
网站: zetcode.com
最后一次编辑: January 2015
"""
from view.texture.edit import EditTextureDialog
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # http.print()
    # response = login_service.login("111","111",False)
    # print(response.content.decode('utf-8'))
    loginDialog = EditTextureDialog()
    loginDialog.show()
    sys.exit(app.exec_())