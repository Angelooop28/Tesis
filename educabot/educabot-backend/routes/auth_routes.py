from flask import Blueprint, request, jsonify
from extensions.extensions import db, bcrypt
from models.usuario import Usuario
from schemas.usuario_schema import LoginSchema, RegisterSchema
from flask_jwt_extended import create_access_token
from marshmallow import ValidationError

auth_bp = Blueprint('auth_bp', __name__)

# RUTA: Registrar usuario
@auth_bp.route('/api/auth/register', methods=['POST'])
def register():
    try:
        # Capturar datos y validar el esquema
        data = request.get_json()
        schema = RegisterSchema()
        data = schema.load(data)

        # Verificar si el email ya existe
        usuario_existente = Usuario.query.filter_by(email=data['email']).first()
        if usuario_existente:
            return jsonify({'mensaje': 'El correo ya está registrado'}), 400

        # Hashear la contraseña y crear el usuario
        hashed_password = bcrypt.generate_password_hash(data['password'].strip()).decode('utf-8')
        nuevo_usuario = Usuario(
            nombre=data['nombre'].strip(),
            email=data['email'].strip(),
            password=hashed_password,
            rol=data['rol'].strip()
        )
        db.session.add(nuevo_usuario)
        db.session.commit()

        return jsonify({'mensaje': 'Usuario registrado con éxito'}), 201
    except ValidationError as err:
        return jsonify({'mensaje': 'Datos inválidos', 'errores': err.messages}), 400
    except Exception as e:
        return jsonify({'mensaje': f'Error en el servidor: {str(e)}'}), 500


# RUTA: Iniciar sesión
@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    try:
        # Capturar datos y validar el esquema
        data = request.get_json()
        schema = LoginSchema()
        data = schema.load(data)

        # Buscar usuario por email
        usuario = Usuario.query.filter_by(email=data['email'].strip()).first()

        # Verificar si el usuario existe y la contraseña es correcta
        if not usuario:
            return jsonify({'mensaje': 'Correo no registrado'}), 401
        
        if bcrypt.check_password_hash(usuario.password, data['password'].strip()):
            access_token = create_access_token(identity={'id_usuario': usuario.id_usuario, 'rol': usuario.rol})
            return jsonify({'token': access_token, 'usuario': usuario.nombre}), 200
        
        return jsonify({'mensaje': 'Contraseña incorrecta'}), 401
    except ValidationError as err:
        return jsonify({'mensaje': 'Datos inválidos', 'errores': err.messages}), 400
    except Exception as e:
        return jsonify({'mensaje': f'Error en el servidor: {str(e)}'}), 500
