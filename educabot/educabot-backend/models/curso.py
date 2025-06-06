from extensions.extensions import db

class Curso(db.Model):
    __tablename__ = "curso"
    id_curso = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(40), nullable=False)
    descripcion = db.Column(db.String(60))
    id_docente = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))

    # Relación con Matricula
    matriculas = db.relationship("Matricula", back_populates="curso", cascade="all, delete-orphan")
