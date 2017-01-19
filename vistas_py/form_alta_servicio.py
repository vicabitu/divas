# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_alta_servicio.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_altaservicio(object):
    def setupUi(self, altaservicio):
        altaservicio.setObjectName("altaservicio")
        altaservicio.resize(510, 264)
        self.label = QtWidgets.QLabel(altaservicio)
        self.label.setGeometry(QtCore.QRect(30, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(altaservicio)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 60, 331, 101))
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
        self.label_precio = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_precio.setFont(font)
        self.label_precio.setObjectName("label_precio")
        self.verticalLayout_2.addWidget(self.label_precio)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.text_nombre = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.text_nombre.setText("")
        self.text_nombre.setObjectName("text_nombre")
        self.verticalLayout_3.addWidget(self.text_nombre)
        self.text_precio = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.text_precio.setObjectName("text_precio")
        self.verticalLayout_3.addWidget(self.text_precio)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(altaservicio)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 180, 301, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_guardar = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.btn_guardar.setObjectName("btn_guardar")
        self.horizontalLayout_3.addWidget(self.btn_guardar)
        self.btn_cancelar = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout_3.addWidget(self.btn_cancelar)
        self.label_2 = QtWidgets.QLabel(altaservicio)
        self.label_2.setGeometry(QtCore.QRect(370, 30, 111, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../imagenes/alta_servicio.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(altaservicio)
        QtCore.QMetaObject.connectSlotsByName(altaservicio)

    def retranslateUi(self, altaservicio):
        _translate = QtCore.QCoreApplication.translate
        altaservicio.setWindowTitle(_translate("altaservicio", "Alta Servicio."))
        self.label.setText(_translate("altaservicio", "Alta Serivicio"))
        self.label_nombre.setText(_translate("altaservicio", "Nombre:"))
        self.label_precio.setText(_translate("altaservicio", "Precio:"))
        self.btn_guardar.setText(_translate("altaservicio", "Guardar"))
        self.btn_cancelar.setText(_translate("altaservicio", "Cancelar"))

