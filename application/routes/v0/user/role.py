import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('user_role', __name__)
api = Blueprint('user_role_api', __name__)

label = "User-Role"

def _getIndex(req):
    """Retrieve %s index data

    return index data""" % label
    return "%s %s Index" % (label, req.user_id)

def _storeRecord(req):
    """Store Record"""
    return "%s %s _storeRecord" % (label, req.user_id)

def _destroyRecord(req):
    """Destroy Record"""
    return "%s %s %s _destroyRecord" % (label, req.user_id, req.role_id) 


###############################################################################
#
# API routes
#

@api.route('/users/<int:user_id>/roles')
@api.route('/users/<int:user_id>/roles.json')
def api_index(user_id):
    setattr(request, 'user_id', user_id)  
    records = _getIndex(request)  
    return records

@api.route('/users/<int:user_id>/roles', methods=['POST'])
def api_store(user_id):
    setattr(request, 'user_id', user_id)    
    record = _storeRecord(request)
    return record

@api.route('/users/<int:user_id>/roles/<int:role_id>', methods=['DELETE'])
def api_destroy(user_id, role_id):
    setattr(request, 'user_id', user_id)
    setattr(request, 'role_id', role_id)
    record = _destroyRecord(request)
    return record
