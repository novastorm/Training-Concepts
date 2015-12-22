import json
import unittest

from app import app

label = "Profile"
uri = '/api/v0/profile'
course_id = '1'

class apiProfileTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_store(self):
        res = self.app.get(uri)
        data = res.data
        assert data == "%s index" % label

    def test_destroy(self):
        res = self.app.put(uri)
        data = res.data
        assert data == "%s update" % label
