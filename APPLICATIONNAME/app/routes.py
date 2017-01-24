"""
Initialization point for the web application
Defines routes and associates them with their flask-restful implementation
"""
import config
from app.resources.example_resource import ExampleResource
from app.resources.healthcheck import HealthCheck
from .error_handlers import app

if config.environment == "PROD":
    # Don't prettyprint json if we are in prod (override flask default)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# CORS Support
@app.after_request
def after_request(response):
    # Allow CORS for swagger UI, except when in prod
    if config.environment != "PROD":
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, api_key, Authorization, Origin, X-Requested-With, Accept')
        response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, PATCH, OPTIONS')
    return response

route_base = '/v{version}/'.format(version=config.API_VERSION)


##### Routes #####
# Example resource
app.add_url_rule(route_base + 'users/<string:user_id>',
                 view_func=ExampleResource.as_view('ExampleView'))
# Same resource but allow an optional identifier
app.add_url_rule(route_base + 'users/',
                 view_func=ExampleResource.as_view('ExampleViewNoId'))

# Simple healthcheck
app.add_url_rule(route_base + 'healthchecks/ping', view_func=HealthCheck.as_view('HealthCheck'))
app.add_url_rule('/healthchecks/ping', view_func=HealthCheck.as_view('HealthCheck2'))

