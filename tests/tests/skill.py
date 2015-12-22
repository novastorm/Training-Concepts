import json
import unittest

from app import app

label = "Skill"

class apiSkillTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        res = self.app.get('/api/v0/skills')
        data = json.loads(res.data)
        assert data['skill_list'][0] == "%s Index" % label

    def test_show(self):
        res = self.app.get('/api/v0/skills/1')
        data = json.loads(res.data)
        assert data['skill'] == "%s _showRecord" % label

    def test_store(self):
        res = self.app.post('/api/v0/skills')
        data = json.loads(res.data)
        assert data['skill'] == "%s _storeRecord" % label

    def test_update(self):
        res = self.app.put('/api/v0/skills/1')
        data = json.loads(res.data)
        assert data['skill'] == "%s _updateRecord" % label

    def test_destroy(self):
        res = self.app.delete('/api/v0/skills/1')
        data = json.loads(res.data)
        assert data['skill'] == "%s _destroyRecord" % label
