
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow

from vistas_py.menuprincipal import Ui_menuprincipal
from controladores.controlador_alta_cliente import *
from controladores.controlador_alta_servicio import *
from controladores.controlador_nuevo_turno import *
from controladores.controlador_listado_clientes import *

class ControladorMenuPrincipal(QMainWindow):

    def __init__(self):
        print("Menu pricipal")
        super(ControladorMenuPrincipal, self).__init__()
        self.menu_principal = Ui_menuprincipal()
        self.menu_principal.setupUi(self)

        self.menu_principal.action_alta_Cliente.triggered.connect(self.alta_cliente)
        self.menu_principal.action_alta_servicio.triggered.connect(self.alta_servicio)
        self.menu_principal.action_nuevo_turno.triggered.connect(self.alta_turno)
        self.menu_principal.action_listado_cliente.triggered.connect(self.listar_clientes)

    def alta_cliente(self):
        print("alta cliente")
        ac = ControladorAltaCliente()
        ac.exec_()

    def listar_clientes(self):
        print("listar clientes")
        lc = ControladorListadoClientes()
        lc.exec_()

    def alta_servicio(self):
        print("alta servicio")
        als = ControladorAltaServicio()
        als.exec_()

    def alta_turno(self):
        print("Nuevo turno")
        nt = ControladorNuevoTurno()
        nt.exec_()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    menu_principal = ControladorMenuPrincipal()
    menu_principal.show()

    sys.exit(app.exec_())
