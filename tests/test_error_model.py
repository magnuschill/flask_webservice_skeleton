"""
Test Suite for  errors model
"""
import unittest
from basetest import BaseTestSuite
from app.models import custom_error

class ErrorModelTest(BaseTestSuite):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_instantiate_error(self):
        """Can create an error object"""
        my_code = 'ERROR_CODE'
        my_message = 'an error message'
        error = custom_error.CustomError(my_code, my_message)
        self.assertEqual(error.code, my_code)
        self.assertEqual(error.message, my_message)
        self.assertFalse(hasattr(error, 'fields'))

    def test_instantiate_fielderr(self):
        """Can Create a Field Validation error object"""
        my_path = 'param_name'
        my_code = 'ERROR_CODE_FOR_FIELD'
        my_message = 'an error message about a field'
        error = custom_error.FieldError(my_path, my_code, my_message)
        self.assertEqual(error.path, my_path)
        self.assertEqual(error.code, my_code)
        self.assertEqual(error.message, my_message)

    def test_instantiate_error_with_field(self):
        """Can create an error object with a field validation error object"""
        my_code = 'ERROR_CODE'
        my_message = 'an error message'
        validation_err = {'param1': ['wrong type']}
        error = custom_error.CustomError(my_code, my_message, validation_err)
        self.assertEqual(error.code, my_code)
        self.assertEqual(error.message, my_message)
        self.assertTrue(hasattr(error, 'fields'))
        self.assertIsInstance(error.fields[0], custom_error.FieldError)

    def test_format_multiple_errors(self):
        """Error dicts are transformed to error objects properly"""
        pname1 = 'param1'
        pname2 = 'param2'
        err1 = 'wrong type'
        err2 = 'out of bounds'
        validation_err = {}
        validation_err[pname1] = [err1]
        validation_err[pname2] = [err1, err2]
        formatted = custom_error.format_field_errors(validation_err)
        for field_err in formatted:
            if field_err.path == pname1:
                self.assertEqual(field_err.message, err1)
            if field_err.path == pname2:
                self.assertEqual(field_err.message, err1 + ' AND ' + err2)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
