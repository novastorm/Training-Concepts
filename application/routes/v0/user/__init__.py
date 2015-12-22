import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('user', __name__)
api = Blueprint('user_api', __name__)

label = "User"

def _getIndex():
    """Retrieve %s index data

    return index data"""
    return "%s Index" % label

def _showRecord(req):
    """Show Record"""
    return "%s _showRecord" % label

def _storeRecord(req):
    """Store Record"""
    return "%s _storeRecord" % label

def _updateRecord(req):
    """Update Record"""
    return "%s _updateRecord" % label

def _destroyRecord(req):
    """Destroy Record"""
    return "%s _destroyRecord" % label


###############################################################################
#
# API routes
#

@api.route('/users')
@api.route('/users.json')
def api_index():
    records = _getIndex()
    return jsonify(user_list=[records])

@api.route('/users/<int:user_id>')
@api.route('/users/<int:user_id>.json')
def api_show(user_id):
    setattr(request, 'user_id', user_id)    
    record = _showRecord(request)
    return jsonify(user=record)

@api.route('/users', methods=['POST'])
def api_store():
    record = _storeRecord(request)
    return jsonify(user=record)

@api.route('/users/<int:user_id>', methods=['PUT'])
def api_update(user_id):
    setattr(request, 'user_id', user_id)
    record = _updateRecord(request)
    return jsonify(user=record)

@api.route('/users/<int:user_id>', methods=['DELETE'])
def api_destroy(user_id):
    setattr(request, 'user_id', user_id)
    record = _destroyRecord(request)
    return jsonify(user=record)
