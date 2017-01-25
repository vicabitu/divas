"""
Esta clase representa el controlador de la vista form_alta_cliente
"""

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from vistas_py.form_baja_cliente import Ui_BajaCLiente
from modelo.modelo import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class ControladorBajaCliente(QDialog):

    def __init__(self):
        super(ControladorBajaCliente, self).__init__()
        self.form_baja_cliente = Ui_BajaCLiente()
        self.form_baja_cliente.setupUi(self)

        self.form_baja_cliente.btn_eliminar.clicked.connect(self.eliminar_cliente)
        self.form_baja_cliente.btn_cancelar.clicked.connect(self.close)

    def eliminar_cliente(self):

        #conexion
        engine = create_engine('sqlite:///divas.db', echo=True)

        # sesion
        Session = sessionmaker(bind=engine)
        session = Session()

