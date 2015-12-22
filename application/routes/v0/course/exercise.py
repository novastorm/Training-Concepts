import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('course_exercise', __name__)
api = Blueprint('course_exercise_api', __name__)

label = "Course-Exercise"

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

@api.route('/courses/<int:course_id>/exercises')
@api.route('/courses/<int:course_id>/exercises.json')
def api_index(course_id):
    setattr(request, 'course_id', course_id)  
    records = _getIndex(request)  
    return jsonify(exercise_list=[records])

@api.route('/courses/<int:course_id>/exercises', methods=['POST'])
def api_store(course_id):
    setattr(request, 'course_id', course_id)    
    record = _storeRecord(request)
    return jsonify(exercise=record)

@api.route('/courses/<int:course_id>/exercises/<int:exercise_id>', methods=['DELETE'])
def api_destroy(course_id, exercise_id):
    setattr(request, 'course_id', course_id)
    setattr(request, 'exercise_id', exercise_id)
    record = _destroyRecord(request)
    return jsonify(exercise=record)
