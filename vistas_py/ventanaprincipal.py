# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaprincipal.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ventanaprincipal(object):
    def setupUi(self, ventanaprincipal):
        ventanaprincipal.setObjectName("ventanaprincipal")
        ventanaprincipal.resize(525, 350)
        self.label = QtWidgets.QLabel(ventanaprincipal)
        self.label.setGeometry(QtCore.QRect(170, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(ventanaprincipal)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 121, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_alta_cliente = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_alta_cliente.setObjectName("btn_alta_cliente")
        self.verticalLayout.addWidget(self.btn_alta_cliente)
        self.btn_alta_servicio = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_alta_servicio.setObjectName("btn_alta_servicio")
        self.verticalLayout.addWidget(self.btn_alta_servicio)
        self.btn_alta_turno = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_alta_turno.setObjectName("btn_alta_turno")
        self.verticalLayout.addWidget(self.btn_alta_turno)
        self.label_2 = QtWidgets.QLabel(ventanaprincipal)
        self.label_2.setGeometry(QtCore.QRect(160, 60, 351, 221))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../imagenes/saloncentro.jpg"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(ventanaprincipal)
        QtCore.QMetaObject.connectSlotsByName(ventanaprincipal)

    def retranslateUi(self, ventanaprincipal):
        _translate = QtCore.QCoreApplication.translate
        ventanaprincipal.setWindowTitle(_translate("ventanaprincipal", "Divas"))
        self.label.setText(_translate("ventanaprincipal", "Divas Proyect"))
        self.btn_alta_cliente.setText(_translate("ventanaprincipal", "Alta Cliente"))
        self.btn_alta_servicio.setText(_translate("ventanaprincipal", "Alta Servicio"))
        self.btn_alta_turno.setText(_translate("ventanaprincipal", "Alta Turno"))

