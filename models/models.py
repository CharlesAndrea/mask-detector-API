from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.orm import backref

db = SQLAlchemy()

# Declaración de clases 
class Empleado(db.Model):
    __tablename__ = 'empleado'
    ci = db.Column(db.Integer, primary_key=True, unique=True)
    nombre_completo = db.Column(db.String, nullable=False)
    correo = db.Column(db.String, nullable=False)
    contrasena = db.Column(db.String, nullable=False)
    tlf = db.Column(db.String)
    direccion = db.Column(db.String(120))
    fecha_nacimiento = db.Column(db.String)
    sexo = db.Column(db.String)
    estado = db.Column(db.Boolean, nullable=False)

    # Columnas correspondientes a relaciones
    dept_id = db.Column(db.Integer, db.ForeignKey('departamento.id'), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable=False)
    # Relación recursiva Supervisor - Empleado
    ci_s = db.Column(db.Integer, db.ForeignKey('empleado.ci')) # Puede ser nulo, en el caso que el empleado sea un supervisor
    parent = db.relationship('Empleado', remote_side=[ci])
    # Relación Empleado - Historial
    historiales = db.relationship('Historial', backref='empleado', lazy=True)


    @property
    def serialize(self):
        return {
            'ci': self.ci,
            'nombre_completo': self.nombre_completo,
            'correo': self.correo,
            'contrasena': self.contrasena,
            'tlf': self.correo,
            'direccion': self.direccion,
            'fecha_nacimiento': self.fecha_nacimiento,
            'sexo': self.sexo,
            'estado': self.estado,
            'dept_id': self.dept_id,
            'rol_id': self.rol_id,
            'historiales': self.historiales
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
    id = db.Column(db.Integer, primary_key=True, unique=True)
    ci_e = db.Column(db.Integer, db.ForeignKey('empleado.ci'), primary_key=True)
    modo_uso = db.Column(db.String)
    fecha = db.Column(db.DateTime)
    @property
    def serialize(self):
        return {
            'id': self.id,
            'ci_e': self.ci_e,
            'modo_uso': self.modo_uso,
            'fecha': self.fecha
        }
