from flask import Flask, jsonify, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from datetime import datetime

app = Flask(__name__)

# Configuración de PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin2024@localhost:5432/bd_educabot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'clave_secreta'

db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Inicialización de la base de datos (reemplazo de @app.before_first_request)
with app.app_context():
    db.create_all()

# Modelos de la base de datos
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    contraseña = db.Column(db.String(100), nullable=False)  # Cambiar a String(100)
    rol = db.Column(db.String(40), nullable=False)

class Estudiante(db.Model):
    __tablename__ = 'Estudiante'
    id_estudiante = db.Column(db.Integer, primary_key=True)
    grado_actual = db.Column(db.Integer, nullable=False)
    celular_representante = db.Column(db.Integer)

class Docente(db.Model):
    __tablename__ = 'Docente'
    id_docente = db.Column(db.Integer, primary_key=True)
    especialidad = db.Column(db.String(40), nullable=False)

class Curso(db.Model):
    __tablename__ = 'Curso'
    id_curso = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(40), nullable=False)
    descripcion = db.Column(db.String(60))

class Matricula(db.Model):
    __tablename__ = 'Matricula'
    id_matricula = db.Column(db.Integer, primary_key=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('Estudiante.id_estudiante'), nullable=False)
    id_curso = db.Column(db.Integer, db.ForeignKey('Curso.id_curso'), nullable=False)
    fecha_matricula = db.Column(db.Date, nullable=False)

class Asignatura(db.Model):
    __tablename__ = 'Asignatura'
    id_asignatura = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(40), nullable=False)
    descripcion = db.Column(db.String(60))

class Tarea(db.Model):
    __tablename__ = 'Tarea'
    id_tarea = db.Column(db.Integer, primary_key=True)
    id_asignatura = db.Column(db.Integer, db.ForeignKey('Asignatura.id_asignatura'), nullable=False)
    titulo = db.Column(db.String(40), nullable=False)
    descripcion = db.Column(db.String(60))
    fecha_entrega = db.Column(db.Date, nullable=False)

class Asistencia(db.Model):
    __tablename__ = 'Asistencia'
    id_asistencia = db.Column(db.Integer, primary_key=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('Estudiante.id_estudiante'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    estado = db.Column(db.String(40), nullable=False)

class Calificacion(db.Model):
    __tablename__ = 'Calificacion'
    id_calificacion = db.Column(db.Integer, primary_key=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('Estudiante.id_estudiante'), nullable=False)
    id_asignatura = db.Column(db.Integer, db.ForeignKey('Asignatura.id_asignatura'), nullable=False)
    nota = db.Column(db.String(10), nullable=False)
    fecha = db.Column(db.Date, nullable=False)

class Chatbot(db.Model):
    __tablename__ = 'Chatbot'
    id_chatbot = db.Column(db.Integer, primary_key=True)
    pregunta = db.Column(db.String(50), nullable=False)
    respuesta = db.Column(db.String(80), nullable=False)

# Rutas principales
@app.route('/')
def home():
    return jsonify({'mensaje': 'Bienvenido a la API de Educabot'}), 200

@app.route('/favicon.ico')
def favicon():
    return '', 204  # Ignorar favicon.ico

# Rutas de ejemplo
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['contraseña']).decode('utf-8')
    nuevo_usuario = Usuario(
        nombre=data['nombre'],
        email=data['email'],
        contraseña=hashed_password,
        rol=data['rol']
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario registrado con éxito'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = Usuario.query.filter_by(email=data['email']).first()
    if usuario and bcrypt.check_password_hash(usuario.contraseña, data['contraseña']):
        access_token = create_access_token(identity={'id_usuario': usuario.id_usuario, 'rol': usuario.rol})
        return jsonify({'token': access_token}), 200
    return jsonify({'mensaje': 'Credenciales incorrectas'}), 401

@app.route('/tareas', methods=['GET'])
@jwt_required()
def get_tareas():
    tareas = Tarea.query.all()
    result = [
        {
            'id_tarea': tarea.id_tarea,
            'titulo': tarea.titulo,
            'descripcion': tarea.descripcion,
            'fecha_entrega': tarea.fecha_entrega.strftime('%Y-%m-%d')
        } for tarea in tareas
    ]
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
