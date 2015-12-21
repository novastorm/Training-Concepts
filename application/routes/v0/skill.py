import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('skill', __name__)
api = Blueprint('skill_api', __name__)

label = "Skill"

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

@api.route('/skills')
@api.route('/skills.json')
def api_index():
    return jsonify(
        skill_list=['index.json'], 
        req=request.values)

@api.route('/skills;saved')
def api_index_saved():
    return jsonify(
        skill_list_saved=['index.json'], 
        req=request.values)


@api.route('/skills/<int:skill_id>')
@api.route('/skills/<int:skill_id>.json')
def api_show(skill_id):
    setattr(request, 'skill_id', skill_id)    
    record = _showRecord(request)
    return jsonify(skill=record)

@api.route('/skills', methods=['POST'])
def api_store():
    record = _storeRecord(request)
    return jsonify(skill=record)

@api.route('/skills/<int:skill_id>', methods=['PUT'])
def api_update(skill_id):
    setattr(request, 'skill_id', skill_id)
    record = _updateRecord(request)
    return jsonify(skill=record)

@api.route('/skills/<int:skill_id>', methods=['DELETE'])
def api_destroy(skill_id):
    setattr(request, 'skill_id', skill_id)
    record = _destroyRecord(request)
    return jsonify(skill=record)
