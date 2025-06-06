from extensions.extensions import db

class Matricula(db.Model):
    __tablename__ = "matricula"
    id_matricula = db.Column(db.Integer, primary_key=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey("usuario.id_usuario"))
    id_curso = db.Column(db.Integer, db.ForeignKey("curso.id_curso"))
    fecha_matricula = db.Column(db.Date, nullable=False)

    # Relación inversa
    curso = db.relationship("Curso", back_populates="matriculas")
