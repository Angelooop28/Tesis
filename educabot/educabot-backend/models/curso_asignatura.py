from extensions.extensions import db

class CursoAsignatura(db.Model):
    __tablename__ = 'curso_asignatura'

    id = db.Column(db.Integer, primary_key=True)
    id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=False)
    id_asignatura = db.Column(db.Integer, db.ForeignKey('asignatura.id_asignatura'), nullable=False)
