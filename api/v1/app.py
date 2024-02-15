#!/usr/bin/python3
""" API for edvy """
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)

cores = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error Handler"""
    return jsonify({'error': "Not found"}), 404

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port='5001', threaded=True, debug=True)
