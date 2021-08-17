from models.models import Historial 
from models.models import db 

def create(historial):
    h = Historial(
        historial['id'], # Puede que no sea necesario porque se autoincrementa
        historial['ci_e'],
        historial['modo_uso'],
        historial['fecha']
    )
    db.session.add(h)
    db.session.commit()
