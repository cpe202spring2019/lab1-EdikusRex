import unittest
from lab1 import *


class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        # Tests possible positions of max int
        self.assertEqual(max_list_iter([1, 2, 3, 4]), 4)
        self.assertEqual(max_list_iter([1, 2, 4, 3]), 4)
        self.assertEqual(max_list_iter([1, 4, 2, 3]), 4)
        self.assertEqual(max_list_iter([4, 1, 2, 3]), 4)

    def test_max_list_iter_border(self):
        # Tests border cases
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([0, 0, 0, 0]), 0)
        self.assertEqual(max_list_iter([0, 0, 0, 1]), 1)
        self.assertEqual(max_list_iter([1, 0, 0, 0]), 1)
        self.assertEqual(max_list_iter([1, 1, 1, 0]), 1)
        self.assertEqual(max_list_iter([0, 1, 1, 1]), 1)

    def test_reverse_rec(self):
        # Tests a few random lists
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])

        tlist = [-19, -52, 5, 82, 69]
        tlist_rev = [69, 82, 5, -52, -19]
        self.assertEqual(reverse_rec(tlist), tlist_rev)

        tlist = [87, 89, 15, 65, 88]
        tlist_rev = [88, 65, 15, 89, 87]
        self.assertEqual(reverse_rec(tlist), tlist_rev)

        tlist = [-71, 21, 88, 76, -38]
        tlist_rev = [-38, 76, 88, 21, -71]
        self.assertEqual(reverse_rec(tlist), tlist_rev)

        tlist = [-35, -63, -38, 56, -44]
        tlist_rev = [-44, 56, -38, -63, -35]
        self.assertEqual(reverse_rec(tlist), tlist_rev)

        tlist = [56, -27, 39, 12, -57]
        tlist_rev = [-57, 12, 39, -27, 56]
        self.assertEqual(reverse_rec(tlist), tlist_rev)

    def test_reverse_rec_border(self):
        # Tests Value Error
        with self.assertRaises(ValueError):
            reverse_rec(None)

    def test_bin_search(self):
        # Tests search for every position in a list of 10
        tlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(bin_search(1, 0, len(tlist) - 1, tlist), 0)
        self.assertEqual(bin_search(2, 0, len(tlist) - 1, tlist), 1)
        self.assertEqual(bin_search(3, 0, len(tlist) - 1, tlist), 2)
        self.assertEqual(bin_search(4, 0, len(tlist) - 1, tlist), 3)
        self.assertEqual(bin_search(5, 0, len(tlist) - 1, tlist), 4)
        self.assertEqual(bin_search(6, 0, len(tlist) - 1, tlist), 5)
        self.assertEqual(bin_search(7, 0, len(tlist) - 1, tlist), 6)
        self.assertEqual(bin_search(8, 0, len(tlist) - 1, tlist), 7)
        self.assertEqual(bin_search(9, 0, len(tlist) - 1, tlist), 8)
        self.assertEqual(bin_search(10, 0, len(tlist) - 1, tlist), 9)

    def test_bin_search_border(self):
        # Tests border cases
        with self.assertRaises(ValueError):
            bin_search(1, 1, 1, None)
        tlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(bin_search(1, 0, len(tlist) - 1, tlist), None)
        tlist = [15, 65, 87, 88, 89]
        self.assertEqual(bin_search(20, 0, len(tlist) - 1, tlist), None)
        tlist = [-57, -27, 12, 39, 56]
        self.assertEqual(bin_search(90, 0, len(tlist) - 1, tlist), None)

        tlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        self.assertEqual(bin_search(1, 0, len(tlist) - 1, tlist), 9)
        tlist = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(bin_search(-1, 0, len(tlist) - 1, tlist), 0)
        tlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(bin_search(0, 0, len(tlist) - 1, tlist), 0)


if __name__ == "__main__":
    unittest.main()
