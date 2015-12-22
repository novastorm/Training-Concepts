import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('exercise_skill', __name__)
api = Blueprint('exercise_skill_api', __name__)

label = "Exercise-Skill"

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

@api.route('/exercises/<int:exercise_id>/skills')
@api.route('/exercises/<int:exercise_id>/skills.json')
def api_index(exercise_id):
    setattr(request, 'exercise_id', exercise_id)  
    records = _getIndex(request)  
    return jsonify(skill_list=[records])

@api.route('/exercises/<int:exercise_id>/skills', methods=['POST'])
def api_store(exercise_id):
    setattr(request, 'exercise_id', exercise_id)    
    record = _storeRecord(request)
    return jsonify(skill=record)

@api.route('/exercises/<int:exercise_id>/skills/<int:required_skill_id>', methods=['DELETE'])
def api_destroy(exercise_id, required_skill_id):
    setattr(request, 'exercise_id', exercise_id)
    setattr(request, 'required_skill_id', required_skill_id)
    record = _destroyRecord(request)
    return jsonify(skill=record)
