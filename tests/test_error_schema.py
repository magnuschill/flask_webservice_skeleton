"""
Test Suite for error schemas
"""
import unittest
from basetest import BaseTestSuite
from app.schemas import custom_error
from app.models.custom_error import CustomError

class ErrorSchemaTest(BaseTestSuite):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.my_schema = custom_error.ErrorSchema()

    def test_dumps_error(self):
        """Properly serialize an error without validation errors"""
        my_error = CustomError('ERROR_CODE','an error message')
        serialized = self.my_schema.dumps(my_error).data
        self.assertTrue('"message": "an error message"' in serialized)
        self.assertTrue('"code": "ERROR_CODE"' in serialized)
        self.assertTrue('"fields":' not in serialized)

    def test_dumps_error_fields(self):
        """Properly serialize an error with validation errors"""
        my_error_fields = CustomError('ERROR_CODE', 'an error message', {'param1': ['wrong type']})
        serialized = self.my_schema.dumps(my_error_fields).data
        self.assertTrue('"fields": [{' in serialized)
        self.assertTrue('"path": "param1"' in serialized)
        self.assertTrue('"message": "wrong type"' in serialized)


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
