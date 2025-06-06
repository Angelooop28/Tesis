from marshmallow import Schema, fields, validate

class LoginSchema(Schema):
    email = fields.Email(
        required=True,
        validate=validate.Length(max=60),
        error_messages={
            "required": "El email es obligatorio.",
            "validate": "El email debe ser válido y tener un máximo de 60 caracteres."
        }
    )
    password = fields.Str(
        required=True,
        validate=validate.Length(min=6),
        error_messages={
            "required": "La contraseña es obligatoria.",
            "validate": "La contraseña debe tener al menos 6 caracteres."
        }
    )

class RegisterSchema(Schema):
    nombre = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=40),
        error_messages={
            "required": "El nombre es obligatorio.",
            "validate": "El nombre debe tener entre 1 y 40 caracteres."
        }
    )
    email = fields.Email(
        required=True,
        validate=validate.Length(max=60),
        error_messages={
            "required": "El email es obligatorio.",
            "validate": "El email debe ser válido y tener un máximo de 60 caracteres."
        }
    )
    password = fields.Str(
        required=True,
        validate=validate.Length(min=6),
        error_messages={
            "required": "La contraseña es obligatoria.",
            "validate": "La contraseña debe tener al menos 6 caracteres."
        }
    )
    rol = fields.Str(
        required=True,
        validate=validate.OneOf(["admin", "docente", "estudiante"]),
        error_messages={
            "required": "El rol es obligatorio.",
            "validate": "El rol debe ser 'admin', 'docente', o 'estudiante'."
        }
    )
