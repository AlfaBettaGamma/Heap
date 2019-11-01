class Heap:

    def __init__(self):
        self.HeapArray = [] # хранит неотрицательные числа-ключи
        
    def MakeHeap(self, a, depth):
        if a == []:
            return False
        else:
            self.HeapArray = [None] * sum([2**i for i in range(depth + 1)])
            for item in a:
                self.Add(item)
            return True
    # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth 

    def GetMax(self):
        if self.HeapArray == []:
            return -1
        else:
            max_element = self.HeapArray[0]
            index_min_el = self.HeapArray.index(min(filter(None, self.HeapArray)))
            self.HeapArray[0] = self.HeapArray[index_min_el]
            self.HeapArray[index_min_el] = None
            parent = 0
            while 2*parent+2 < len(self.HeapArray) and self.HeapArray[2*parent+2]:
                if self.HeapArray[parent] is not None and self.HeapArray[parent] < max(self.HeapArray[2*parent+1], self.HeapArray[2*parent+2]):
                    child = self.HeapArray.index(max(self.HeapArray[2*parent+1], self.HeapArray[2*parent+2]))
                    self.HeapArray[parent], self.HeapArray[child] = self.HeapArray[child], self.HeapArray[parent]
                    parent = child
                else:
                    break
                
        return max_element 
        # вернуть значение корня и перестроить кучу
        # если куча пуста

    def Add(self, key):
        if None in self.HeapArray:
            child = self.HeapArray.index(None)
            self.HeapArray[child] = key
            while child > 0:
                parent = int((child-1)/2)
                if self.HeapArray[child] > self.HeapArray[parent]:
                    self.HeapArray[child], self.HeapArray[parent] = self.HeapArray[parent], self.HeapArray[child]
                    child = parent
                else:
                    break
            return True
    # добавляем новый элемент key в кучу и перестраиваем её
        else:
            return False # если куча вся заполнена



