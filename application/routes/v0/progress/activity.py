import flask

from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

app = Blueprint('progress_activity', __name__)
api = Blueprint('progress_activity_api', __name__)

label = "Progress-Activity"

def _storeActivity(req):
    """Store record"""
    return "%s _storeRecord" % (label)


###############################################################################
#
# API routes
#

@api.route('/progress/activity', methods=['POST'])
def api_store():
    records = _storeActivity(request)
    return records
