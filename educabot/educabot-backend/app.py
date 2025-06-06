import os
import logging
import traceback
from dotenv import load_dotenv

from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from extensions.extensions import db, ma, bcrypt, jwt

# Blueprints
from routes.auth_routes import auth_bp
from routes.tarea_routes import tarea_bp
from routes.asistencia_routes import asistencia_bp
from routes.calificacion_routes import calificacion_bp
from routes.user_routes import user_bp
from routes.gestion_academica import gestion_bp
<<<<<<< HEAD
from routes.chatbot_routes import chatbot_bp
from routes.dashboardestudiantes_routes import dashboard_bp as estudiante_bp
from routes.dashboardadmin_routes import admin_bp
from routes.dashboarddocentes_routes import docentes_bp
from routes.subir_tarea_estudiante import upload_bp  # ✅ NUEVO

# Cargar variables de entorno
load_dotenv()
=======
from routes.chatbot_routes import chatbot_bp  # Importar el blueprint del chatbot
>>>>>>> parent of 9dbd3cc (avance 4)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

<<<<<<< HEAD
    # ✅ CORS configurado para frontend Vue
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}}, supports_credentials=True)

    # ✅ Inicializar extensiones
=======
    # Inicialización de extensiones
    initialize_extensions(app)

    # Configuración de CORS
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

    # Registro de Blueprints
    register_blueprints(app)

    # Manejo global de errores
    register_error_handlers(app)

    # Crear tablas solo en desarrollo
    if app.config.get('ENV', 'production') == 'development':
        with app.app_context():
            db.create_all()

    return app

def initialize_extensions(app):
    """Inicializar las extensiones necesarias para Flask."""
>>>>>>> parent of 9dbd3cc (avance 4)
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

<<<<<<< HEAD
    # ✅ Registrar rutas (blueprints)
=======
def register_blueprints(app):
    """Registrar los blueprints de las rutas."""
>>>>>>> parent of 9dbd3cc (avance 4)
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(tarea_bp, url_prefix="/api/tareas")
    app.register_blueprint(asistencia_bp, url_prefix="/api/asistencias")
    app.register_blueprint(calificacion_bp, url_prefix="/api/calificaciones")
    app.register_blueprint(user_bp, url_prefix="/api/usuarios")
    app.register_blueprint(gestion_bp, url_prefix="/api/gestion")
<<<<<<< HEAD
    app.register_blueprint(chatbot_bp, url_prefix="/api/chatbot")
    app.register_blueprint(estudiante_bp, url_prefix="/api/dashboard")
    app.register_blueprint(admin_bp, url_prefix="/api/dashboard-admin")
    app.register_blueprint(docentes_bp, url_prefix="/api/dashboard-docentes")
    app.register_blueprint(upload_bp, url_prefix="/api/subir-tarea")

    # ✅ CORS manual (seguro para fallos CORS preflight)
    @app.after_request
    def apply_cors_headers(response):
        response.headers["Access-Control-Allow-Origin"] = "http://localhost:8080"
        response.headers["Access-Control-Allow-Credentials"] = "true"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
        response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
        return response

    # ✅ Manejo global de errores
    register_error_handlers(app)

    # Crear tablas en entorno de desarrollo
    if app.config.get("ENV") == "development":
        with app.app_context():
            db.create_all()

    return app
=======
    app.register_blueprint(chatbot_bp, url_prefix="/api/chatbot")  # Registrar el blueprint del chatbot
>>>>>>> parent of 9dbd3cc (avance 4)

def register_error_handlers(app):
    """Registrar manejadores de errores."""
    @app.errorhandler(404)
    def not_found_error(error):
        logging.error(f"📛 Ruta no encontrada: {error}")
        return jsonify({'error': 'Ruta no encontrada'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        logging.error("💥 Error interno del servidor:")
        traceback.print_exc()
        return jsonify({'error': 'Error interno del servidor'}), 500

# ✅ Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# ✅ Crear app y contexto
app = create_app()
<<<<<<< HEAD
with app.app_context():
    db.create_all()

# Ruta de prueba
@app.route("/")
=======

# Ruta principal de prueba
@app.route('/')
>>>>>>> parent of 9dbd3cc (avance 4)
def home():
    return {'mensaje': 'Bienvenido a la API de Educabot'}, 200

# Ejecutar app
if __name__ == "__main__":
    app.run(debug=True)
