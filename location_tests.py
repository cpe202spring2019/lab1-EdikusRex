import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("Not SLO", 4, 5)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")
        self.assertNotEqual(repr(loc1), "Location('SLO', 35.3, -120.7)")

    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("Not SLO", 4, 5)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertNotEqual(loc, loc1)
        self.assertEqual(loc, loc2)
        self.assertNotEqual(loc, "hat")


if __name__ == "__main__":
    unittest.main()
