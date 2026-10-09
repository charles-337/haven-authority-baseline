import unittest
from app import add

class T(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 2), 4)
