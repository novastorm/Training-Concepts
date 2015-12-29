'''
enrollment.py

This module handles 

'''

import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('course_enrollment', __name__)
api = Blueprint('course_enrollment_api', __name__)

label = "Course-Enrollment"

def _enrollCourse(req):
    """Enroll Course"""
    return "%s %s enroll" % (label, req.course_id)

def _dropCourse(req):
    """Drop Course"""
    return "%s %s drop" % (label, req.course_id)


###############################################################################
#
# API routes
#

@api.route('/courses/<int:course_id>/enroll', methods=['POST'])
def api_enroll(course_id):
    setattr(request, 'course_id', course_id)    
    record = _enrollCourse(request)
    return record

@api.route('/courses/<int:course_id>/drop', methods=['DELETE'])
def api_drop(course_id):
    setattr(request, 'course_id', course_id)    
    record = _dropCourse(request)
    return record
