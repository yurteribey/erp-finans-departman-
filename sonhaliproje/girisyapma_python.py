# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'girisyapma.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(581, 548)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 90, 501, 391))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 120, 161, 41))
        self.label.setObjectName("label")
        self.lneEditkullanici = QtWidgets.QLineEdit(self.groupBox)
        self.lneEditkullanici.setGeometry(QtCore.QRect(222, 131, 231, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lneEditkullanici.setFont(font)
        self.lneEditkullanici.setText("")
        self.lneEditkullanici.setObjectName("lneEditkullanici")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 190, 141, 31))
        self.label_2.setObjectName("label_2")
        self.lneEditsifre = QtWidgets.QLineEdit(self.groupBox)
        self.lneEditsifre.setGeometry(QtCore.QRect(220, 200, 231, 22))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lneEditsifre.setFont(font)
        self.lneEditsifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lneEditsifre.setObjectName("lneEditsifre")
        self.btngiris = QtWidgets.QPushButton(self.groupBox)
        self.btngiris.setGeometry(QtCore.QRect(160, 290, 191, 41))
        self.btngiris.setObjectName("btngiris")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "FİNANSAL İŞLEMLER"))
        self.label.setText(_translate("Form", "Kullanıcı Adı:"))
        self.label_2.setText(_translate("Form", "Şifre : "))
        self.btngiris.setText(_translate("Form", "Giriş Yap"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())