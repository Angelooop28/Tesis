from flask import Blueprint, request, jsonify
from extensions.extensions import db
from models.asistencia import Asistencia
from flask_jwt_extended import jwt_required

# Crear el Blueprint para asistencias
asistencia_bp = Blueprint("asistencia_routes", __name__)

# Ruta para crear una asistencia
@asistencia_bp.route('/api/asistencias', methods=['POST'])
@jwt_required()
def crear_asistencia():
    data = request.get_json()
    estudiante_id = data.get('estudiante_id')
    materia = data.get('materia')
    fecha = data.get('fecha')
    presente = data.get('presente', False)

    if not (estudiante_id and materia and fecha):
        return jsonify({"mensaje": "Todos los campos son requeridos"}), 400

    nueva_asistencia = Asistencia(
        estudiante_id=estudiante_id,
        materia=materia,
        fecha=fecha,
        presente=presente
    )
    db.session.add(nueva_asistencia)
    db.session.commit()

    return jsonify({"mensaje": "Asistencia creada exitosamente"}), 201

# Ruta para obtener todas las asistencias
@asistencia_bp.route('/api/asistencias', methods=['GET'])
@jwt_required()
def obtener_asistencias():
    asistencias = Asistencia.query.all()
    resultado = [
        {
            "id": a.id,
            "estudiante_id": a.estudiante_id,
            "materia": a.materia,
            "fecha": str(a.fecha),
            "presente": a.presente
        }
        for a in asistencias
    ]
    return jsonify(resultado), 200
