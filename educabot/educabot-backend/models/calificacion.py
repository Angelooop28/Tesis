from extensions.extensions import db

class Calificacion(db.Model):
    __tablename__ = 'calificaciones'

    id = db.Column(db.Integer, primary_key=True)
    estudiante_id = db.Column(db.Integer, nullable=False)  # ID del estudiante
    materia = db.Column(db.String(100), nullable=False)    # Nombre de la materia
    calificacion = db.Column(db.Float, nullable=False)     # Calificación obtenida
    fecha = db.Column(db.Date, nullable=False)             # Fecha de registro

    def __init__(self, estudiante_id, materia, calificacion, fecha):
        self.estudiante_id = estudiante_id
        self.materia = materia
        self.calificacion = calificacion
        self.fecha = fecha
