from flask_sqlalchemy import SQLAlchemy

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
    historiales = db.relationship('Historial', backref='empleado', lazy=True)
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
            'historiales': self.historiales
        }

class Departamento(db.Model):
    __tablename__ = 'departamento'
    id = db.Column(db.Integer, primary_key=True)
    nombre_dept = db.Column(db.String)
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
    @property
    def serialize(self):
        return {
            'id': self.id,
            'nombre_rol': self.nombre_rol
        }

class Historial(db.Model):
    __tablename__= 'historial'
    id = db.Column(db.Integer)
    ci_empleado = db.Column(db.Integer, db.ForeignKey('empleado.ci'),
        nullable=False)
    modo_uso = db.Column(db.String)
    fecha = db.Column(db.DateTime)
    @property
    def serialize(self):
        return {
            'id': self.id,
            'ci_empleado': self.ci_empleado,
            'modo_uso': self.modo_uso,
            'fecha': self.fecha
        }


historial_generado = db.Table('historial_generado',
    db.Column('ci_empleado', db.Integer, db.ForeignKey('empleado.ci'), primary_key=True),
    db.Column('id_hist', db.Integer, db.ForeignKey('historial.id'), primary_key=True)
)