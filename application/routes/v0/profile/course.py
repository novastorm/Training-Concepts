import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('profile_course', __name__)
api = Blueprint('profile_course_api', __name__)

label = "Profile-Course"

def _getIndex(req):
    """Retrieve %s index data

    return index data""" % label
    return "%s %s Index" % (label, req.profile_id)


###############################################################################
#
# API routes
#

@api.route('/profile/<int:profile_id>/courses')
@api.route('/profile/<int:profile_id>/courses.json')
def api_index(profile_id):
    setattr(request, 'profile_id', profile_id)  
    records = _getIndex(request)
    return records
