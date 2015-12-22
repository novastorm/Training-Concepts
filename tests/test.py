import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, '../application')

from app import app

from tests.course import *
from tests.course.exercise import *
from tests.course.question import *
from tests.course.skill import *
from tests.course.student import *
from tests.exercise import *
from tests.skill import *
from tests.user import *

if __name__ == '__main__':
    unittest.main()