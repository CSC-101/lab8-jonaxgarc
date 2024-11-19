import unittest
import group

class Tests(unittest.TestCase):

#Task 1
    def test_groups_of_3_1(self):
        self.assertEqual(group.groups_of_3([1, 2, 3, 4, 5, 6, 7, 8, 9]), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    def test_groups_of_3_2(self):
        self.assertEqual(group.groups_of_3([3, 3, 5, 2, 1, 9, 7, 8]), [[3, 3, 5], [2, 1, 9], [7, 8]])
