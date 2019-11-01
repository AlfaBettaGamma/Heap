from heap import Heap

import unittest
from random import choice



class ls2_test(unittest.TestCase):

    def test_make_heap(self):
        array = [10, 15, 6, 22, 34, 86]
        new_heap = Heap()
        new_heap.MakeHeap(array, 2)
        etalon_array = [86, 22, 34, 10, 15, 6, None]
        self.assertEqual(new_heap.HeapArray, etalon_array)

    def test_empty_heap_add(self):
        new_heap = Heap()
        self.assertEqual(new_heap.Add(15), False)

    def test_make_heap_2(self):
        array = [10, 15, 37, 22, 56, 86]
        new_heap = Heap()
        new_heap.MakeHeap(array, 2)
        array2 = [10, 15, 6, 22, 34, 86]
        new_heap.MakeHeap(array2, 2)
        etalon_array = [86, 22, 34, 10, 15, 6, None]
        self.assertEqual(new_heap.HeapArray, etalon_array)


    def test_GetMax(self):
        array = [10, 15, 37, 22, 56, 86]
        new_heap = Heap()
        new_heap.MakeHeap(array, 2)
        roots = [86, 56, 37, 22, 15, 10]
        for ind in range(6):
            self.assertEqual(new_heap.GetMax(), roots[ind])
        empty_array = [None] * 7
        self.assertEqual(len(new_heap.HeapArray), 7)
        self.assertEqual(new_heap.HeapArray, empty_array)

    def test_GetMax_make_new(self):
        array = [10, 15, 6, 22, 34, 86]
        new_heap = Heap()
        new_heap.MakeHeap(array, 2)
        for key in array:
            self.assertEqual(new_heap.GetMax() is not None, True)
            self.assertEqual(len(new_heap.HeapArray), 7)
        new_heap.MakeHeap(array, 2)
        self.assertEqual(len(new_heap.HeapArray), 7)
        etalon_array = [86, 22, 34, 10, 15, 6, None]
        self.assertEqual(new_heap.HeapArray, etalon_array)

    def test_GetMax_make_new2(self):
        array = [10, 15, 6, 22, 34, 86]
        new_heap = Heap()
        new_heap.MakeHeap(array, 2)
        for key in range(3):
            self.assertEqual(new_heap.GetMax() is not None, True)
        new_heap.MakeHeap(array, 2)
        self.assertEqual(len(new_heap.HeapArray), 7)
        etalon_array = [86, 22, 34, 10, 15, 6, None]
        self.assertEqual(new_heap.HeapArray, etalon_array)

    def test_GetMax_make_new3(self):
        array = [10]
        new_heap = Heap()
        new_heap.MakeHeap(array, 1)
        self.assertEqual(new_heap.GetMax(), 10)
        self.assertEqual(new_heap.HeapArray, [None, None, None])
        new_heap.MakeHeap(array, 1)
        self.assertEqual(len(new_heap.HeapArray), 3)
        etalon_array = [10, None, None]
        self.assertEqual(new_heap.HeapArray, etalon_array)

    def test_GetMax_Add(self):
        array = [10, 15, 6, 22, 34, 86]
        new_heap = Heap()
        new_heap.MakeHeap(array, 2)
        for key in range(8):
            self.assertEqual(new_heap.GetMax() is not None, True)
        for i in range(6):
            new_heap.Add(array[i])
        etalon_array = [86, 22, 34, 10, 15, 6, None]
        self.assertEqual(new_heap.HeapArray, etalon_array)

    def test_GetMax_Add2(self):
        array = [10, 15, 6, 22, 34, 86, 5]
        new_heap = Heap()
        new_heap.MakeHeap(array, 2)
        for i in range(6):
            self.assertEqual(new_heap.Add(array[i]), False)
        etalon_array = [86, 22, 34, 10, 15, 6, 5]
        self.assertEqual(new_heap.HeapArray, etalon_array)


    def test_GetMax_Add3(self):
        array = [10, 15, 6, 22, 34, 86]
        new_heap = Heap()
        new_heap.MakeHeap(array, 2)
        for i in range(82):
            self.assertEqual(new_heap.GetMax() is not None, True)
            self.assertEqual(len(new_heap.HeapArray), 7)
            self.assertEqual(new_heap.Add(choice(array)), True)
        self.assertEqual(len(new_heap.HeapArray), 7)




unittest.main()