import json
from flask import Blueprint, jsonify, request
from services import compound_service
from models.compound import Compound
from werkzeug.exceptions import HTTPException

api = Blueprint('users', 'users')


@api.route('/compounds', methods=['GET'])
def api_get():
    """Get all entities"""
    compounds = compound_service.get()
    return [compound.as_dict() for compound in compounds]


@api.route('/compounds', methods=['POST'])
def api_post():
    """Create entity"""
    compound = compound_service.post(request.json)
    return jsonify(compound.as_dict())


@api.route('/users/<string:id>', methods=['PUT'])
def api_put(_id):
    """Update entity by ID"""
    body = request.json
    body['id'] = _id
    res = compound_service.put(body)
    return jsonify(res.as_dict()) if isinstance(res, Compound) else jsonify(res)


@api.route('/compounds/<string:id>', methods=['DELETE'])
def api_delete(_id):
    """Delete entity by ID"""
    res = compound_service.delete(_id)
    return jsonify(res)


@api.errorhandler(HTTPException)
def handle_exception(exp):
    """Return JSON format for HTTP errors."""
    # start with the correct headers and status code from the error
    response = exp.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        'success': False,
        "message": exp.description
    })
    response.content_type = "application/json"
    return response
