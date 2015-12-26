import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('course_skill', __name__)
api = Blueprint('course_skill_api', __name__)

label = "Course-Skill"

def _getIndex(req):
    """Retrieve %s index data

    return index data""" % label
    return "%s %s Index" % (label, req.course_id)

def _storeRecord(req):
    """Store Record"""
    return "%s %s _storeRecord" % (label, req.course_id)

def _destroyRecord(req):
    """Destroy Record"""
    return "%s %s %s _destroyRecord" % (label, req.course_id, req.skill_id)


###############################################################################
#
# API routes
#

@api.route('/courses/<int:course_id>/skills')
@api.route('/courses/<int:course_id>/skills.json')
def api_index(course_id):
    setattr(request, 'course_id', course_id)  
    records = _getIndex(request)  
    return records

@api.route('/courses/<int:course_id>/skills', methods=['POST'])
def api_store(course_id):
    setattr(request, 'course_id', course_id)    
    record = _storeRecord(request)
    return record

@api.route('/courses/<int:course_id>/skills/<int:skill_id>', methods=['DELETE'])
def api_destroy(course_id, skill_id):
    setattr(request, 'course_id', course_id)
    setattr(request, 'skill_id', skill_id)
    record = _destroyRecord(request)
    return record
