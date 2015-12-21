import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('course_skill', __name__)
api = Blueprint('course_skill_api', __name__)

label = "Course-Skill"

def _getIndex():
    """Retrieve %s index data

    return index data""" % label
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

@api.route('/courses/<int:course_id>/skills')
@api.route('/courses/<int:course_id>/skills.json')
def api_index(course_id):
    setattr(request, 'course_id', course_id)    
    return jsonify(course_skill_list=['index.json'])

@api.route('/courses/<int:course_id>/skills/<int:skill_id>')
@api.route('/courses/<int:course_id>/skills/<int:skill_id>.json')
def api_show(course_id, skill_id):
    setattr(request, 'course_id', course_id)    
    setattr(request, 'skill_id', skill_id)    
    record = _showRecord(request)
    return jsonify(skill=record)

@api.route('/courses/<int:course_id>/skills', methods=['POST'])
def api_store(course_id):
    setattr(request, 'course_id', course_id)    
    record = _storeRecord(request)
    return jsonify(skill=record)

@api.route('/courses/<int:course_id>/skills/<int:skill_id>', methods=['PUT'])
def api_update(course_id, skill_id):
    setattr(request, 'course_id', course_id)    
    setattr(request, 'skill_id', skill_id)
    record = _updateRecord(request)
    return jsonify(skill=record)

@api.route('/courses/<int:course_id>/skills/<int:skill_id>', methods=['DELETE'])
def api_destroy(course_id, skill_id):
    setattr(request, 'course_id', course_id)    
    setattr(request, 'skill_id', skill_id)
    record = _destroyRecord(request)
    return jsonify(skill=record)
