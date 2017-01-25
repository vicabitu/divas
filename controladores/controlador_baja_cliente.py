"""
Esta clase representa el controlador de la vista form_alta_cliente
"""

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QWidget, QPushButton
from vistas_py.form_baja_cliente import Ui_BajaCLiente
from modelo.modelo import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class ControladorBajaCliente(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 messagebox - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

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

        if self.form_baja_cliente.text_nombre.text() == "" or self.form_baja_cliente.text_apellido.text() == "":
            QMessageBox.information(self, "Campos incompletos", "Debe completar todos los campos.")
        else:
            nombre = str(self.form_baja_cliente.text_nombre.text())
            apellido = str(self.form_baja_cliente.text_apellido.text())

            cliente_base = session.query(Cliente).filter(Cliente.nombre == nombre, Cliente.apellido == apellido).first()
            print(cliente_base)

            if cliente_base != None:
                buttonReply = QMessageBox.question(self, 'Mensaje', "¿esta seguro que desea elimnar al cliente?",
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    session.delete(cliente_base)
                    session.commit()
                    self.close()
                else:
                    self.close()
            else:
                print("El cliente existe")
                QMessageBox.information(self, "Error",
                                        "El cliente no existe, intente ingresarlo nuevamente.")