"""
Schema definitions representing a Go Daddy Error returned to an service consumer
Used for marshalling data
"""
import marshmallow

class FieldErrorSchema(marshmallow.Schema):
    path = marshmallow.fields.String(required=True)
    code = marshmallow.fields.String(required=True)
    message = marshmallow.fields.String()

class ErrorSchema(marshmallow.Schema):
    code = marshmallow.fields.String(required=True)
    message = marshmallow.fields.String(required=True)
    fields = marshmallow.fields.Nested('FieldErrorSchema', many=True)

