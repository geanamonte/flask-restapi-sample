from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Str(dump_only=True) # Not used for validation
    name = fields.Str(required=True) # Required must be in JSON payload
    store_id = fields.Str(required=True)
    price = fields.Float(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)