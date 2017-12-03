import unittest
import day3


class TestDay3(unittest.TestCase):

    def test_day3(self):
        self.assertEqual(day3.find_number_of_steps(1), 0)
        self.assertEqual(day3.find_number_of_steps(12), 3)
        self.assertEqual(day3.find_number_of_steps(23), 2)
        self.assertEqual(day3.find_number_of_steps(1024), 31)


if __name__ == '__main__':
    unittest.main()
