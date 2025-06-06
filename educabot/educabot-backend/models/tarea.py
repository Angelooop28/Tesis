from extensions.extensions import db

class Tarea(db.Model):
    __tablename__ = "tareas"
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    fecha_vencimiento = db.Column(db.Date, nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)
<<<<<<< HEAD
    estudiante_id = db.Column(db.Integer, nullable=False)
    
    id_materia = db.Column(db.Integer, db.ForeignKey('curso.id_curso'))
    materia = db.relationship('Curso', backref='tareas')

=======
    estudiante_id = db.Column(db.Integer, nullable=False)  # ID del estudiante

    def __init__(self, titulo, fecha_vencimiento, descripcion=None, estudiante_id=None):
        self.titulo = titulo
        self.fecha_vencimiento = fecha_vencimiento
        self.descripcion = descripcion
        self.estudiante_id = estudiante_id
>>>>>>> parent of 9dbd3cc (avance 4)
