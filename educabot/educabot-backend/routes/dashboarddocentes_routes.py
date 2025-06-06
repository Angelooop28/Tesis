from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.usuario import Usuario
from models.curso import Curso
from models.matricula import Matricula
from models.curso_asignatura import CursoAsignatura
from models.asignatura import Asignatura
from extensions.extensions import db

docentes_bp = Blueprint('docentes_bp', __name__)

@docentes_bp.route('/api/dashboard-docentes', methods=['GET'])
@jwt_required()
def obtener_datos_docente():
    identidad = get_jwt_identity()
    id_usuario = identidad.get("id_usuario")

    docente = Usuario.query.filter_by(id_usuario=id_usuario, rol='docente').first()
    if not docente:
        return jsonify({'mensaje': 'Usuario no autorizado'}), 403

    cursos = Curso.query.filter_by(id_docente=docente.id_usuario).all()
    datos = []

    for curso in cursos:
        curso_asignaturas = CursoAsignatura.query.filter_by(id_curso=curso.id_curso).all()

        for ca in curso_asignaturas:
            asignatura = Asignatura.query.get(ca.id_asignatura)
            if asignatura:
                matriculas = Matricula.query.filter_by(id_curso=curso.id_curso).all()

                estudiantes = []
                for m in matriculas:
                    estudiante = Usuario.query.filter_by(id_usuario=m.id_estudiante).first()
                    if estudiante:
                        estudiantes.append({
                            "id": estudiante.id_usuario,
                            "nombre": estudiante.nombre
                        })

                datos.append({
                    "id": asignatura.id_asignatura,
                    "nombre": asignatura.nombre,
                    "estudiantes": estudiantes
                })

    return jsonify({
        "materias": datos,
        "docente": docente.nombre
    }), 200
