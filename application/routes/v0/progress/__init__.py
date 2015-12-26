import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('progress', __name__)
api = Blueprint('progress_api', __name__)

label = "Progress"

def _getIndex():
    """Retrieve %s index data

    return index data"""
    return "%s Index" % label

def _showRecord(req):
    """Show Record"""
    return "%s %s _showRecord" % (label, req.progress_id)

def _storeRecord(req):
    """Store Record"""
    return "%s _storeRecord" % (label)

def _updateRecord(req):
    """Update Record"""
    return "%s %s _updateRecord" % (label, req.progress_id)

def _destroyRecord(req):
    """Destroy Record"""
    return "%s %s _destroyRecord" % (label, req.progress_id)


###############################################################################
#
# API routes
#

@api.route('/progress')
@api.route('/progress.json')
def api_index():
    records = _getIndex()
    return records

@api.route('/progress/<int:progress_id>')
@api.route('/progress/<int:progress_id>.json')
def api_show(progress_id):
    setattr(request, 'progress_id', progress_id)    
    record = _showRecord(request)
    return record

@api.route('/progress', methods=['POST'])
def api_store():
    record = _storeRecord(request)
    return record

@api.route('/progress/<int:progress_id>', methods=['PUT'])
def api_update(progress_id):
    setattr(request, 'progress_id', progress_id)
    record = _updateRecord(request)
    return record

@api.route('/progress/<int:progress_id>', methods=['DELETE'])
def api_destroy(progress_id):
    setattr(request, 'progress_id', progress_id)
    record = _destroyRecord(request)
    return record
