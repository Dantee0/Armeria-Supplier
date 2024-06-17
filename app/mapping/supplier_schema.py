from app.models.supplier import Supplier
from marshmallow import validate, fields, Schema, post_load

"""
En esta clase se define los parametros para convertirlo a json
"""
class SupplierSchema(Schema):
    id = fields.Integer(dump_only=True) #dump_only es para que la info que envie al cliente se muestre 
    name = fields.String(required=True, validate=validate.Length(min=1, max=105))
    cuil = fields.String(required=True, validate=validate.Length(min=1, max=11))
    email = fields.String(required=True, validate=validate.Length(min=1, max=256))
    code = fields.String(required=True, validate=validate.Length(min=1, max=8))

    @post_load
    def make_user(self, data, **kwargs):
        return Supplier(**data) # los asteriscos hacen que vincule los esquemas con los modelos 