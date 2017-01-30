
from PyQt5.QtWidgets import QDialog
from vistas_py.form_listado_clientes import *
from controladores.controlador_baja_cliente import *
from modelo.modelo import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class ControladorListadoClientes(QDialog):

    def __init__(self):
        super(ControladorListadoClientes, self).__init__()
        self.form_listado_clientes = Ui_ListadoClientes()
        self.form_listado_clientes.setupUi(self)

        # conexion
        engine = create_engine('sqlite:///divas.db', echo=True)

        self.listar_clientes()
        self.form_listado_clientes.btn_eliminar.clicked.connect(self.eliminar_cliente)
        self.form_listado_clientes.btn_actualizar.clicked.connect(self.actualizar_lista)
        self.form_listado_clientes.btn_salir.clicked.connect(self.close)

    def listar_clientes(self):

        # sesion
        Session = sessionmaker(bind=engine)
        session = Session()

        for cliente in session.query(Cliente).all():
            self.form_listado_clientes.list_widget_clientes.addItem(cliente.__str__())

    def eliminar_cliente(self):

        cliente_item = self.form_listado_clientes.list_widget_clientes.currentItem().text() #Me quedo con el item de listwidget, es un string

        cliente_item_lista = cliente_item.split(' ') #separo a cliente_item para quedarme con el nombre, split me devuelve una lista

        nombre = cliente_item_lista.pop(1) #de la lista me quedo con el segundo indice que es nombre del cliente

        apellido = cliente_item_lista.pop(3) #de la lista me quedo con el cuarto indice que es apellido del cliente


        bc = ControladorBajaCliente() #instancio el form de baja cliente
        bc.form_baja_cliente.text_nombre.setText(nombre)
        bc.form_baja_cliente.text_apellido.setText(apellido)
        bc.exec_()

    def actualizar_lista(self):

        self.form_listado_clientes.list_widget_clientes.clear()
        self.listar_clientes()




