import json
import os
import unittest

from app import app

label = 'Role'
route = '/api/v0/roles'
res_id = '1'

class apiRoleTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_res_id(self):
        res = self.app.get(route)
        data = res.data
        assert data == "%s Index" % label

    def test_show(self):
        res = self.app.get(os.path.join(route, res_id))
        data = res.data
        assert data == "%s %s _showRecord" % (label, res_id)

    def test_store(self):
        res = self.app.post(route)
        data = res.data
        assert data == "%s _storeRecord" % (label)

    def test_update(self):
        res = self.app.put(os.path.join(route, res_id))
        data = res.data
        assert data == "%s %s _updateRecord" % (label, res_id)

    def test_destroy(self):
        res = self.app.delete(os.path.join(route, res_id))
        data = res.data
        assert data == "%s %s _destroyRecord" % (label, res_id)
