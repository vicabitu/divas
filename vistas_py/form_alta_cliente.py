# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_alta_cliente.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AltaCLiente(object):
    def setupUi(self, AltaCLiente):
        AltaCLiente.setObjectName("AltaCLiente")
        AltaCLiente.resize(616, 300)
        self.label_alta_cliente = QtWidgets.QLabel(AltaCLiente)
        self.label_alta_cliente.setGeometry(QtCore.QRect(20, 20, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_alta_cliente.setFont(font)
        self.label_alta_cliente.setObjectName("label_alta_cliente")
        self.horizontalLayoutWidget = QtWidgets.QWidget(AltaCLiente)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 190, 301, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_guardar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_guardar.setObjectName("btn_guardar")
        self.horizontalLayout.addWidget(self.btn_guardar)
        self.btn_cancelar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout.addWidget(self.btn_cancelar)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(AltaCLiente)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 50, 331, 130))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_nombre = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_nombre.setFont(font)
        self.label_nombre.setObjectName("label_nombre")
        self.verticalLayout_2.addWidget(self.label_nombre)
        self.label_apellido = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_apellido.setFont(font)
        self.label_apellido.setObjectName("label_apellido")
        self.verticalLayout_2.addWidget(self.label_apellido)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.text_nombre = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.text_nombre.setText("")
        self.text_nombre.setObjectName("text_nombre")
        self.verticalLayout_3.addWidget(self.text_nombre)
        self.text_apellido = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.text_apellido.setObjectName("text_apellido")
        self.verticalLayout_3.addWidget(self.text_apellido)
        self.text_dni = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.text_dni.setObjectName("text_dni")
        self.verticalLayout_3.addWidget(self.text_dni)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.label_2 = QtWidgets.QLabel(AltaCLiente)
        self.label_2.setGeometry(QtCore.QRect(370, 30, 221, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../imagenes/cliente.png"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(AltaCLiente)
        QtCore.QMetaObject.connectSlotsByName(AltaCLiente)

    def retranslateUi(self, AltaCLiente):
        _translate = QtCore.QCoreApplication.translate
        AltaCLiente.setWindowTitle(_translate("AltaCLiente", "Alta Cliente."))
        self.label_alta_cliente.setText(_translate("AltaCLiente", "Alta Cliente"))
        self.btn_guardar.setText(_translate("AltaCLiente", "Guardar"))
        self.btn_cancelar.setText(_translate("AltaCLiente", "Cancelar"))
        self.label_nombre.setText(_translate("AltaCLiente", "Nombre:"))
        self.label_apellido.setText(_translate("AltaCLiente", "Apellido:"))
        self.label.setText(_translate("AltaCLiente", "Dni"))

