from PyQt5.QtWidgets import QDialog
from vistas_py.form_listado_servicios import Ui_Dialog
from modelo.modelo import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class ControladorListarServicios(QDialog):

    def __init__(self):
        super(ControladorListarServicios, self).__init__()
        self.form_listado_servicios = Ui_Dialog()
        self.form_listado_servicios.setupUi(self)

        # conexion
        engine = create_engine('sqlite:///divas.db', echo=True)
        # sesion
        Session = sessionmaker(bind=engine)
        session = Session()

        self.llenar_listado(session)

        self.form_listado_servicios.btn_eliminar.clicked.connect(self.eliminar_servicio)
        self.form_listado_servicios.btn_modificar.clicked.connect(self.modificar_servicio)
        self.form_listado_servicios.btn_cancelar.clicked.connect(self.close)

    def llenar_listado(self, session):

        servicios = session.query(Servicio).all()

        for servicio in servicios:
            self.form_listado_servicios.list_widget_servicios.addItem(servicio.__str__())

    def modificar_servicio(self, session):
        pass

    def eliminar_servicio(self, session):
        pass