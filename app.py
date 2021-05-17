from flask import Flask, request, jsonify
from flask_restful import Api, abort
from webargs.flaskparser import parser
from logger import logger
from endpoints.status import ServiceStatus
from endpoints.zscore import Zscore


def create_app():
    """
    Creates a new Flask application.
    """
    app = Flask(__name__)
    register_error_handlers(app)
    api = Api(app, catch_all_404s=True)
    api.add_resource(ServiceStatus, '/status')
    api.add_resource(Zscore, '/company/<string:country_code>/<int:company_id>')
    return app


def handle_webargs_request_error(error, req, schema, status_code, headers):
    """
    Handling 400 errors from the API.
    """
    logger.debug(error, req, schema, status_code, headers)
    abort(400, message='Client error, please correct the request.',
          errors=error.messages)


def handle_server_error(error):
    """
    Handling 500 errors from the API.
    """
    logger.exception(f'Unhandled Exception: {error}')
    abort(500, message='Unknown error, please try again later.')


def register_error_handlers(app):
    """
    Attaching the error handlers to the Flask application.
    :param obj app: a flask application instance.
    """
    parser.error_handler(handle_webargs_request_error)
    app.register_error_handler(Exception, handle_server_error)
