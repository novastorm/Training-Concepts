import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('course_student', __name__)
api = Blueprint('course_student_api', __name__)

label = "Course-Student"

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

@api.route('/courses/<int:course_id>/students')
@api.route('/courses/<int:course_id>/students.json')
def api_index(course_id):
    setattr(request, 'course_id', course_id)  
    records = _getIndex(request)  
    return jsonify(student_list=[records])

@api.route('/courses/<int:course_id>/students', methods=['POST'])
def api_store(course_id):
    setattr(request, 'course_id', course_id)    
    record = _storeRecord(request)
    return jsonify(student=record)

@api.route('/courses/<int:course_id>/students/<int:student_id>', methods=['DELETE'])
def api_destroy(course_id, student_id):
    setattr(request, 'course_id', course_id)
    setattr(request, 'student_id', student_id)
    record = _destroyRecord(request)
    return jsonify(student=record)
