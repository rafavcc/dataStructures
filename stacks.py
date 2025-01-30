class Stack:

    class Node:
        def __init__(self, data = None):
            self.next = None
            self.data = data
        
    bottom = Node()
    top = Node()
    
    def isEmpty(self):
        pass
    
    def peek(self):
        return self.top.data
    
    def add(self,data):
        if (self.bottom.data == None):
            self.bottom = self.Node(data)
            return
        newNode = self.Node(data)
        newNode.next = self.top
        self.top = newNode
    
    def remove(self):
        if (self.top.data == None):
            return self.bottom.data
        temp = self.top
        self.top = self.top.next
        return temp.data

pilha = Stack()
pilha.add("First")
pilha.add("Second")
pilha.add("Third")
print(pilha.remove())
print(pilha.remove())
print(pilha.remove())
pilha.add("First")
pilha.add("Second")
pilha.add("Third")
print(pilha.remove())
print(pilha.remove())
print(pilha.remove())
print(f'Finish')