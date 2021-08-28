from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
marsh = Marshmallow()

# Declaración de clases 

# Empleados
class Empleado(db.Model):
    __tablename__ = 'empleado'
    ci = db.Column(db.Integer, primary_key=True, unique=True)
    public_id = db.Column(db.String(50), unique = True)
    nombre_completo = db.Column(db.String, nullable=False)
    correo = db.Column(db.String, nullable=False)
    contrasena = db.Column(db.String(200), nullable=False)
    tlf = db.Column(db.String)
    direccion = db.Column(db.String(120))
    fecha_nacimiento = db.Column(db.String)
    sexo = db.Column(db.String)
    estado = db.Column(db.SmallInteger, nullable=False, default=1)

    # Columnas correspondientes a relaciones
    # Relación Empleado - Departamento (m-1)
    dept_id = db.Column(db.Integer, db.ForeignKey('departamento.id'), nullable=False)
    # Relación Empleado - Rol (m-1)
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable=False, default=2)
    # Relación recursiva Supervisor - Trabajador (1-m)
    ci_s = db.Column(db.Integer, db.ForeignKey('empleado.ci')) # Puede ser nulo, en el caso que el empleado sea un supervisor
    parent = db.relationship('Empleado', remote_side=[ci])
    # Relación Empleado - Historial (1-m)
    historiales = db.relationship('Historial', backref='empleado', lazy=True)

    def __init__(self, ci, public_id, nombre_completo, correo, contrasena, tlf, direccion, fecha_nacimiento, sexo, estado, dept_id, rol_id, ci_s):
        self.ci = ci,
        self.public_id = public_id,
        self.nombre_completo = nombre_completo,
        self.correo = correo,
        self.contrasena = contrasena,
        self.tlf = tlf, 
        self.direccion = direccion, 
        self.fecha_nacimiento = fecha_nacimiento,
        self.sexo = sexo,
        self.estado = estado, 
        self.dept_id = dept_id,
        self.rol_id = rol_id,
        self.ci_s = ci_s

class EmpleadoEsquema(marsh.SQLAlchemySchema):
    class Meta:
        fields = (
        'ci', 
        'public_id',
        'nombre_completo', 
        'correo', 
        'contrasena', 
        'tlf', 
        'direccion', 
        'fecha_nacimiento',
        'sexo',
        'estado',
        'dept_id',
        'rol_id',
        'ci_s')

# Departamentos
class Departamento(db.Model):
    __tablename__ = 'departamento'
    id = db.Column(db.Integer, primary_key=True)
    nombre_dept = db.Column(db.String)
    # Relación Empleado - Departamento (m-1)
    empleados = db.relationship('Empleado', backref='departamento', lazy=True)

    def __init__(self, id, nombre_dept):
        self.id = id,
        self.nombre_dept = nombre_dept
    
class DepartamentoSchema(marsh.SQLAlchemySchema):
    class Meta:
        fields = ('id', 'nombre_dept')

# Historiales
class Historial(db.Model):
    __tablename__= 'historial'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    # Relación Empleado - Historial (1-m)
    ci_e = db.Column(db.Integer, db.ForeignKey('empleado.ci'), primary_key=True)
    modo_uso = db.Column(db.String)
    fecha = db.Column(db.DateTime)

    def __init__(self, id, ci_e, modo_uso, fecha):
        self.id = id,
        self.ci_e = ci_e,
        self.modo_uso = modo_uso,
        self.fecha = fecha

class HistorialSchema(marsh.SQLAlchemySchema):
    class Meta:
        fields = ('id', 'ci_e', 'modo_uso', 'fecha')

 # Roles  
class Rol(db.Model):
    __tablename__ = 'rol'
    id = db.Column(db.Integer, primary_key=True)
    nombre_rol = db.Column(db.String)
    # Relación Empleados - Rol (m-1)
    empleados = db.relationship('Empleado', backref='rol', lazy=True)

class RolSchema(marsh.SQLAlchemySchema):
    class Meta:
        fields = ('id', 'nombre_rol')