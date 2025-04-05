from marshmallow import Schema, fields


class ProdCreateDtoSchema(Schema):
    name = fields.List(fields.Str(), required=True)


class ProdSchema(Schema):
    id = fields.List(fields.Str())
    name = fields.String()
    price = fields.Float()


class ProdGetManyParams(Schema):
    page = fields.Int(required=True)
    limit = fields.Int(required=True)