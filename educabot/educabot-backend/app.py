from flask import Flask
from config import Config
from extensions.extensions import db, ma, bcrypt, jwt
from flask_cors import CORS

# Importación de Blueprints
from routes.auth_routes import auth_bp
from routes.tarea_routes import tarea_bp  # Rutas de tareas
from routes.asistencia_routes import asistencia_bp  # Rutas de asistencias
from routes.calificacion_routes import calificacion_bp  # Rutas de calificaciones
from routes.user_routes import user_bp  # Importar la ruta de usuarios

app = Flask(__name__)
app.config.from_object(Config)

# Inicialización de extensiones
db.init_app(app)
ma.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

# Crear tablas (solo si no existen)
with app.app_context():
    db.create_all()

# Registrar rutas existentes
app.register_blueprint(auth_bp)  # Rutas de autenticación
app.register_blueprint(tarea_bp, url_prefix="/api/tareas")  # Rutas de tareas
app.register_blueprint(asistencia_bp, url_prefix="/api/asistencias")  # Rutas de asistencias
app.register_blueprint(calificacion_bp, url_prefix="/api/calificaciones")  # Rutas de calificaciones

# Registrar rutas nuevas
app.register_blueprint(user_bp, url_prefix="/api/usuarios")  # Rutas de usuarios

# Ruta principal de prueba
@app.route('/')
def home():
    return {'mensaje': 'Bienvenido a la API de Educabot'}, 200

# Ejecución del servidor
if __name__ == '__main__':
    app.run(debug=True)
