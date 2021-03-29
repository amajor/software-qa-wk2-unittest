import unittest
from app.heap import Heap


class TestHeap(unittest.TestCase):
    def setUp(self):
        self._heap = Heap()
        """Empty the heap for fresh start each test"""
        self._heap.empty()

    def test_empty(self):
        expected = True
        result = self._heap.empty()
        self.assertEqual(expected, result)

    def test_is_not_empty(self):
        self._heap.add(10)
        expected = False
        result = self._heap.empty()
        self.assertEqual(expected, result)

    def test_add(self):
        self._heap.add(10)
        self._heap.add(20)
        self._heap.add(30)
        self.assertFalse(self._heap.empty())

    def test_remove_min(self):
        minimum = 3
        self._heap.add(minimum)
        self._heap.add(4)
        self._heap.add(5)
        self._heap.add(25)
        result = self._heap.remove_min()
        self.assertEqual(minimum, result)

    def test_remove_min_from_empty(self):
        """Test case: empty heap raises ValueError"""
        with self.assertRaises(Exception):
            self._heap.remove_min()

    def test_remove_min_large_numbers(self):
        minimum = 3999
        self._heap.add(4567)
        self._heap.add(59850)
        self._heap.add(6501)
        self._heap.add(minimum)
        result = self._heap.remove_min()
        self.assertEqual(minimum, result)

    def test_remove_min_negative_numbers(self):
        minimum = -99999
        self._heap.add(-4567)
        self._heap.add(-59850)
        self._heap.add(-6501)
        self._heap.add(minimum)
        result = self._heap.remove_min()
        self.assertEqual(minimum, result)

    def test_heap_sort(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        unsorted_list = [2, 8, 4, 7, 5, 1, 6, 3]
        result = self._heap.heap_sort(unsorted_list)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
