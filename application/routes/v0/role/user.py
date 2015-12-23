import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('role_user', __name__)
api = Blueprint('role_user_api', __name__)

label = "Role-User"

def _getIndex(req):
    """Retrieve %s index data

    return index data""" % label
    return "%s Index" % label

def _storeRecord(req):
    """Store Record"""
    return "%s _storeRecord" % label

def _destroyRecord(req):
    """Destroy Record"""
    return "%s _destroyRecord" % label


###############################################################################
#
# API routes
#

@api.route('/roles/<int:role_id>/users')
@api.route('/roles/<int:role_id>/users.json')
def api_index(role_id):
    setattr(request, 'role_id', role_id)  
    records = _getIndex(request)  
    return jsonify(user_list=[records])

@api.route('/roles/<int:role_id>/users', methods=['POST'])
def api_store(role_id):
    setattr(request, 'role_id', role_id)    
    record = _storeRecord(request)
    return jsonify(user=record)

@api.route('/roles/<int:role_id>/users/<int:user_id>', methods=['DELETE'])
def api_destroy(role_id, user_id):
    setattr(request, 'role_id', role_id)
    setattr(request, 'user_id', user_id)
    record = _destroyRecord(request)
    return jsonify(user=record)
