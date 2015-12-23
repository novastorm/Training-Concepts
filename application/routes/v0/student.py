import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('student', __name__)
api = Blueprint('student_api', __name__)

label = "Student"

def _getIndex():
    """Retrieve %s index data

    return index data"""
    return "%s Index" % label

def _showRecord(req):
    """Show Record"""
    return "%s %s _showRecord" % (label, req.student_id)

def _storeRecord(req):
    """Store Record"""
    return "%s _storeRecord" % (label)

def _updateRecord(req):
    """Update Record"""
    return "%s %s _updateRecord" % (label, req.student_id)

def _destroyRecord(req):
    """Destroy Record"""
    return "%s %s _destroyRecord" % (label, req.student_id)


###############################################################################
#
# API routes
#

@api.route('/students')
@api.route('/students.json')
def api_index():
    records = _getIndex()
    return records

@api.route('/students/<int:student_id>')
@api.route('/students/<int:student_id>.json')
def api_show(student_id):
    setattr(request, 'student_id', student_id)    
    record = _showRecord(request)
    return record

@api.route('/students', methods=['POST'])
def api_store():
    record = _storeRecord(request)
    return record

@api.route('/students/<int:student_id>', methods=['PUT'])
def api_update(student_id):
    setattr(request, 'student_id', student_id)
    record = _updateRecord(request)
    return record

@api.route('/students/<int:student_id>', methods=['DELETE'])
def api_destroy(student_id):
    setattr(request, 'student_id', student_id)
    record = _destroyRecord(request)
    return record
