from marshmallow import Schema, fields

class TareaSchema(Schema):
    id = fields.Int(dump_only=True)
    titulo = fields.Str(required=True)
    fecha_vencimiento = fields.Str(required=True)
    archivo_subido = fields.Str(dump_only=True)
