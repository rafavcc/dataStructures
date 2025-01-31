from math import ceil

class Heap:
    '''
    Heap is tree-like data structure. It could be of two types: Min-heap, where the node is smaller than its childs; or Max-heap, where the node is bigger than its childs
    
    The heap can be represented as array. The parent and the childs of the index nodes can be accessed based on the index:
    Parent: (index - 2) / 2
    Left Child: 2 * index + 1
    Right Child: 2 * index + 2
    '''
    items = [] * 10
    size = 0
    
    # Functions to retrieve position of childs and parent
    def getLeftChildIndex(self, parentIndex):
        return (2 * parentIndex + 1)
    
    def getRightChildIndex(self, parentIndex):
        return (2 * parentIndex + 2)
    
    def getParentIndex(self, parentIndex):
        return (ceil((parentIndex-2)/2))
    
    # Functions to check if node has childs or parent
    def hasLeftChild(self, index):
        return (self.getLeftChildIndex(index) < self.size)

    def hasRightChild(self,index):
        return (self.getRightChildIndex(index) < self.size)
    
    def hasParent(self,index):
        return (self.getParentIndex(index) >= 0)
    
    # Retrieve childs or parent values
    def leftChild(self, index):
        return (self.items[2 * index + 1])
    
    def rightChild(self, index):
        return (self.items[2 * index + 2])
    
    def parent(self, index):
        return self.items[ceil((index - 2)/2)]
    
    def add(self, data):
        self.ensureExtraCapacity()
        self.items.append(data)
        self.size += 1
        self.heapifyUp()
    
    def swap(self, index1, index2):
        temp = self.items[index1]
        self.items[index1] = self.items[index2]
        self.items[index2] = temp
    
    def pool(self):
        temp = self.items[0]
        self.size -= 1 
        self.items[0] = self.items[self.size - 1]
        self.heapifyDown()
        return temp
    
    def peek(self):
        if (self.size == 0):
            raise IndexError("Heap is empty")
        else: 
            return self.items[0]
    
    def ensureExtraCapacity(self):
        if (self.size == len(self.items) - 1):
            self.items().extend([None] * self.size)
        pass
    
    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.items[index] < self.parent(index):
            self.swap(index, self.getParentIndex(index))
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            if (self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index)):
                temp = self.getRightChildIndex(index)
            else: 
                temp = self.getLeftChildIndex(index)
            if self.items[index] < self.items[temp]:
                break
            else:
                self.swap(index, temp)
            index = tempß
            
        

heap = Heap()
heap.add(8)
heap.add(6)
heap.add(4)
heap.add(2)