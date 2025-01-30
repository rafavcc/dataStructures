class Queue:
    
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
            
    head = Node()
    tail = Node()
    
    def isEmpty(self):
        return (self.head == self.tail)

    def peek(self):
        return self.head.data
    
    def add(self, data):
        newNode = self.Node(data)
        if self.tail != None:
            self.tail.next = newNode
            self.tail = newNode
            
        if self.head.data == None:
            self.head = newNode
    
    def remove(self):
        temp = self.head
        self.head = self.head.next
        return temp.data
    
    def print(self):
        if self.isEmpty(): "Fila está vazia / Queue is empty"
        temp = self.head
        while (temp != None):
            print(temp.data)
            temp = temp.next
    
if __name__ == "__main__":
    fila = Queue()
    fila.add("Rafael")
    fila.add("Viegas")
    fila.add("Carvalho")
    fila.add("Carlos")
    fila.print()