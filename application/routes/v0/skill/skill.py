import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('skill_skill', __name__)
api = Blueprint('skill_skill_api', __name__)

label = "Skill-Skill"

def _getIndex(req):
    """Retrieve %s index data

    return index data""" % label
    return "%s %s Index" % (label, req.skill_id)

def _storeRecord(req):
    """Store Record"""
    return "%s %s _storeRecord" % (label, req.skill_id)

def _destroyRecord(req):
    """Destroy Record"""
    return "%s %s %s _destroyRecord" % (label, req.skill_id, req.required_skill_id)


###############################################################################
#
# API routes
#

@api.route('/skills/<int:skill_id>/skills')
@api.route('/skills/<int:skill_id>/skills.json')
def api_index(skill_id):
    setattr(request, 'skill_id', skill_id)  
    records = _getIndex(request)  
    return records

@api.route('/skills/<int:skill_id>/skills', methods=['POST'])
def api_store(skill_id):
    setattr(request, 'skill_id', skill_id)    
    record = _storeRecord(request)
    return record

@api.route('/skills/<int:skill_id>/skills/<int:required_skill_id>', methods=['DELETE'])
def api_destroy(skill_id, required_skill_id):
    setattr(request, 'skill_id', skill_id)
    setattr(request, 'required_skill_id', required_skill_id)
    record = _destroyRecord(request)
    return record
