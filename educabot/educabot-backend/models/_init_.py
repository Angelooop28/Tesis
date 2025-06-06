from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importar modelos para registrarlos en SQLAlchemy
from extensions.extensions import db
from .tarea import Tarea
from .asistencia import Asistencia
from .calificacion import Calificacion
<<<<<<< HEAD
from models.matricula import Matricula
from models.usuario import Usuario
from models.curso import Curso
from .curso_asignatura import CursoAsignatura


# Exportar para que otros módulos puedan importarlos desde models directamente
__all__ = ["db", "Tarea", "Asistencia", "Calificacion", "Matricula", "Usuario", "Curso", "CursoAsignatura"]
=======

# Exportar db y modelos
__all__ = ["db", "Tarea", "Asistencia", "Calificacion"]
>>>>>>> parent of 9dbd3cc (avance 4)
