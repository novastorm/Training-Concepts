import json
import os
import unittest

from app import app

label = "Progress-Activity"
route = '/api/v0/progress'
res_label = 'activity'

class apiProgressActivityTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        uri = os.path.join(route, res_label)
        res = self.app.post(uri)
        data = res.data
        self.assertEqual(data, "%s _storeRecord" % label, "HEllo")
