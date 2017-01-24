"""
Example of a RESTful resource
"""

from flask import jsonify
from flask.views import MethodView

class ExampleResource(MethodView):

    def get(self, user_id=None):
        return jsonify({"Result": "Success"}), 200

    def put(self, user_id=None):
        return jsonify({"Result": "Success"}), 200

    def patch(self, user_id=None):
        return jsonify({"Result": "Success"}), 200

    def delete(self, user_id=None):
        return jsonify({"Result": "Success"}), 200

    def post(self, user_id=None):
        return jsonify({"Result": "Success"}), 200
