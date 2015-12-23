import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('role', __name__)
api = Blueprint('role_api', __name__)

label = "Role"

def _getIndex():
    """Retrieve %s index data

    return index data"""
    return "%s Index" % label

def _showRecord(req):
    """Show Record"""
    return "%s %s _showRecord" % (label, req.role_id)

def _storeRecord(req):
    """Store Record"""
    return "%s _storeRecord" % (label)

def _updateRecord(req):
    """Update Record"""
    return "%s %s _updateRecord" % (label, req.role_id)

def _destroyRecord(req):
    """Destroy Record"""
    return "%s %s _destroyRecord" % (label, req.role_id)


###############################################################################
#
# API routes
#

@api.route('/roles')
@api.route('/roles.json')
def api_index():
    records = _getIndex()
    return records

@api.route('/roles/<int:role_id>')
@api.route('/roles/<int:role_id>.json')
def api_show(role_id):
    setattr(request, 'role_id', role_id)    
    record = _showRecord(request)
    return record

@api.route('/roles', methods=['POST'])
def api_store():
    record = _storeRecord(request)
    return record

@api.route('/roles/<int:role_id>', methods=['PUT'])
def api_update(role_id):
    setattr(request, 'role_id', role_id)
    record = _updateRecord(request)
    return record

@api.route('/roles/<int:role_id>', methods=['DELETE'])
def api_destroy(role_id):
    setattr(request, 'role_id', role_id)
    record = _destroyRecord(request)
    return record
