import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get_positive(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)

    def test_get_negative(self):
        self.assertEqual(arrs.get([1, 2, 3], -1, "test"), "test")

    def test_get_zero(self):
        self.assertEqual(arrs.get([1, 2, 3], 0, "test"), 1)

    def test_slice_positive_start(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

    def test_slice_negative_start(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], -4), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -2), [2, 3])

    def test_slice_empty_list(self):
        self.assertEqual(arrs.my_slice([]), [])
