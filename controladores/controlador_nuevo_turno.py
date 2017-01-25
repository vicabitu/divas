
from PyQt5.QtWidgets import QDialog
from vistas_py.form_alta_turno import *
from modelo.modelo import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class ControladorNuevoTurno(QDialog):

    def __init__(self):
        super(ControladorNuevoTurno, self).__init__()
        self.form_nuevo_turno = Ui_NuevoTurno()
        self.form_nuevo_turno.setupUi(self)

        self.form_nuevo_turno.btn_cancelar.clicked.connect(self.close)

        self.form_nuevo_turno.list_servicios.addItem("Servicios agregados:")

        """self.form_nuevo_turno.combo_box_clientes.addItem("")
        self.form_nuevo_turno.combo_box_clientes.addItem("Juan Perez")
        self.form_nuevo_turno.combo_box_clientes.addItem("Carla Gonzalez")
        self.form_nuevo_turno.combo_box_clientes.addItem("Carlitos Gomez")

        self.form_nuevo_turno.combo_box_servicios.addItem("")
        self.form_nuevo_turno.combo_box_servicios.addItem("Corte de pelo")
        self.form_nuevo_turno.combo_box_servicios.addItem("Cambio de aceite")
        self.form_nuevo_turno.combo_box_servicios.addItem("Cambio de aros")"""

        # conexion
        engine = create_engine('sqlite:///divas.db', echo=True)

        # sesion
        Session = sessionmaker(bind=engine)
        session = Session()

        self.form_nuevo_turno.combo_box_clientes.addItem("Clientes:")
        self.llenar_combo_clientes(session)
        self.form_nuevo_turno.combo_box_servicios.addItem("Servicios:")
        self.llenar_combo_servicios(session)

        self.form_nuevo_turno.combo_box_clientes.currentIndexChanged.connect(self.agregar_cliente)
        self.form_nuevo_turno.combo_box_servicios.currentIndexChanged.connect(self.agregar_servicio)
        self.form_nuevo_turno.btn_eliminas_servicio.clicked.connect(self.eliminar_servicio)
        self.form_nuevo_turno.btn_guardar.clicked.connect(self.guardar_turno)
        self.form_nuevo_turno.btn_cancelar.clicked.connect(self.close)

    def llenar_combo_clientes(self, session):

        for cliente in session.query(Cliente).all():
            nombre_y_apellido = cliente.nombre + " " + cliente.apellido
            self.form_nuevo_turno.combo_box_clientes.addItem(nombre_y_apellido)

    def llenar_combo_servicios(self, session):

        for servicio in session.query(Servicio).all():
            self.form_nuevo_turno.combo_box_servicios.addItem(servicio.nombre)


    def agregar_servicio(self):

        servicio_seleccionado = self.form_nuevo_turno.combo_box_servicios.currentText()

        print(servicio_seleccionado)

        rango = range(self.form_nuevo_turno.list_servicios.count())

        for s in rango:
            if self.form_nuevo_turno.list_servicios.item(s) != servicio_seleccionado:
                self.form_nuevo_turno.list_servicios.addItem(servicio_seleccionado)
            else:
                print("El servicio ya esta agregado")


        """indice = int(self.form_nuevo_turno.combo_box_servicios.currentIndex())
        #self.verificar_servicio(servicio)
        if self.verificar_servicio(servicio) == True:
            self.form_nuevo_turno.list_servicios.addItem(servicio)
        else:
            print("El servicio ya esta en la lista")


        print(indice)
        self.form_nuevo_turno.list_servicios.addItem(servicio)
        self.form_nuevo_turno.combo_box_servicios.setItemText(indice, "")"""

    def verificar_servicio(self, servicio):

        for s in range(self.form_nuevo_turno.list_servicios.count()):
            ser = str(self.form_nuevo_turno.list_servicios.item(s))
            print(self.form_nuevo_turno.list_servicios.count())
            print(ser)
            print(range(self.form_nuevo_turno.list_servicios.count()))
            if ser != servicio:
                #self.form_nuevo_turno.list_servicios.addItem(servicio)
                return True
            else:
                return False


    def agregar_cliente(self):

        cliente = self.form_nuevo_turno.combo_box_clientes.currentText()
        print(cliente)
        self.form_nuevo_turno.text_cliente.setText(cliente)

    def eliminar_servicio(self):
        pass


    def guardar_turno(self):
        pass
