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

        if self.form_alta_cliente.text_nombre.text() == "" or self.form_alta_cliente.text_apellido.text() == "":
            QMessageBox.information(self, "Campos incompletos", "Debe completar todos los campos.")
        else:
            nombre = str(self.form_alta_cliente.text_nombre.text())
            apellido = str(self.form_alta_cliente.text_apellido.text())

            cliente_base = session.query(Cliente).filter(Cliente.nombre == nombre, Cliente.apellido == apellido).first()
            print(cliente_base)

            if cliente_base == None:
                cliente = Cliente(nombre, apellido)
                session.add(cliente)
                session.commit()
                self.close()
            else:
                print("El cliente existe")
                QMessageBox.information(self, "Error",
                                        "El cliente ya existe, intente darlo de alta nuevamente.")