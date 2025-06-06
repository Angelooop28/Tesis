import os
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from extensions.extensions import db
from models.usuario import Usuario
from models.entrega_tarea import EntregaTarea

upload_bp = Blueprint('upload_bp', __name__)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_bp.route('/api/subir-tarea', methods=['POST'])
@jwt_required()
def subir_tarea_pdf():
    identidad = get_jwt_identity()
    id_usuario = identidad.get("id_usuario")

    estudiante = Usuario.query.filter_by(id_usuario=id_usuario, rol='estudiante').first()
    if not estudiante:
        return jsonify({"mensaje": "No autorizado"}), 403

    if 'archivo' not in request.files:
        return jsonify({"mensaje": "No se encontró el archivo"}), 400

    archivo = request.files['archivo']
    materia = request.form.get("materia")

    if not archivo or not allowed_file(archivo.filename):
        return jsonify({"mensaje": "Archivo inválido"}), 400

    # Guardar archivo
    filename = secure_filename(f"{estudiante.nombre}_{materia}.pdf")
    path_destino = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    archivo.save(path_destino)

    # Registrar en base de datos
    entrega = EntregaTarea(
        id_estudiante=estudiante.id_usuario,
        materia=materia,
        nombre_archivo=filename,
        ruta_archivo=path_destino
    )
    db.session.add(entrega)
    db.session.commit()

    return jsonify({"mensaje": "Archivo subido y registrado", "ruta": path_destino}), 200
