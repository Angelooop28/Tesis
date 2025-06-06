from extensions.extensions import db
from datetime import datetime

# ----------------------------
# Modelo: Tarea
# ----------------------------
class Tarea(db.Model):
    __tablename__ = 'tarea'
    
    id_tarea = db.Column(db.Integer, primary_key=True)
    id_asignatura = db.Column(db.Integer, db.ForeignKey('asignatura.id_asignatura'), nullable=False)
    titulo = db.Column(db.String(40), nullable=False)
    descripcion = db.Column(db.String(60))
    fecha_entrega = db.Column(db.Date)
    
    asignatura = db.relationship("Asignatura", backref="tareas")  # acceso inverso opcional

# ----------------------------
# Modelo: Asistencia
# ----------------------------
class Asistencia(db.Model):
    __tablename__ = 'asistencia'

    id_asistencia = db.Column(db.Integer, primary_key=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    estado = db.Column(db.String(40), nullable=False)

    estudiante = db.relationship("Usuario", backref="asistencias")

# ----------------------------
# Modelo: Calificacion
# ----------------------------
class Calificacion(db.Model):
    __tablename__ = 'calificacion'

    id_calificacion = db.Column(db.Integer, primary_key=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    id_asignatura = db.Column(db.Integer, db.ForeignKey('asignatura.id_asignatura'), nullable=False)
    nota = db.Column(db.String(10), nullable=False)
    fecha = db.Column(db.Date, nullable=False)

    estudiante = db.relationship("Usuario", backref="calificaciones")
    asignatura = db.relationship("Asignatura", backref="calificaciones")
