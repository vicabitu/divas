
from PyQt5.QtWidgets import QDialog
from vistas_py.form_listado_clientes import *
from modelo import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class ControladorListadoClientes(QDialog):

    def __init__(self):
        super(ControladorListadoClientes, self).__init__()
        self.form_listado_clientes = Ui_ListadoClientes()
        self.form_listado_clientes.setupUi(self)

        # conexion
        engine = create_engine('sqlite:///divas.db', echo=True)

        # sesion
        Session = sessionmaker(bind=engine)
        session = Session()

        self.listar_clientes(session)

    def listar_clientes(self, session):
        for cliente in session.query(Cliente).all():
            self.form_listado_clientes.listView.add



