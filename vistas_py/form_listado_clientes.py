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
        ListadoClientes.resize(756, 340)
        self.label_titulo = QtWidgets.QLabel(ListadoClientes)
        self.label_titulo.setGeometry(QtCore.QRect(20, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_titulo.setFont(font)
        self.label_titulo.setObjectName("label_titulo")
        self.layoutWidget = QtWidgets.QWidget(ListadoClientes)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 58, 621, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.list_widget_clientes = QtWidgets.QListWidget(self.layoutWidget)
        self.list_widget_clientes.setObjectName("list_widget_clientes")
        self.verticalLayout.addWidget(self.list_widget_clientes)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_salir = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_salir.setObjectName("btn_salir")
        self.horizontalLayout.addWidget(self.btn_salir)
        self.btn_eliminar = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.horizontalLayout.addWidget(self.btn_eliminar)
        self.btn_modificar = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_modificar.setObjectName("btn_modificar")
        self.horizontalLayout.addWidget(self.btn_modificar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.btn_actualizar = QtWidgets.QPushButton(ListadoClientes)
        self.btn_actualizar.setGeometry(QtCore.QRect(640, 70, 101, 27))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagenes/actualizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_actualizar.setIcon(icon)
        self.btn_actualizar.setIconSize(QtCore.QSize(17, 17))
        self.btn_actualizar.setObjectName("btn_actualizar")

        self.retranslateUi(ListadoClientes)
        QtCore.QMetaObject.connectSlotsByName(ListadoClientes)

    def retranslateUi(self, ListadoClientes):
        _translate = QtCore.QCoreApplication.translate
        ListadoClientes.setWindowTitle(_translate("ListadoClientes", "Listado Clientes"))
        self.label_titulo.setText(_translate("ListadoClientes", "Listado clientes"))
        self.btn_salir.setText(_translate("ListadoClientes", "Salir"))
        self.btn_eliminar.setText(_translate("ListadoClientes", "Eliminar"))
        self.btn_modificar.setText(_translate("ListadoClientes", "Modificar"))
        self.btn_actualizar.setText(_translate("ListadoClientes", "Actualizar"))

