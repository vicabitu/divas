# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_listado_clientes.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ListadoClientes(object):
    def setupUi(self, ListadoClientes):
        ListadoClientes.setObjectName("ListadoClientes")
        ListadoClientes.resize(701, 332)
        self.listView = QtWidgets.QListView(ListadoClientes)
        self.listView.setGeometry(QtCore.QRect(10, 60, 631, 192))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(ListadoClientes)
        self.label.setGeometry(QtCore.QRect(30, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(ListadoClientes)
        QtCore.QMetaObject.connectSlotsByName(ListadoClientes)

    def retranslateUi(self, ListadoClientes):
        _translate = QtCore.QCoreApplication.translate
        ListadoClientes.setWindowTitle(_translate("ListadoClientes", "Listado Clientes"))
        self.label.setText(_translate("ListadoClientes", "Listado clientes"))

