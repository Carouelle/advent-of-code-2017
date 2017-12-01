import unittest
import day1
import day1_part2


class TestStringMethods(unittest.TestCase):

    def test_day1(self):
        self.assertEqual(day1.find_sum('1122'), 3)
        self.assertEqual(day1.find_sum('1111'), 4)
        self.assertEqual(day1.find_sum('1234'), 0)
        self.assertEqual(day1.find_sum('91212129'), 9)

    def test_day1_part2(self):
        self.assertEqual(day1_part2.find_sum('1212'), 6)
        self.assertEqual(day1_part2.find_sum('1221'), 0)
        self.assertEqual(day1_part2.find_sum('123425'), 4)
        self.assertEqual(day1_part2.find_sum('123123'), 12)
        self.assertEqual(day1_part2.find_sum('12131415'), 4)


if __name__ == '__main__':
    unittest.main()
