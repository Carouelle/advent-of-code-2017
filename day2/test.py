import unittest
import day2
import day2_part2


class TestDay2(unittest.TestCase):

    def test_day1(self):
        self.assertEqual(day2.find_checksum("""5\t1\t9\t5
7\t5\t3
2\t4\t6\t8"""), 18)

    def test_day1_part2(self):
        self.assertEqual(day2_part2.find_checksum("""5\t9\t2\t8
9\t4\t7\t3
3\t8\t6\t5"""), 9)


if __name__ == '__main__':
    unittest.main()
