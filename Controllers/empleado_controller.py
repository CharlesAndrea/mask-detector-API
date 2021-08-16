from models.models import Empleado
from models.models import db 


def create(empleado):
    e = Empleado(
        empleado['ci'],
        empleado['nombre_completo'],
        empleado['correo'],
        empleado['contrasena'],
        empleado['tlf'],
        empleado['direccion'],
        empleado['fecha_nacimiento'],
        empleado['sexo'],
        empleado['estado'],
        empleado['dept_id'],
        empleado['rol_id'],
        empleado['ci_s']
    )
    db.session.add(e)
    db.session.commit()
