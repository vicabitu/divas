# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuprincipal.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_menuprincipal(object):
    def setupUi(self, menuprincipal):
        menuprincipal.setObjectName("menuprincipal")
        menuprincipal.setWindowModality(QtCore.Qt.WindowModal)
        menuprincipal.resize(657, 416)
        menuprincipal.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(menuprincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 300, 151, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../imagenes/divas_logo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        menuprincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(menuprincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 25))
        self.menubar.setDefaultUp(True)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menu_clientes = QtWidgets.QMenu(self.menubar)
        self.menu_clientes.setSeparatorsCollapsible(False)
        self.menu_clientes.setObjectName("menu_clientes")
        self.menu_turnos = QtWidgets.QMenu(self.menubar)
        self.menu_turnos.setObjectName("menu_turnos")
        self.menu_servicios = QtWidgets.QMenu(self.menubar)
        self.menu_servicios.setObjectName("menu_servicios")
        menuprincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(menuprincipal)
        self.statusbar.setObjectName("statusbar")
        menuprincipal.setStatusBar(self.statusbar)
        self.action_alta_Cliente = QtWidgets.QAction(menuprincipal)
        self.action_alta_Cliente.setObjectName("action_alta_Cliente")
        self.action_baja_Cliente = QtWidgets.QAction(menuprincipal)
        self.action_baja_Cliente.setObjectName("action_baja_Cliente")
        self.action_nuevo_turno = QtWidgets.QAction(menuprincipal)
        self.action_nuevo_turno.setObjectName("action_nuevo_turno")
        self.action_alta_servicio = QtWidgets.QAction(menuprincipal)
        self.action_alta_servicio.setObjectName("action_alta_servicio")
        self.action_modificacion_cliente = QtWidgets.QAction(menuprincipal)
        self.action_modificacion_cliente.setObjectName("action_modificacion_cliente")
        self.action_modificacion_servicio = QtWidgets.QAction(menuprincipal)
        self.action_modificacion_servicio.setObjectName("action_modificacion_servicio")
        self.menu_clientes.addAction(self.action_alta_Cliente)
        self.menu_clientes.addAction(self.action_baja_Cliente)
        self.menu_clientes.addAction(self.action_modificacion_cliente)
        self.menu_turnos.addAction(self.action_nuevo_turno)
        self.menu_servicios.addAction(self.action_alta_servicio)
        self.menu_servicios.addAction(self.action_modificacion_servicio)
        self.menubar.addAction(self.menu_clientes.menuAction())
        self.menubar.addAction(self.menu_servicios.menuAction())
        self.menubar.addAction(self.menu_turnos.menuAction())

        self.retranslateUi(menuprincipal)
        QtCore.QMetaObject.connectSlotsByName(menuprincipal)

    def retranslateUi(self, menuprincipal):
        _translate = QtCore.QCoreApplication.translate
        menuprincipal.setWindowTitle(_translate("menuprincipal", "Divas"))
        self.menu_clientes.setTitle(_translate("menuprincipal", "Clientes"))
        self.menu_turnos.setTitle(_translate("menuprincipal", "Turnos"))
        self.menu_servicios.setTitle(_translate("menuprincipal", "Servicios"))
        self.action_alta_Cliente.setText(_translate("menuprincipal", "Alta"))
        self.action_baja_Cliente.setText(_translate("menuprincipal", "Baja"))
        self.action_nuevo_turno.setText(_translate("menuprincipal", "Nuevo turno"))
        self.action_alta_servicio.setText(_translate("menuprincipal", "Alta"))
        self.action_modificacion_cliente.setText(_translate("menuprincipal", "Modificacion"))
        self.action_modificacion_servicio.setText(_translate("menuprincipal", "Modificacion"))

