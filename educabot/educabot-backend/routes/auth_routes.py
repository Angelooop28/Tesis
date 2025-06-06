import os
from flask import Blueprint, request, jsonify
from extensions.extensions import db, bcrypt
from models.usuario import Usuario
from schemas.usuario_schema import LoginSchema, RegisterSchema
from flask_jwt_extended import create_access_token
from marshmallow import ValidationError

auth_bp = Blueprint('auth_bp', __name__)

<<<<<<< HEAD
@auth_bp.route('/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        return '', 204
=======
# RUTA: Registrar usuario
@auth_bp.route('/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        return '', 204  # Respuesta vacía para solicitudes OPTIONS
>>>>>>> parent of 9dbd3cc (avance 4)

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
            email=data['email'].strip().lower(),  # Convertir email a minúsculas
            password=hashed_password,
            rol=data['rol'].strip()
        )
        db.session.add(nuevo_usuario)
        db.session.commit()

        return jsonify({'mensaje': 'Usuario registrado con éxito'}), 201
    except ValidationError as err:
        return jsonify({'mensaje': 'Datos inválidos', 'errores': err.messages}), 400
    except Exception as e:
        print("🚨 Error en registro:", str(e))
        return jsonify({'mensaje': f'Error en el servidor: {str(e)}'}), 500

<<<<<<< HEAD
=======

# RUTA: Iniciar sesión
>>>>>>> parent of 9dbd3cc (avance 4)
@auth_bp.route('/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return '', 204  # Respuesta vacía para solicitudes OPTIONS

    try:
        # Capturar datos y validar el esquema
        data = request.get_json()
        schema = LoginSchema()
        data = schema.load(data)

<<<<<<< HEAD
        email = data.get("email", "").strip().lower()
        password = data.get("password", "").strip()

        usuario = Usuario.query.filter_by(email=email).first()

        print("🧪 Buscando usuario con email:", email)

        if not usuario:
            print("❌ Usuario no encontrado")
            return jsonify({"mensaje": "Usuario no encontrado"}), 404

        if not usuario.password:
            print("⚠️ Usuario no tiene contraseña registrada")
            return jsonify({"mensaje": "Contraseña no configurada"}), 400

        print("🔐 Comparando password...")
        if bcrypt.check_password_hash(usuario.password, password):
            print("✅ Contraseña válida. Login exitoso.")

            token_de_acceso = create_access_token(identity={
                "id_usuario": usuario.id_usuario,
                "rol": usuario.rol
            })
=======
        # Buscar usuario por email
        usuario = Usuario.query.filter_by(email=data['email'].strip().lower()).first()  # Email en minúsculas
>>>>>>> parent of 9dbd3cc (avance 4)

        # Verificar si el usuario existe y la contraseña es correcta
        if not usuario:
            return jsonify({'mensaje': 'Correo no registrado'}), 401
        
        if bcrypt.check_password_hash(usuario.password, data['password'].strip()):
            access_token = create_access_token(identity={'id_usuario': usuario.id_usuario, 'rol': usuario.rol})
            return jsonify({
                'token': access_token,
                'usuario': usuario.nombre,
                'rol': usuario.rol  # Rol del usuario
            }), 200
<<<<<<< HEAD
        else:
            print("❌ Contraseña inválida")
            return jsonify({"mensaje": "Contraseña incorrecta"}), 401

    except ValidationError as err:
        return jsonify({'mensaje': 'Datos inválidos', 'errores': err.messages}), 400
    except Exception as e:
        print("💥 Error general en login:", str(e))
        return jsonify({'mensaje': f'Error del servidor: {str(e)}'}), 500

@auth_bp.route('/recuperar', methods=['POST'])
def recuperar_password():
    data = request.get_json()
    email = data.get('email', '').strip()

    if not email:
        return jsonify({'mensaje': 'Correo requerido'}), 400

    usuario = Usuario.query.filter_by(email=email).first()
    if not usuario:
        return jsonify({'mensaje': 'Correo no registrado'}), 404

    print(f"📧 Se simuló el envío del link de recuperación a {email}")
    return jsonify({'mensaje': 'Se ha enviado un enlace de recuperación a tu correo'}), 200
=======
        
        return jsonify({'mensaje': 'Contraseña incorrecta'}), 401
    except ValidationError as err:
        return jsonify({'mensaje': 'Datos inválidos', 'errores': err.messages}), 400
    except Exception as e:
        return jsonify({'mensaje': f'Error en el servidor: {str(e)}'}), 500
>>>>>>> parent of 9dbd3cc (avance 4)
