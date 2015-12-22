import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('exercise', __name__)
api = Blueprint('exercise_api', __name__)

label = "Exercise"

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

@api.route('/exercises')
@api.route('/exercises.json')
def api_index():
    records = _getIndex()
    return jsonify(
        exercise_list=[records], 
        req=request.values)

@api.route('/exercises/<int:exercise_id>')
@api.route('/exercises/<int:exercise_id>.json')
def api_show(exercise_id):
    setattr(request, 'exercise_id', exercise_id)    
    record = _showRecord(request)
    return jsonify(exercise=record)

@api.route('/exercises', methods=['POST'])
def api_store():
    record = _storeRecord(request)
    return jsonify(exercise=record)

@api.route('/exercises/<int:exercise_id>', methods=['PUT'])
def api_update(exercise_id):
    setattr(request, 'exercise_id', exercise_id)
    record = _updateRecord(request)
    return jsonify(exercise=record)

@api.route('/exercises/<int:exercise_id>', methods=['DELETE'])
def api_destroy(exercise_id):
    setattr(request, 'exercise_id', exercise_id)
    record = _destroyRecord(request)
    return jsonify(exercise=record)
