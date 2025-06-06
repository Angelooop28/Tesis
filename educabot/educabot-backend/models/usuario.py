from extensions.extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(40), nullable=False)

<<<<<<< HEAD
    def check_password(self, password_input):
        return bcrypt.check_password_hash(self.password, password_input)
=======
    def __init__(self, nombre, email, password, rol):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.rol = rol
>>>>>>> parent of 9dbd3cc (avance 4)
