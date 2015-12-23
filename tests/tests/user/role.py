import json
import unittest

from app import app

label = "User-Role"
user_id = '1'
role_id = '2'

class apiUserRoleTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        res = self.app.get('/api/v0/users/%s/roles' % user_id)
        data = res.data
        assert data == "%s %s Index" % (label, user_id)

    def test_store(self):
        res = self.app.post('/api/v0/users/%s/roles' % user_id)
        data = res.data
        assert data == "%s %s _storeRecord" % (label, user_id)

    def test_destroy(self):
        res = self.app.delete('/api/v0/users/%s/roles/%s' % (user_id, role_id))
        data = res.data
        assert data == "%s %s %s _destroyRecord" % (label, user_id, role_id)
