# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_listado_servicios.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(668, 535)
        self.list_widget_servicios = QtWidgets.QListWidget(Dialog)
        self.list_widget_servicios.setGeometry(QtCore.QRect(10, 10, 641, 451))
        self.list_widget_servicios.setObjectName("list_widget_servicios")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 470, 311, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_cancelar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout.addWidget(self.btn_cancelar)
        self.btn_modificar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_modificar.setObjectName("btn_modificar")
        self.horizontalLayout.addWidget(self.btn_modificar)
        self.btn_eliminar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.horizontalLayout.addWidget(self.btn_eliminar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Listar Servicios"))
        self.btn_cancelar.setText(_translate("Dialog", "Cancelar"))
        self.btn_modificar.setText(_translate("Dialog", "Modifcar"))
        self.btn_eliminar.setText(_translate("Dialog", "Eliminar"))

