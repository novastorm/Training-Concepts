import json
import os
import unittest

from app import app

label = 'User'
route = '/api/v0/users'
index = '1'

class apiUserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        res = self.app.get(route)
        data = json.loads(res.data)
        assert data['user_list'][0] == "%s Index" % label

    def test_show(self):
        res = self.app.get(os.path.join(route, index))
        data = json.loads(res.data)
        assert data['user'] == "%s _showRecord" % label

    def test_store(self):
        res = self.app.post(route)
        data = json.loads(res.data)
        assert data['user'] == "%s _storeRecord" % label

    def test_update(self):
        res = self.app.put(os.path.join(route, index))
        data = json.loads(res.data)
        assert data['user'] == "%s _updateRecord" % label

    def test_destroy(self):
        res = self.app.delete(os.path.join(route, index))
        data = json.loads(res.data)
        assert data['user'] == "%s _destroyRecord" % label
