import unittest
from utils import *
from unittest.mock import Mock
from unittest.mock import patch
class TestUtils(unittest.TestCase):
    def test_checkOutPath(self):
        self.assertTrue(checkOutPath('/this/is/path.png'))
        self.assertTrue(checkOutPath('/this/is/path.jpg'))
        self.assertTrue(checkOutPath('/this/is/path.svg'))
        self.assertTrue(checkOutPath('/this/is/path.gif'))
        self.assertTrue(checkOutPath('/this/is/path.gif'))



if __name__== '__main__':
    unittest.main()