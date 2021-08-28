from models.models import Empleado, EmpleadoEsquema, db


def create_employee(e):
    empleado_esquema = EmpleadoEsquema()
    empleado = Empleado(
        e['ci'],
        e['public_id'],
        e['nombre_completo'],
        e['correo'],
        e['contrasena'],
        e['tlf'],
        e['direccion'],
        e['fecha_nacimiento'],
        e['sexo'],
        e['estado'],
        e['dept_id'],
        e['rol_id'],
        e['ci_s']
    )
    db.session.add(empleado)
    db.session.commit()
    empleado_esquema.dump(empleado)