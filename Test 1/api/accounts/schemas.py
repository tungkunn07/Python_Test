from marshmallow import Schema, fields

class AccountGetSchema(Schema):
    account_id = fields.Integer()

class AccountPostSchema(Schema):
    login = fields.String(required=True)
    password = fields.String(required=True)
    phone = fields.String()

class AccountPatchSchema(Schema):
    account_id = fields.Integer(required=True)
    login = fields.String()
    password = fields.String()
    phone = fields.String()

class AccountDeleteSchema(Schema):
    account_id = fields.Integer(required=True)