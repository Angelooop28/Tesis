from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import jsonify
from models.usuario import Usuario


def rol_requerido(rol_esperado):
    def decorador(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            id_usuario = get_jwt_identity()
            usuario = Usuario.query.filter_by(id_usuario=id_usuario).first()
            if not usuario or usuario.rol.lower() != rol_esperado.lower():
                return jsonify({"mensaje": "Acceso no autorizado"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorador
