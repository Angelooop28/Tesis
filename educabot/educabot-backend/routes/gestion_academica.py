from flask import Blueprint, request, jsonify
from extensions.extensions import db
from models.tarea import Tarea
from models.asistencia import Asistencia
from models.calificacion import Calificacion

gestion_bp = Blueprint('gestion', __name__)

# Agregar Tarea
@gestion_bp.route('/api/tareas', methods=['POST'])
def agregar_tarea():
    data = request.get_json()
    nueva_tarea = Tarea(
        id_asignatura=data['id_asignatura'],
        titulo=data['titulo'],
        descripcion=data['descripcion'],
        fecha_entrega=data['fecha_entrega']
    )
    db.session.add(nueva_tarea)
    db.session.commit()
    return jsonify({'message': 'Tarea agregada correctamente'}), 201

# Registrar Asistencia
@gestion_bp.route('/api/asistencias', methods=['POST'])
def registrar_asistencia():
    data = request.get_json()
    nueva_asistencia = Asistencia(
        id_estudiante=data['id_estudiante'],
        fecha=data['fecha'],
        estado=data['estado']
    )
    db.session.add(nueva_asistencia)
    db.session.commit()
    return jsonify({'message': 'Asistencia registrada correctamente'}), 201

# Ingresar Calificaciones
@gestion_bp.route('/api/calificaciones', methods=['POST'])
def ingresar_calificacion():
    data = request.get_json()
    nueva_calificacion = Calificacion(
        id_estudiante=data['id_estudiante'],
        id_asignatura=data['id_asignatura'],
        nota=data['nota'],
        fecha=data['fecha']
    )
    db.session.add(nueva_calificacion)
    db.session.commit()
    return jsonify({'message': 'Calificación registrada correctamente'}), 201
