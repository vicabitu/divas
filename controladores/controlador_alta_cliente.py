"""
Esta clase representa el controlador de la vista form_alta_cliente
"""

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from vistas_py.form_alta_cliente import Ui_AltaCLiente
from modelo.modelo import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class ControladorAltaCliente(QDialog):

    def __init__(self):
        super(ControladorAltaCliente, self).__init__()
        self.form_alta_cliente = Ui_AltaCLiente()
        self.form_alta_cliente.setupUi(self)

        self.form_alta_cliente.btn_guardar.clicked.connect(self.guardar_cliente)
        self.form_alta_cliente.btn_cancelar.clicked.connect(self.close)

    def guardar_cliente(self):

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