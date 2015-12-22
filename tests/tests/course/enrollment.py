import json
import unittest

from app import app

label = "Course-Enrollment"
course_id = '1'

class apiCourseEnrollmentTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_store(self):
        res = self.app.post('/api/v0/courses/%s/enroll' % course_id)
        data = res.data
        assert data == "%s %s enroll" % (label, course_id)

    def test_destroy(self):
        res = self.app.delete('/api/v0/courses/%s/drop' % course_id)
        data = res.data
        assert data == "%s %s drop" % (label, course_id)
