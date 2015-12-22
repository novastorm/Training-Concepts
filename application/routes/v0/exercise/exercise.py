import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('exercise_exercise', __name__)
api = Blueprint('exercise_exercise_api', __name__)

label = "Exercise-Exercise"

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

@api.route('/exercises/<int:exercise_id>/exercises')
@api.route('/exercises/<int:exercise_id>/exercises.json')
def api_index(exercise_id):
    setattr(request, 'exercise_id', exercise_id)  
    records = _getIndex(request)  
    return jsonify(exercise_list=[records])

@api.route('/exercises/<int:exercise_id>/exercises', methods=['POST'])
def api_store(exercise_id):
    setattr(request, 'exercise_id', exercise_id)    
    record = _storeRecord(request)
    return jsonify(exercise=record)

@api.route('/exercises/<int:exercise_id>/exercises/<int:required_exercise_id>', methods=['DELETE'])
def api_destroy(exercise_id, required_exercise_id):
    setattr(request, 'exercise_id', exercise_id)
    setattr(request, 'required_exercise_id', required_exercise_id)
    record = _destroyRecord(request)
    return jsonify(exercise=record)
