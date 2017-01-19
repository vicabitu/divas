"""
Esta clase representa el controlador de la vista form_alta_servicio
"""

from PyQt5.QtWidgets import QApplication, QDialog
from vistas_py.form_alta_servicio import Ui_altaservicio
from modelo.modelo import *


class ControladorAltaServicio(QDialog):

    def __init__(self):
        super(ControladorAltaServicio, self).__init__()
        self.form_alta_servicio = Ui_altaservicio()
        self.form_alta_servicio.setupUi(self)

        self.form_alta_servicio.btn_guardar.clicked.connect(self.guardar_servicio)
        self.form_alta_servicio.btn_cancelar.clicked.connect(self.close)

    def guardar_servicio(self):

        nombre = str(self.form_alta_servicio.text_nombre.text())
        precio = str(self.form_alta_servicio.text_precio.text())
        servicio = Servicio(nombre, precio)

        print(servicio.__str__())
        print("Servicio guardado")



