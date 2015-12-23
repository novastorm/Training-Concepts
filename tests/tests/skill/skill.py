import json
import unittest

from app import app

label = "Skill-Skill"
skill_id = 1
required_skill_id = 2

class apiSkillSkillTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        res = self.app.get('/api/v0/skills/%s/skills' % skill_id)
        data = res.data
        assert data == "%s %s Index" % (label, skill_id)

    def test_store(self):
        res = self.app.post('/api/v0/skills/%s/skills' % skill_id)
        data = res.data
        assert data == "%s %s _storeRecord" % (label, skill_id)

    def test_destroy(self):
        res = self.app.delete('/api/v0/skills/%s/skills/%s' % (skill_id, required_skill_id))
        data = res.data
        assert data == "%s %s %s _destroyRecord" % (label, skill_id, required_skill_id)
