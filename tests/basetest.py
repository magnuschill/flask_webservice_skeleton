import sys
import os
import unittest

# neccesary for running tests from the APPLICATIONNAME/ context
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../APPLICATIONNAME')))
sys.path.insert(0, os.path.abspath('..'))
os.environ['APPLICATIONNAME_ENV'] = 'TEST'

class BaseTestSuite(unittest.TestCase):
    """Base class for all test cases"""

    def __init__(self, *args, **kwargs):
        super(BaseTestSuite, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
