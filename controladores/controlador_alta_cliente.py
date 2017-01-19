"""
Esta clase representa el controlador de la vista form_alta_cliente
"""

from PyQt5.QtWidgets import QApplication, QDialog
from vistas_py.form_alta_cliente import Ui_AltaCLiente
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelo.modelo import Cliente

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

        nombre = str(self.form_alta_cliente.text_nombre.text())
        apellido = str(self.form_alta_cliente.text_apellido.text())

        cliente_base = session.query(Cliente).filter(Cliente.nombre == nombre).first()
        print(cliente_base)

        if cliente_base == None:
            cliente = Cliente(2, nombre, apellido)
            session.add(cliente)
            session.commit()
        else:
            print("El cliente existe")
