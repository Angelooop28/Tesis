from extensions.extensions import db

class Asignatura(db.Model):
    __tablename__ = 'asignatura'

    id_asignatura = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(40), nullable=False)
    descripcion = db.Column(db.String(60))
