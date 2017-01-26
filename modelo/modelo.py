
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///divas.db', echo=True)

Base = declarative_base()

turno_servicio = Table('turno_servicio', Base.metadata,
    Column('turno_id', Integer, ForeignKey('turno.id')),
    Column('servicio_id', Integer, ForeignKey('servicio.id'))
)


class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), index=True, nullable=False)
    apellido = Column(String(120), index=True, nullable=False)
    turno = relationship("Turno")

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):

        return "Nombre: {} - Apellido: {}" .format(self.nombre, self.apellido)


class Turno(Base):
    __tablename__ = 'turno'
    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime, index=True, nullable=False)
    fecha_creacion = Column(Date, index=True, nullable=False)
    fecha_realizado = Column(DateTime, index=True, nullable=False)
    fecha_cancelacion = Column(Date, index=True, nullable=False)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    control_ganancia_id = Column(Integer, ForeignKey('control_ganancia.id'), nullable=True)
    servicios = relationship("Servicio", secondary=turno_servicio)

class Servicio(Base):
    __tablename__ = 'servicio'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), index=True, nullable=False)
    precio = Column(Float, index=True, nullable=False)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return "Servicio: {} - Precio: {}" .format(self.nombre, self.precio)


class ControlGanancia(Base):
    __tablename__ = 'control_ganancia'
    id = Column(Integer, primary_key=True)
    monto = Column(Float, index=True, nullable=False)
    fecha_inicio = Column(Date, index=True, nullable=False)
    fecha_fin = Column(Date, index=True, nullable=False)
    turno = relationship("Turno")

    def __init__(self, monto, fecha_de_inicio, fecha_fin):
        self.monto = monto
        self.fecha_de_inicio = fecha_de_inicio
        self.fecha_fin = fecha_fin


Base.metadata.create_all(engine)