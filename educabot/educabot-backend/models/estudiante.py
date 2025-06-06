from extensions.extensions import db
from models.usuario import Usuario

class Estudiante(db.Model):
    id_estudiante = db.Column(db.Integer, primary_key=True)
    grado_actual = db.Column(db.Integer, nullable=False)
    celular_representante = db.Column(db.BigInteger)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)

    usuario = db.relationship('Usuario', backref='estudiante', lazy=True)
