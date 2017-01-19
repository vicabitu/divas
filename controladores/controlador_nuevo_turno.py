
from PyQt5.QtWidgets import QDialog
from vistas_py.form_alta_turno import *
from modelo.modelo import *

class ControladorNuevoTurno(QDialog):

    def __init__(self):
        super(ControladorNuevoTurno, self).__init__()
        self.form_nuevo_turno = Ui_NuevoTurno()
        self.form_nuevo_turno.setupUi(self)

        self.form_nuevo_turno.btn_cancelar.clicked.connect(self.close)

        self.form_nuevo_turno.list_servicios.addItem("Servicios agregados:")

        self.form_nuevo_turno.combo_box_clientes.addItem("")
        self.form_nuevo_turno.combo_box_clientes.addItem("Juan Perez")
        self.form_nuevo_turno.combo_box_clientes.addItem("Carla Gonzalez")
        self.form_nuevo_turno.combo_box_clientes.addItem("Carlitos Gomez")

        self.form_nuevo_turno.combo_box_servicios.addItem("")
        self.form_nuevo_turno.combo_box_servicios.addItem("Corte de pelo")
        self.form_nuevo_turno.combo_box_servicios.addItem("Cambio de aceite")
        self.form_nuevo_turno.combo_box_servicios.addItem("Cambio de aros")

        self.form_nuevo_turno.combo_box_clientes.currentIndexChanged.connect(self.agregar_cliente)
        self.form_nuevo_turno.combo_box_servicios.currentIndexChanged.connect(self.agregar_servicio)
        self.form_nuevo_turno.btn_eliminas_servicio.clicked.connect(self.eliminar_servicio)


    def agregar_servicio(self):

        servicio = self.form_nuevo_turno.combo_box_servicios.currentText()
        indice = int(self.form_nuevo_turno.combo_box_servicios.currentIndex())
        #self.verificar_servicio(servicio)
        if self.verificar_servicio(servicio) == True:
            self.form_nuevo_turno.list_servicios.addItem(servicio)
        else:
            print("El servicio ya esta en la lista")


        """print(indice)
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


        #self.form_nuevo_turno.list_servicios.


    def agregar_cliente(self):

        cliente = self.form_nuevo_turno.combo_box_clientes.currentText()
        print(cliente)
        self.form_nuevo_turno.text_cliente.setText(cliente)

    def eliminar_servicio(self):
        print("Eliminar Servicio")
