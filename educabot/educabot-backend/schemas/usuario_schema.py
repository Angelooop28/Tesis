from marshmallow import Schema, fields

class LoginSchema(Schema):
    email = fields.Email(required=True, error_messages={"required": "El email es obligatorio."})
    password = fields.Str(required=True, error_messages={"required": "La contraseña es obligatoria."})

class RegisterSchema(Schema):
    nombre = fields.Str(required=True, error_messages={"required": "El nombre es obligatorio."})
    email = fields.Email(required=True, error_messages={"required": "El email es obligatorio."})
    password = fields.Str(required=True, error_messages={"required": "La contraseña es obligatoria."})
    rol = fields.Str(required=True, error_messages={"required": "El rol es obligatorio."})
