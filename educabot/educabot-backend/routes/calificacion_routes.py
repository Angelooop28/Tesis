from flask import Blueprint, request, jsonify
from models.models import Calificacion
from extensions.extensions import db

calificacion_bp = Blueprint("calificacion_bp", __name__, url_prefix="/api/calificaciones")

@calificacion_bp.route("/agregar", methods=["POST"])
def agregar_calificacion():
    data = request.get_json()
    nueva_calificacion = Calificacion(
        materia=data.get("materia"),
        calificacion=data.get("calificacion"),
    )
    db.session.add(nueva_calificacion)
    db.session.commit()
    return jsonify({"mensaje": "Calificación agregada exitosamente"}), 201

@calificacion_bp.route("/listar", methods=["GET"])
def listar_calificaciones():
    calificaciones = Calificacion.query.all()
    resultado = [{"materia": c.materia, "calificacion": c.calificacion} for c in calificaciones]
    return jsonify(resultado)
