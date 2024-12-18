import os

class Config:
    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin2024@localhost:5432/bd_educabot'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuración de JWT
    JWT_SECRET_KEY = 'clave_secreta'
    
    # Configuración de CORS
    CORS_ORIGINS = 'http://localhost:8080'

    # Configuración de carpetas de subida
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    ASISTENCIA_FOLDER = os.path.join(UPLOAD_FOLDER, 'asistencia')
    TAREAS_FOLDER = os.path.join(UPLOAD_FOLDER, 'tareas')
    TEMP_FOLDER = os.path.join(UPLOAD_FOLDER, 'temp')

    # Asegurarse de que las carpetas existan
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(ASISTENCIA_FOLDER, exist_ok=True)
    os.makedirs(TAREAS_FOLDER, exist_ok=True)
    os.makedirs(TEMP_FOLDER, exist_ok=True)
