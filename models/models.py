from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy

# Definición de clases, cada clase corresponde a un modelo

class Empleado(db.Model):
    __tablename__ = 'empleado'
    ci = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String)
    correo = db.Column(db.String)
    tlf = db.Column(db.String)
    direccion = db.Column(db.String(120))
    fecha_nacimiento = db.Column(db.String)
    sexo = db.Column(db.String)
    estado = db.Column(db.Boolean)
    dept_id = db.Column(db.Integer, db.ForeignKey('departamento.id'), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable=False)
    ci_s = Column(Integer, ForeignKey('empleado.id'))
    parent = relationship('Empleado', remote_side=[ci])
    @property
    def serialize(self):
        return {
            'ci': self.ci,
            'nombre_completo': self.nombre_completo,
            'correo': self.correo,
            'tlf': self.correo,
            'direccion': self.direccion,
            'fecha_nacimiento': self.fecha_nacimiento,
            'sexo': self.sexo,
            'estado': self.estado,
            'dept_id': self.dept_id,
            'rol_id': self.rol_id
        }

class Departamento(db.Model):
    __tablename__ = 'departamento'
    id = db.Column(db.Integer, primary_key=True)
    nombre_dept = db.Column(db.String)
    empleados = db.relationship('Empleado', backref='departamento', lazy=True)
    @property
    def serialize(self):
        return {
            'id': self.id,
            'nombre_dept': self.nombre_dept
        }

class Rol(db.Model):
    __tablename__ = 'rol'
    id = db.Column(db.Integer, primary_key=True)
    nombre_rol = db.Column(db.String)
    empleados = db.relationship('Empleado', backref='rol', lazy=True)
    @property
    def serialize(self):
        return {
            'id': self.id,
            'nombre_rol': self.nombre_rol,
            'empleados': self.empleados
        }

class Historial(db.Model):
    __tablename__= 'historial'
    id = db.Column(db.Integer)
    modo_uso = db.Column(db.String)
    fecha = db.Column(db.DateTime)
    @property
    def serialize(self):
        return {
            'id': self.id,
            'modo_uso': self.modo_uso,
            'fecha': self.fecha
        }


historial_generado = db.Table('historial_generado',
    db.Column('ci_e', db.Integer, db.ForeignKey('empleado.ci'), primary_key=True),
    db.Column('id_hist', db.Integer, db.ForeignKey('historial.id'), primary_key=True)
)
