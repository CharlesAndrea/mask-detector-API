from models.models import Historial, HistorialSchema, db

def create_record(h):
    historial_esquema = HistorialSchema()
    historial = Historial(
        h['id'], # Puede que no sea necesario porque se autoincrementa
        h['ci_e'],
        h['modo_uso'],
        h['fecha']
    )
    db.session.add(historial)
    db.session.commit()
    historial_esquema.dump(historial)
