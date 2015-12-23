import json
import unittest

from app import app

label = "Skill-Exercise"
skill_id = '1'
exercise_id = '2'

class apiSkillExerciseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        res = self.app.get('/api/v0/skills/%s/exercises' % skill_id)
        data = res.data
        assert data == "%s %s Index" % (label, skill_id)

    def test_store(self):
        res = self.app.post('/api/v0/skills/%s/exercises' % skill_id)
        data = res.data
        assert data == "%s %s _storeRecord" % (label, skill_id)

    def test_destroy(self):
        res = self.app.delete('/api/v0/skills/%s/exercises/%s' % (skill_id, exercise_id))
        data = res.data
        assert data == "%s %s %s _destroyRecord" % (label, skill_id, exercise_id)
