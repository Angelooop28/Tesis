class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin2024@localhost:5432/bd_educabot'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'clave_secreta'
    CORS_ORIGINS = 'http://localhost:8080'
