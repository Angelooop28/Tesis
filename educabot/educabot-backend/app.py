from flask import Flask
from config import Config
from extensions.extensions import db, ma, bcrypt, jwt
from flask_cors import CORS
from routes.auth_routes import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

# Inicialización de extensiones
db.init_app(app)
ma.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

# Crear tablas
with app.app_context():
    db.create_all()

# Registrar rutas
app.register_blueprint(auth_bp)

@app.route('/')
def home():
    return {'mensaje': 'Bienvenido a la API de Educabot'}, 200

if __name__ == '__main__':
    app.run(debug=True)
