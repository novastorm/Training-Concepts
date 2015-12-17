import flask

from flask import Blueprint
from flask import abort
from flask import jsonify

course = Blueprint('course', __name__)
course_api = Blueprint('course_api', __name__)
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

@course_api.route('/')
@course_api.route('.json')
def api_index():
    return jsonify(category_list=['index.json'])

@course_api.route('/<int:category_id>')
@course_api.route('/<int:category_id>.json')
def api_show(category_id):
    setattr(request, 'category_id', category_id)    
    record = _showRecord(request)
    return jsonify(category=record)

@course_api.route('/', methods=['POST'])
def api_store():
    record = _storeRecord(request)
    return jsonify(category=record)

@course_api.route('/<int:category_id>', methods=['PUT'])
def api_update(category_id):
    setattr(request, 'category_id', category_id)
    record = _updateRecord(request)
    return jsonify(category=record)

@course_api.route('/<int:category_id>', methods=['DELETE'])
def api_destroy(category_id):
    setattr(request, 'category_id', category_id)
    record = _destroyRecord(request)
    return jsonify(category=record)

