import json
import unittest

from app import app

label = "Course-Skill"
res_label = 'courses'
res_id = '1'
subres_label = 'skills'
subres_id = '2'

class apiCourseSkillTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        res = self.app.get('/api/v0/%s/%s/%s' % (res_label, res_id, subres_label))
        data = res.data
        assert data == "%s %s Index" % (label, res_id)

    def test_store(self):
        res = self.app.post('/api/v0/%s/%s/%s' % (res_label, res_id, subres_label))
        data = res.data
        assert data == "%s %s _storeRecord" % (label, res_id)

    def test_destroy(self):
        res = self.app.delete('/api/v0/%s/%s/%s/%s' % (res_label, res_id, subres_label, subres_id))
        data = res.data
        assert data == "%s %s %s _destroyRecord" % (label, res_id, subres_id)
