class MinHeap:
    def __init__(self):
        self.heapList = []

    def heappush(self, data):
        self.heapList.append(data)
        self.__heapifyUp(len(self.heapList) - 1)

    def heappop(self):
        """Extract Node"""
        if self.heapList:
            item = self.heapList[0]
            self.heapList[0] = self.heapList[len(self.heapList) - 1]
            self.heapList.pop()
            self.__heapifyDown()
            return item
        else:
            raise IndexError("Heap is empty!!")

    def __heapifyUp(self, i):
        while self.__hasParent(i) and self.heapList[i] < self.heapList[self.__getParentIndex(i)]:  # (>) for max heap
            self.__swap(i, self.__getParentIndex(i))
            i = self.__getParentIndex(i)

    def __heapifyDown(self):
        i = 0
        while self.__hasLeftChild(i):
            small_child = self.__getLeftChildIndex(i)
            # (>) for max heap
            if self.__hasRightChild(i) and self.heapList[self.__getRightChildIndex(i)] < self.heapList[small_child]:
                small_child = self.__getRightChildIndex(i)

            if self.heapList[i] < self.heapList[small_child]:  # (>) for max heap
                break
            else:
                self.__swap(i, small_child)
            i = small_child

    def __swap(self, i, j):
        self.heapList[i], self.heapList[j] = self.heapList[j], self.heapList[i]

    def peek(self):
        if self.heapList:
            return self.heapList[0]
        raise IndexError("Heap is empty!!")

    def size(self):
        if self.heapList:
            return self.length
        return 0

    def levelOrder(self):
        if self.heapList is None:
            return
        else:
            for i in range(len(self.heapList)):
                print(self.heapList[i], end=" ")

    # Helper Functions
    def __getParentIndex(self, i):
        return (i - 1) // 2

    def __getLeftChildIndex(self, i):
        return (i * 2) + 1

    def __getRightChildIndex(self, i):
        return (i * 2) + 2

    def __hasParent(self, i):
        return self.__getParentIndex(i) >= 0

    def __hasLeftChild(self, i):
        return self.__getLeftChildIndex(i) < len(self.heapList)

    def __hasRightChild(self, i):
        return self.__getRightChildIndex(i) < len(self.heapList)


heap = MinHeap()
heap.heappush(5)
heap.heappush(10)
heap.heappush(20)
heap.heappush(30)
heap.heappush(40)
heap.heappush(80)
heap.heappush(60)
heap.heappush(50)

print(heap.heappop())
heap.levelOrder()
