import json
import unittest

from app import app

label = "Course-Question"

class apiCourseQuestionTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        res = self.app.get('/api/v0/courses/1/questions')
        data = json.loads(res.data)
        assert data['question_list'][0] == "%s Index" % label

    def test_store(self):
        res = self.app.post('/api/v0/courses/1/questions')
        data = json.loads(res.data)
        assert data['question'] == "%s _storeRecord" % label

    def test_destroy(self):
        res = self.app.delete('/api/v0/courses/1/questions/1')
        data = json.loads(res.data)
        assert data['question'] == "%s _destroyRecord" % label
