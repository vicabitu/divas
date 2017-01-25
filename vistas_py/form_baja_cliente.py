# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_baja_cliente.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BajaCLiente(object):
    def setupUi(self, BajaCLiente):
        BajaCLiente.setObjectName("BajaCLiente")
        BajaCLiente.resize(616, 303)
        self.label_alta_cliente = QtWidgets.QLabel(BajaCLiente)
        self.label_alta_cliente.setGeometry(QtCore.QRect(20, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_alta_cliente.setFont(font)
        self.label_alta_cliente.setObjectName("label_alta_cliente")
        self.horizontalLayoutWidget = QtWidgets.QWidget(BajaCLiente)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 190, 301, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_eliminar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.horizontalLayout.addWidget(self.btn_eliminar)
        self.btn_cancelar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout.addWidget(self.btn_cancelar)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(BajaCLiente)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 50, 331, 130))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.label_imagen = QtWidgets.QLabel(BajaCLiente)
        self.label_imagen.setGeometry(QtCore.QRect(350, 50, 271, 201))
        self.label_imagen.setText("")
        self.label_imagen.setPixmap(QtGui.QPixmap("../imagenes/e743b83c54a9e43194143cd3bd23a87e.png"))
        self.label_imagen.setScaledContents(True)
        self.label_imagen.setObjectName("label_imagen")

        self.retranslateUi(BajaCLiente)
        QtCore.QMetaObject.connectSlotsByName(BajaCLiente)

    def retranslateUi(self, BajaCLiente):
        _translate = QtCore.QCoreApplication.translate
        BajaCLiente.setWindowTitle(_translate("BajaCLiente", "Alta Cliente."))
        self.label_alta_cliente.setText(_translate("BajaCLiente", "Baja Cliente"))
        self.btn_eliminar.setText(_translate("BajaCLiente", "Eliminar"))
        self.btn_cancelar.setText(_translate("BajaCLiente", "Cancelar"))
        self.label_nombre.setText(_translate("BajaCLiente", "Nombre:"))
        self.label_apellido.setText(_translate("BajaCLiente", "Apellido:"))

