import json
import unittest

from app import app

label = "Profile-Course"
profile_id = '1'

class apiProfileCourseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        res = self.app.get('/api/v0/profile/%s/courses' % profile_id)
        data = res.data
        assert data == "%s %s Index" % (label, profile_id)
