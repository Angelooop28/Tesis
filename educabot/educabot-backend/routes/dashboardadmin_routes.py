from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.usuario import Usuario
from models.tarea import Tarea
from models.asignatura import Asignatura
from extensions.extensions import db

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/api/dashboard-admin', methods=['GET'])
@jwt_required()
def dashboard_admin():
    identidad = get_jwt_identity()
    id_usuario = identidad.get("id_usuario")

    admin = Usuario.query.filter_by(id_usuario=id_usuario, rol='admin').first()
    if not admin:
        return jsonify({'mensaje': 'No autorizado'}), 403

    # Obtener todos los usuarios
    usuarios = Usuario.query.all()
    lista_usuarios = [{
        'id': u.id_usuario,
        'nombre': u.nombre,
        'email': u.email,
        'rol': u.rol
    } for u in usuarios]

    # Obtener todas las tareas con asignatura asociada
    tareas = Tarea.query.all()
    lista_tareas = [{
        'id': t.id,
        'titulo': t.titulo,
        'descripcion': t.descripcion,
        'fecha_entrega': t.fecha_vencimiento.strftime('%Y-%m-%d') if t.fecha_vencimiento else None,
        'materia': t.materia.nombre if t.materia else "Sin asignar"
    } for t in tareas]

    # Obtener todas las asignaturas
    asignaturas = Asignatura.query.all()
    lista_asignaturas = [{
        'id': a.id_asignatura,
        'nombre': a.nombre,
        'descripcion': a.descripcion
    } for a in asignaturas]

    return jsonify({
        'admin': admin.nombre,
        'usuarios': lista_usuarios,
        'tareas': lista_tareas,
        'asignaturas': lista_asignaturas  # ✅ Incluido correctamente
    }), 200
