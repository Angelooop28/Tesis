from flask import Blueprint, jsonify, request
from extensions.extensions import db
from models.tarea import Tarea
from models.asistencia import Asistencia  # Nuevo modelo
from models.calificacion import Calificacion  # Nuevo modelo
from flask_jwt_extended import jwt_required
from schemas.tarea_schema import TareaSchema

tarea_bp = Blueprint("tarea_routes", __name__)
tarea_schema = TareaSchema()
tareas_schema = TareaSchema(many=True)

# --------------------------------------------
# TAREAS
# --------------------------------------------

# Obtener todas las tareas
@tarea_bp.route('/api/tareas', methods=['GET'])
@jwt_required()
def obtener_tareas():
    tareas = Tarea.query.all()
    return tareas_schema.jsonify(tareas), 200

# Obtener detalles de una tarea
@tarea_bp.route('/api/tareas/<int:id>', methods=['GET'])
@jwt_required()
def detalle_tarea(id):
    tarea = Tarea.query.get(id)
    if not tarea:
        return jsonify({"mensaje": "Tarea no encontrada"}), 404
    return tarea_schema.jsonify(tarea), 200

# Subir archivo para una tarea
@tarea_bp.route('/api/tareas/<int:id>/subir', methods=['POST'])
@jwt_required()
def subir_tarea(id):
    tarea = Tarea.query.get(id)
    if not tarea:
        return jsonify({"mensaje": "Tarea no encontrada"}), 404
    
    archivo = request.files.get("archivo")
    if archivo:
        ruta_guardado = f"./uploads/tarea_{id}.pdf"
        archivo.save(ruta_guardado)
        tarea.archivo_subido = ruta_guardado
        db.session.commit()
        return jsonify({"mensaje": "Archivo subido exitosamente"}), 200
    
    return jsonify({"mensaje": "Error al subir archivo"}), 400

# Agregar una nueva tarea (para docentes)
@tarea_bp.route('/api/tareas/agregar', methods=['POST'])
@jwt_required()
def agregar_tarea():
    data = request.get_json()
    nueva_tarea = Tarea(
        materia=data.get("materia"),
        titulo=data.get("titulo"),
        fecha_entrega=data.get("fecha_entrega")
    )
    db.session.add(nueva_tarea)
    db.session.commit()
    return jsonify({"mensaje": "Tarea agregada exitosamente"}), 201

# --------------------------------------------
# ASISTENCIA
# --------------------------------------------

# Registrar asistencia
@tarea_bp.route('/api/asistencia/registrar', methods=['POST'])
@jwt_required()
def registrar_asistencia():
    data = request.get_json()
    nueva_asistencia = Asistencia(total_asistencias=data.get("total_asistencias"))
    db.session.add(nueva_asistencia)
    db.session.commit()
    return jsonify({"mensaje": "Asistencia registrada exitosamente"}), 201

# Obtener asistencias
@tarea_bp.route('/api/asistencia', methods=['GET'])
@jwt_required()
def obtener_asistencias():
    asistencias = Asistencia.query.all()
    resultado = [{"id": a.id, "total_asistencias": a.total_asistencias} for a in asistencias]
    return jsonify(resultado), 200

# --------------------------------------------
# CALIFICACIONES
# --------------------------------------------

# Agregar calificaciones
@tarea_bp.route('/api/calificaciones/agregar', methods=['POST'])
@jwt_required()
def agregar_calificacion():
    data = request.get_json()
    nueva_calificacion = Calificacion(
        materia=data.get("materia"),
        calificacion=data.get("calificacion")
    )
    db.session.add(nueva_calificacion)
    db.session.commit()
    return jsonify({"mensaje": "Calificación agregada exitosamente"}), 201

# Obtener calificaciones
@tarea_bp.route('/api/calificaciones', methods=['GET'])
@jwt_required()
def obtener_calificaciones():
    calificaciones = Calificacion.query.all()
    resultado = [{"materia": c.materia, "calificacion": c.calificacion} for c in calificaciones]
    return jsonify(resultado), 200
