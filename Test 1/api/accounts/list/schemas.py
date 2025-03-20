from marshmallow import Schema, fields

class AccountListGetSchema(Schema):
    page = fields.Integer()
    per_page = fields.Integer()