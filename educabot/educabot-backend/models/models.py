from extensions.extensions import db

# Modelo de Tareas
class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    materia = db.Column(db.String(50), nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    fecha_entrega = db.Column(db.String(20), nullable=False)

# Modelo de Asistencia
class Asistencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_asistencias = db.Column(db.Integer, nullable=False)

# Modelo de Calificaciones
class Calificacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    materia = db.Column(db.String(50), nullable=False)
    calificacion = db.Column(db.Float, nullable=False)
