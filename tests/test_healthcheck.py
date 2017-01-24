"""
Test Suite for the healthcheck
"""
import unittest
from basetest import BaseTestSuite
import json
from config import API_VERSION
from run import app

class HealthCheckTest(BaseTestSuite):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()
        self.root = "/v{version}/".format(version=API_VERSION)

    def test_healthcheck_gives_200(self):
        response = self.app.get(self.root + 'healthchecks/ping')
        self.assertEqual(response.status_code, 200)

    def test_custom_405(self):
        response = self.app.delete(self.root + 'healthchecks/ping')
        self.assertEqual(response.status_code, 405)
        result = json.loads(response.data)
        self.assertEqual(result['code'], 'METHOD_NOT_ALLOWED')

    def test_custom_404(self):
        response = self.app.get(self.root + 'healthchecks/marklar')
        self.assertEqual(response.status_code, 404)
        result = json.loads(response.data)
        self.assertEqual(result['code'], '404_NOT_FOUND')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
