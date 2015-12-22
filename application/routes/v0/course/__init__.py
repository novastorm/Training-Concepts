import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('course', __name__)
api = Blueprint('course_api', __name__)

label = "Course"

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

@api.route('/courses')
@api.route('/courses.json')
def api_index():
    records = _getIndex()
    return jsonify(course_list=[records])

@api.route('/courses/<int:course_id>')
@api.route('/courses/<int:course_id>.json')
def api_show(course_id):
    setattr(request, 'course_id', course_id)    
    record = _showRecord(request)
    return jsonify(course=record)

@api.route('/courses', methods=['POST'])
def api_store():
    record = _storeRecord(request)
    return jsonify(course=record)

@api.route('/courses/<int:course_id>', methods=['PUT'])
def api_update(course_id):
    setattr(request, 'course_id', course_id)
    record = _updateRecord(request)
    return jsonify(course=record)

@api.route('/courses/<int:course_id>', methods=['DELETE'])
def api_destroy(course_id):
    setattr(request, 'course_id', course_id)
    record = _destroyRecord(request)
    return jsonify(course=record)
