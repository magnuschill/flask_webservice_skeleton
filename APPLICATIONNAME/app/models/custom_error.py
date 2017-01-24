"""
Class which models an Error returned to an service consumer
Based on api spec for errors
    https://github.secureserver.net/Enterprise-Standards/api-design#readme
"""
class FieldError(object):
    """The Fields error object. Used to describe input validation errors"""
    def __init__(self, path, code, message):
        self.path = path
        self.code = code
        self.message = message

class CustomError(object):
    """The Standard error object"""
    def __init__(self, code, message, fields=None):
        self.code = code
        self.message = message
        if fields:
            self.fields = format_field_errors(fields)

def format_field_errors(error_messages):
    """Takes a dict of validation errors and formats them into the spec"""
    fields = []
    for param, messages in error_messages.items():
        details = " AND ".join(messages)
        field = FieldError(param, "VALIDATION_FAILED", details)
        fields.append(field)
    return fields
