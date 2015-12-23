import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, '../application')

from app import app

from tests.course import *
from tests.course.exercise import *
from tests.course.enrollment import *
from tests.course.question import *
from tests.course.skill import *
from tests.course.student import *
from tests.exercise import *
from tests.exercise.exercise import *
from tests.exercise.skill import *
from tests.profile import *
from tests.profile.course import *
from tests.role import *
from tests.role.user import *
from tests.skill import *
from tests.skill.exercise import *
from tests.skill.skill import *
from tests.student import *
from tests.user import *
from tests.user.role import *

if __name__ == '__main__':
    unittest.main()
