from flask import Blueprint, request, jsonify
from extensions.extensions import db, bcrypt
from models.usuario import Usuario
from flask_jwt_extended import create_access_token, jwt_required

user_bp = Blueprint("user_routes", __name__)

# Registro de usuario
@user_bp.route('/api/usuarios/registro', methods=['POST'])
def registrar_usuario():
    data = request.get_json()
    nombre = data.get('nombre')
    email = data.get('email')
    password = data.get('password')

    if not (nombre and email and password):
        return jsonify({"mensaje": "Todos los campos son requeridos"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    nuevo_usuario = Usuario(nombre=nombre, email=email, password=hashed_password)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201

# Inicio de sesión
@user_bp.route('/api/usuarios/login', methods=['POST'])
def login_usuario():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    usuario = Usuario.query.filter_by(email=email).first()
    if not usuario or not bcrypt.check_password_hash(usuario.password, password):
        return jsonify({"mensaje": "Credenciales incorrectas"}), 401

    access_token = create_access_token(identity=usuario.id)
    return jsonify({"mensaje": "Inicio de sesión exitoso", "token": access_token}), 200

# Obtener información del usuario
@user_bp.route('/api/usuarios/<int:id>', methods=['GET'])
@jwt_required()
def obtener_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

<<<<<<< HEAD
    return jsonify({"id": usuario.id, "nombre": usuario.nombre, "email": usuario.email, "rol": usuario.rol}), 200

# Listar todos los usuarios (requiere autenticación)
@user_bp.route('/api/usuarios/listar', methods=['GET'])
@jwt_required()
def listar_usuarios():
    usuarios = Usuario.query.all()
    result = [{"id": u.id, "nombre": u.nombre, "rol": u.rol} for u in usuarios]
    return jsonify(result), 200
=======
    return jsonify({"id": usuario.id, "nombre": usuario.nombre, "email": usuario.email}), 200
>>>>>>> parent of 9dbd3cc (avance 4)
