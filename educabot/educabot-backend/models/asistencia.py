from extensions.extensions import db

class Asistencia(db.Model):
    __tablename__ = 'asistencias'

    id = db.Column(db.Integer, primary_key=True)
    estudiante_id = db.Column(db.Integer, nullable=False)  # ID del estudiante
    materia = db.Column(db.String(100), nullable=False)    # Nombre de la materia
    fecha = db.Column(db.Date, nullable=False)             # Fecha de la asistencia
    presente = db.Column(db.Boolean, default=False)        # Si estuvo presente o no

    def __init__(self, estudiante_id, materia, fecha, presente=False):
        self.estudiante_id = estudiante_id
        self.materia = materia
        self.fecha = fecha
        self.presente = presente
