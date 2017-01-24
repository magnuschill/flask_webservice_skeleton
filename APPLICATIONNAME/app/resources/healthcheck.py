"""
Basic endpoint which can be hit as a healthcheck
"""
from flask.views import MethodView
from flask import jsonify

class HealthCheck(MethodView):
    def get(self):
        return jsonify({"Result": "Success"}), 200
