import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('profile', __name__)
api = Blueprint('profile_api', __name__)

label = "Profile"

def _getIndex():
    """Retrieve %s index data

    return index data"""
    return "%s Index" % label

def _updateRecord(req):
    """Update Record"""
    return "%s _updateRecord" % label


###############################################################################
#
# API routes
#

@api.route('/profile')
@api.route('/profile.json')
def api_index():
    return "%s index" % label

@api.route('/profile', methods=['PUT'])
def api_update():
    return "%s update" % label
