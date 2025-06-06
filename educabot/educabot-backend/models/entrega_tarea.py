# models/entrega_tarea.py

from extensions.extensions import db
from datetime import datetime

class EntregaTarea(db.Model):
    __tablename__ = "entregas_tareas"

    id = db.Column(db.Integer, primary_key=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey("usuario.id_usuario"), nullable=False)
    materia = db.Column(db.String(100), nullable=False)
    nombre_archivo = db.Column(db.String(200), nullable=False)
    ruta_archivo = db.Column(db.String(255), nullable=False)
    fecha_entrega = db.Column(db.DateTime, default=datetime.utcnow)

    estudiante = db.relationship("Usuario", backref="entregas")
