from extensions.extensions import db

class Docente(db.Model):
    __tablename__ = 'docente'

    id_docente = db.Column(db.Integer, primary_key=True)
    especialidad = db.Column(db.String(40), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)

    usuario = db.relationship('Usuario', backref='docente', lazy=True)
