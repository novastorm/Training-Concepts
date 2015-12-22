import json
import unittest

from app import app

label = "Course"

class apiCourseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        res = self.app.get('/api/v0/courses')
        data = json.loads(res.data)
        assert data['course_list'][0] == "%s Index" % label

    def test_show(self):
        res = self.app.get('/api/v0/courses/1')
        data = json.loads(res.data)
        assert data['course'] == "%s _showRecord" % label

    def test_store(self):
        res = self.app.post('/api/v0/courses')
        data = json.loads(res.data)
        assert data['course'] == "%s _storeRecord" % label

    def test_update(self):
        res = self.app.put('/api/v0/courses/1')
        data = json.loads(res.data)
        assert data['course'] == "%s _updateRecord" % label

    def test_destroy(self):
        res = self.app.delete('/api/v0/courses/1')
        data = json.loads(res.data)
        assert data['course'] == "%s _destroyRecord" % label
