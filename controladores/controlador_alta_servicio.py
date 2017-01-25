"""
Esta clase representa el controlador de la vista form_alta_servicio
"""

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from vistas_py.form_alta_servicio import Ui_altaservicio
from modelo.modelo import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ControladorAltaServicio(QDialog):

    def __init__(self):
        super(ControladorAltaServicio, self).__init__()
        self.form_alta_servicio = Ui_altaservicio()
        self.form_alta_servicio.setupUi(self)

        self.form_alta_servicio.btn_guardar.clicked.connect(self.guardar_servicio)
        self.form_alta_servicio.btn_cancelar.clicked.connect(self.close)

    def guardar_servicio(self):

        # conexion
        engine = create_engine('sqlite:///divas.db', echo=True)

        # sesion
        Session = sessionmaker(bind=engine)
        session = Session()


        if self.form_alta_servicio.text_nombre.text() == "" or self.form_alta_servicio.text_precio.text() == "":
            QMessageBox.information(self, "Campos incompletos", "Debe completar todos los campos.")
        else:

            try:
                precio = float(self.form_alta_servicio.text_precio.text())
                nombre = str(self.form_alta_servicio.text_nombre.text())

                servicio_base = session.query(Servicio).filter(Servicio.nombre == nombre).first()

                if servicio_base == None:
                    servicio = Servicio(nombre, precio)
                    self.form_alta_servicio.text_nombre.clear()
                    self.form_alta_servicio.text_precio.clear()
                    QMessageBox.information(self, "Servicio guardado", "Servicio guardado exitosamente")
                    session.add(servicio)
                    session.commit()
                else:
                    QMessageBox.information(self, "Servicio ya existe",
                                    "El servicio ya existe, intente darlo de alta nuevamente.")

            except ValueError:
                QMessageBox.warning(self, "Error", "El precio debe ser de tipo numerico")
