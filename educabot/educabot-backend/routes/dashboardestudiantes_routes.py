from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.usuario import Usuario
from models.matricula import Matricula
from models.curso_asignatura import CursoAsignatura
from models.asignatura import Asignatura
from models.tarea import Tarea
from models.asistencia import Asistencia
from models.calificacion import Calificacion
from extensions.extensions import db

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/api/dashboard', methods=['GET'])
@jwt_required()
def obtener_datos_estudiante():
    identidad = get_jwt_identity()
    id_usuario = identidad.get("id_usuario")

    estudiante = Usuario.query.filter_by(id_usuario=id_usuario, rol='estudiante').first()
    if not estudiante:
        return jsonify({'mensaje': 'Usuario no autorizado'}), 403

    # Materias (asignaturas)
    matriculas = Matricula.query.filter_by(id_estudiante=id_usuario).all()
    materias = []

    for m in matriculas:
        curso_asignaturas = CursoAsignatura.query.filter_by(id_curso=m.id_curso).all()
        for ca in curso_asignaturas:
            asignatura = Asignatura.query.get(ca.id_asignatura)
            if asignatura:
                materias.append({
                    "id": asignatura.id_asignatura,
                    "nombre": asignatura.nombre
                })

    # Tareas
    tareas = Tarea.query.filter_by(estudiante_id=id_usuario).all()
    lista_tareas = [{
        "id": t.id,
        "materia": t.materia.nombre if t.materia else "Sin asignar",
        "titulo": t.titulo,
        "fechaEntrega": t.fecha_vencimiento.strftime('%Y-%m-%d') if t.fecha_vencimiento else ""
    } for t in tareas]

    # Calificaciones
    calificaciones = Calificacion.query.filter_by(id_estudiante=id_usuario).all()
    lista_calificaciones = [{
        "materia": c.asignatura.nombre if c.asignatura else "Sin asignar",
        "nota": c.nota
    } for c in calificaciones]

    # Asistencias
    asistencias = Asistencia.query.filter_by(id_estudiante=id_usuario).all()
    total = len(asistencias)
    presentes = sum(1 for a in asistencias if a.estado.lower() == "presente")

    return jsonify({
        "materias": materias,
        "tareas": lista_tareas,
        "calificaciones": lista_calificaciones,
        "asistencias": {
            "asistencias": presentes,
            "total": total
        },
        "estudiante": estudiante.nombre
    }), 200
 