import random
import QuickSort
import unittest


class TestSolution(unittest.TestCase):
    def testQuickSort(self):
        s = QuickSort.Solution()
        for i in range(100):
            list_wait_to_sort = [random.randint(-10000,10000) for i in range(1000)]
            self.assertEqual(sorted(list_wait_to_sort), s.quickSort(list_wait_to_sort, 0, len(list_wait_to_sort)-1))

if __name__ == "__main__":
    unittest.main()
