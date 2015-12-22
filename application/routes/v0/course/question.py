import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('course_question', __name__)
api = Blueprint('course_question_api', __name__)

label = "Course-Question"

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

@api.route('/courses/<int:course_id>/questions')
@api.route('/courses/<int:course_id>/questions.json')
def api_index(course_id):
    setattr(request, 'course_id', course_id)  
    records = _getIndex(request)  
    return jsonify(question_list=[records])

@api.route('/courses/<int:course_id>/questions', methods=['POST'])
def api_store(course_id):
    setattr(request, 'course_id', course_id)    
    record = _storeRecord(request)
    return jsonify(question=record)

@api.route('/courses/<int:course_id>/questions/<int:question_id>', methods=['DELETE'])
def api_destroy(course_id, question_id):
    setattr(request, 'course_id', course_id)
    setattr(request, 'question_id', question_id)
    record = _destroyRecord(request)
    return jsonify(question=record)
