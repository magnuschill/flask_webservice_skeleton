#!/usr/bin/python
"""
Entry point for application
Can be run from command line to start under flask dev server, or
Target for wsgi compliant web server
"""
from app.routes import app

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80, debug=True)
    app.run(debug=True, port=80)
